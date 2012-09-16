import argparse
import cherrypy

import pymongo
import pprint
import os

connection = pymongo.Connection(os.environ['ACCORDION_MONGO_URI'])

class Root(object):
  def index(self):
    return "<p>index</p>"

  index.exposed = True

class File(object):
  exposed = True

  def GET(self, *args, **kwargs):
    return "GET: %s" % str(args)

  def POST(self, *args, **kwargs):
    return "POST: %s" % str(args)

  def PUT(self, *args, **kwargs):
    return "PUT: %s" % str(args)

  def DELETE(self, *args, **kwargs):
    return "DELETE: %s" % str(args)

root = Root()
root.file = File()

conf = {
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