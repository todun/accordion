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
  print "hello"
  parser = argparse.ArgumentParser(prog='PROG', description='Accordion Cloud Aggregation')
  subparsers = parser.add_subparsers()

  subparser_run = subparsers.add_parser('run')

  subparser_run.add_argument('-p', '--port', metavar="PORT")
  subparser_run.add_argument('-c', '--config', metavar="PATH")

  args = parser.parse_args()

  print args