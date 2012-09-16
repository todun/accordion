import json
import pprint as pp

import os
import sys

sys.path.insert(0, '../')

from accordion import multiplexer

f, metadata = multiplexer.read(["foo", "bar.txt"])
print f
print metadata