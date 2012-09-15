import re
from setuptools import setup

def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)

    return requirements

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
  install_requires = parse_requirements('requirements.txt')
)