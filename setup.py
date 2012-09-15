from setuptools import setup

setup(
  name = 'accordion',
  version = '0.0.1',
  author = 'Dylan A. Lukes, Derek Chiang, Siyu Song, Cathy Lee',
  author_email = 'lukes.dylan@gmail.com, derekchiang93@gmail.com, magicmirror2ndmix@gmail.com, cathysmklee@gmail.com',
  packages = ['accordion'],
  scripts = ['bin/accordion-server'],
  url = '',
  license = 'LICENSE.txt',
  description = 'Online/offline storage aggregation server/client/...',
  long_description = open('README.rst').read(),
  install_requires = [
    "cherrypy >= 3.2.2",
    "dropbox  >= 1.4",
    "pymongo  >= 2.3"
  ],
)