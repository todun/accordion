import pymongo
import pprint
import os
from accordion.dropbox import DropboxAdapter
from accordion.google_drive import GoogleDriveAdapter

db = pymongo.Connection(os.environ['ACCORDION_MONGO_URI'])

FileNotFoundExceptionMessage = "The file does not exist."

@staticmethod
def read(path):
  f = _get_file(path)
  if f == None:
    raise FileNotFoundException(FileNotFoundExceptionMessage)
  else:
    adapter = _get_adapter(f.service)
    # Find the file whose name is id
    return adapter.read(_get_auth_info(f), f["_id"])

@staticmethod
def update(file_object, path, mime_type="text/plain"):
  f = _get_file(path)
  if f == None:
    f = _add_file(file_object, path, mime_type)

  adapter = _get_adapter(f['service'])

  return adapter.update(_get_auth_info(f), file_object, f['_id'])

@staticmethod
def delete(path):
  f = _get_file(path)
  if f == None:
    raise FileNotFoundException(FileNotFoundExceptionMessage)

  adapter = _get_adapter(f['service'])
  return adapter.delete(_get_auth_info(f), f['_id'])

@staticmethod
def metadata(path):
  f = _get_file(path)
  if f == None:
    raise FileNotFoundException(FileNotFoundExceptionMessage)
  adapter = _get_adapter(f['service'])
  return adapter.metadata(_get_auth_info(f), f['id'])

@staticmethod
def remaining_space():
  total_remaining_space = 0
  for account in db.accounts.find():
    adapter = _get_adapter()
    total_remaining_space += adapter.remaining_space(account['auth_info'])
  return total_remaining_space

@staticmethod
def total_space():
  total_total_space = 0
  for account in db.accounts.find():
    adapter = _get_adapter()
    total_total_space += adapter.total_space(account['auth_info'])
  return total_total_space

@staticmethod
def unused_space():
  total_unused_space = 0
  for account in db.accounts.find():
    adapter = _get_adapter()
    total_unused_space += adapter.unused_space(account['auth_info'])
  return total_unused_space

@staticmethod
def _add_file(file_object, path, mime_type):
  """
  Creates a new file object in the collection "files"
  """
  path = path.split('/')
  is_dir
  if file_object == None:
    is_dir = True
  else:
    is_dir = False 
  for account in db.accounts.find():
    adapter = _get_adapter(account['service'])
    if (adapter.unused_space() > _get_size(file_object)):
      account_id = account['account_id']
      break

  f = {"path": path,
       "is_dir": is_dir,
       "account_id": account_id,
       "mime_type": mime_type}

  db.files.insert(f)

@staticmethod
def _get_size(fileobject):
  fileobject.seek(0,2) # move the cursor to the end of the file
  size = fileobject.tell()
  return size

@staticmethod
def _get_adapter(service):
  """
  Returns an adapter that corresponds to the given service
  """
  if (service == 'dropbox'):
    return DropboxAdapter
  elif (service == 'google_drive'):
    return GoogleDriveAdapter

@staticmethod
def _get_file(path):
  """
  Returns a dictionary corresponds 
  """
  return db.files.find_one({"path": path})

@staticmethod
def _get_auth_info(f):
  """
  Returns auth_info of the account that is in charge of the give file f
  """
  account = db.accounts.find_one({"_id": f["account_id"]})
  return account["auth_info"]