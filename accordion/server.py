import argparse
import cherrypy

from pymongo import *
import pprint

connection = Connection(environ[ACCORDION_MONGO_URI])

class Root(object):
  pass

root = Root()

conf = {
  'global': {
    'server.socket_host': '0.0.0.0',
  },
  '/': {
    'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
  }
}

def main():
  parser = argparse.ArgumentParser(prog='accordion-server', description='Accordion Cloud Aggregation')

  parser.add_argument('-p', '--port', metavar="PORT", type=int, required=True)
  parser.add_argument('-c', '--config', metavar="PATH")

  args = parser.parse_args()

  cherrypy.config.update({'server.socket_host': '0.0.0.0'})
  cherrypy.config.update({'server.socket_port': args.port})
  cherrypy.quickstart(root, '/', conf)