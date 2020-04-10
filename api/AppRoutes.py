# Route imports
#from api import GraphqlServer
from tornado.web import StaticFileHandler
import cgi
from os import getcwd, path
import json
from api.GraphqlServer import GraphQLServer

def get_app_routes(static_path, notifications_enabled):
    routes = [
       (r'/graphql', GraphqlServer),
       (r'/graphql/(.*)', GraphqlServer),
       (r"/static/(.*)", StaticFileHandler, { "path": static_path }),
       (r"/(manifest\.json)", StaticFileHandler, { "path": static_path }),
       (r"/(favicon\.ico)", StaticFileHandler, { "path": static_path }),
    ]

    return routes
