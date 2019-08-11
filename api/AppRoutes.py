# Route imports
#from graphene_tornado.schema import schema
from graphene_tornado.tornado_graphql_handler import TornadoGraphQLHandler
from tornado.web import StaticFileHandler

from graphene import ObjectType, String, Schema

class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)

def get_app_routes(static_path, notifications_enabled):
    routes = [
       (r'/graphql', TornadoGraphQLHandler, dict(graphiql=True, schema=schema)),
       (r'/graphql/batch', TornadoGraphQLHandler, dict(graphiql=True, schema=schema, batch=True)),
       (r'/graphql/graphiql', TornadoGraphQLHandler, dict(graphiql=True, schema=schema)),
       (r"/static/(.*)", StaticFileHandler, {"path": static_path}),
       (r"/(manifest\.json)", StaticFileHandler, {"path": static_path}),
       (r"/(favicon\.ico)", StaticFileHandler, {"path": static_path}),
    ]

    return routes
