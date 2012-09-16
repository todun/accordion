import argparse
import cherrypy
import pymongo
import pprint
import os

import accordion.multiplexer as multiplexer

# this monkeypatch is required to "fix" cherrypy so it will work on Heroku
from cherrypy.process import servers
def fake_wait_for_occupied_port(host, port): return
servers.wait_for_occupied_port = fake_wait_for_occupied_port

conn = pymongo.Connection(os.environ['ACCORDION_MONGO_URI'])
db = conn.accordion

class Root(object):
  pass

class File(object):
  exposed = True

  def GET(self, *args, **kwargs):
    try:
      multiplexer.read(args)
      return "<h1>Now make this work</h1>"
    except multiplexer.FileNotFoundException, e:
      return "<h1>File not found!</h1>"

  def POST(self, *args, **kwargs):
    return "<p>POST: %s</p>" % str(args)

  def PUT(self, *args, **kwargs):
    return "<p>PUT: %s</p>" % str(args)

  def DELETE(self, *args, **kwargs):
    return "<p>DELETE: %s</p>" % str(args)

class Debug(object):
  exposed = True

  def GET(self, *args, **kwargs):
    return """
      <h2>Debug:</h2>
    """

root = Root()
root.file = File()
root.debug = Debug()

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