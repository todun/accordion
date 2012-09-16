import pymongo
import pprint
import os
import accordion.adapter.dropbox as dropbox_adapter

conn = pymongo.Connection(os.environ['ACCORDION_MONGO_URI'])
db = conn.test

class FileNotFoundException(Exception): pass

def read(path):
  f = _get_file(path)
  if f == None:
    raise FileNotFoundException()
  else:
    adapter = _get_adapter(f['service'])
    # Find the file whose name is id
    return adapter.read(_get_auth_info(f), f["_id"])

def update(file_object, path, mime_type="text/plain"):
  f = _get_file(path)
  if f == None:
    f = _add_file(file_object, path, mime_type)

  adapter = _get_adapter(f['service'])

  return adapter.update(_get_auth_info(f), file_object, f['_id'])

def delete(path):
  f = _get_file(path)
  if f == None:
    raise FileNotFoundException()

  adapter = _get_adapter(f['service'])
  return adapter.delete(_get_auth_info(f), f['_id'])

def metadata(path):
  f = _get_file(path)
  if f == None:
    raise FileNotFoundException()
  adapter = _get_adapter(f['service'])
  return adapter.metadata(_get_auth_info(f), f['id'])

def remaining_space():
  total_remaining_space = 0
  for account in db.accounts.find():
    adapter = _get_adapter()
    total_remaining_space += adapter.remaining_space(account['auth_info'])
  return total_remaining_space

def total_space():
  total_total_space = 0
  for account in db.accounts.find():
    adapter = _get_adapter()
    total_total_space += adapter.total_space(account['auth_info'])
  return total_total_space

def unused_space():
  total_unused_space = 0
  for account in db.accounts.find():
    adapter = _get_adapter()
    total_unused_space += adapter.unused_space(account['auth_info'])
  return total_unused_space

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

def _get_size(fileobject):
  fileobject.seek(0,2) # move the cursor to the end of the file
  size = fileobject.tell()
  return size

def _get_adapter(service):
  """
  Returns an adapter that corresponds to the given service
  """
  if (service == 'dropbox'):
    return dropbox_adapter
  # elif (service == 'google_drive'):
    # return google_drive_adapter

def _get_file(path):
  """
  Returns a dictionary corresponds 
  """
  return db.files.find_one({"path": path})

def _get_auth_info(f):
  """
  Returns auth_info of the account that is in charge of the give file f
  """
  account = db.accounts.find_one({"_id": f["account_id"]})
  return account["auth_info"]