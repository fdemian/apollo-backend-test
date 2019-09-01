# Route imports
#from api import GraphqlServer
from tornado.web import StaticFileHandler
import cgi
from os import getcwd, path
import json
from tornado.web import RequestHandler
from ariadne import QueryType, MutationType, graphql_sync, make_executable_schema, upload_scalar, combine_multipart_data

type_defs = """
      scalar Upload

      type UploadImagePayload {
        status: Boolean!,
        path: String!,
        mime_type: String!
      }

      type Query {
        hello: String!
      }

      type Mutation {
        uploadUserImage(file: Upload!): UploadImagePayload
      }
  """

query = QueryType()
mutations = MutationType()


@query.field("hello")
def resolve_hello(_, info):
    request = info.context
    user_agent = request.headers.get("User-Agent", "Guest")
    print(user_agent)
    return "Hello,Dude!"


@mutations.field("uploadUserImage")
@upload_scalar.serializer
def resolve_upload(_, info, file):
    file_name = file[0]['filename']
    file_type = file[0]['content_type']
    file_content = file[0]['body']

    current_dir = getcwd()
    file_path = path.join(current_dir, "static/") + file_name

    with open(file_path, "bw") as f:
        f.write(file_content)

    return {
     "status": True,
     "path": "static/" + file_name,
     "mime_type": file_type
    }


schema = make_executable_schema(type_defs, [query, mutations, upload_scalar])


class GraphqlServer(RequestHandler):

    # GraphQL queries are always sent as POST
    def post(self):

        content_type = self.request.headers['Content-Type']

        if "multipart/form-data" in content_type:
            try:
                operations = json.loads(self.get_body_argument("operations", default=None, strip=False))
                map = json.loads(self.get_body_argument("map", default=None, strip=False))
                data = combine_multipart_data(operations, map, self.request.files)

            except:
                self.set_status(400, "Error")
                self.set_header("Access-Control-Allow-Origin", "*")
                self.set_header("Content-Type", "application/jsonp;charset=UTF-8")

                return

        else:
            data = json.loads(self.request.body.decode("utf-8"))

        # Note: Passing the request to the context is optional.
        success, result = graphql_sync(schema, data, context_value=self.request, debug=True)

        status_code = 200 if success else 400
        status_text = 'Ok' if success else "Error"

        self.set_status(status_code, status_text)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/jsonp;charset=UTF-8")

        if success:
          self.write(result)

        return


def get_app_routes(static_path, notifications_enabled):
    routes = [
       (r'/graphql', GraphqlServer),
       (r'/graphql/(.*)', GraphqlServer),
       (r"/static/(.*)", StaticFileHandler, { "path": static_path }),
       (r"/(manifest\.json)", StaticFileHandler, { "path": static_path }),
       (r"/(favicon\.ico)", StaticFileHandler, { "path": static_path }),
    ]

    return routes
