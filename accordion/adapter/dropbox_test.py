from dropbox import client, rest, session
from dropbox_adapter import DropboxAdapter
import cPickle

inFile = open('access_token', 'r')
token_dictionary = cPickle.load(inFile)
inFile.close()
path = 'ABC'

DropboxAdapter.update(token_dictionary, path, path, overwrite=False)

f, metadata = DropboxAdapter.read(token_dictionary, path)
out = open(path+'D', 'w')
print metadata
out.write(f.read())

DropboxAdapter.delete(token_dictionary, path)