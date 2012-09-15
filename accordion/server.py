import argparse
import cherrypy

class Root(object):
  pass

root = Root()

conf = {
  'global': {
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 8000,
  },
  '/': {
    'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
  }
}

#cherrypy.quickstart(root, '/', conf)

def main():
  parser = argparse.ArgumentParser(prog='accordion-server', description='Accordion Cloud Aggregation')

  parser.add_argument('-p', '--port', metavar="PORT")
  parser.add_argument('-c', '--config', metavar="PATH")

  args = parser.parse_args()

  