import sys
import dropbox
import os

def _get_authorized_client(auth_info):
  """Get an authorized client using auth_info.

  Args:
  - ``auth_info``: A tuple of (key, secret) representing the access token Dropbox assigned to this app and user

  Returns:
  - ``client.DropboxClient(sess)``: The authorized client

  """
  sess = session.DropboxSession(os.environ['DROPBOX_APP_KEY'], os.environ['DROPBOX_APP_SECRET'], 'app_folder')
  sess.set_token(auth_info['key'], auth_info['secret'])
  return dropbox.client.DropboxClient(sess)

def read(auth_info, ID):
  """Get the file whose name is ID.

  Args:
  - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
  - ``ID``: A hashed ID that points to a file, relative to /Dropbox/Apps/Accordion/

  Returns:
  - ``f``: The file specified by the path; you need to call f.read() to actually get the content
  - ``metadata``: The metadata of the file

  """
  client = get_authorized_client(auth_info)
  f, metadata = client.get_file_and_metadata('/'+ID)
  return f, metadata

def update(auth_info, file_object, ID):
  """Upload the file specified by local_path to remote_path

  Args:
  - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
  - ``local_path``: A path pointing toward the file, relative to the local root
  - ``ID``: A hashed ID that points to a file, relative to /Dropbox/Apps/Accordion/
  - ``overwrite``: A boolean value specifying what happens if a file with the same path exists.

  Returns:
  - ``metadata``: The metadata of the file specified by the path;
                  you should check the name of the file via metadata if you specify overwrite=false;
                  if there exists a file with the same path and name, the uploaded file will get a different name

  """
  client = get_authorized_client(auth_info)
  metadata = client.put_file('/'+ID, file_object, True)
  return metadata

def delete(auth_info, ID):
  """Delete the file specified by the path

  Args:
  - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
  - ``ID``: A hashed ID that points to a file, relative to /Dropbox/Apps/Accordion/

  Returns:
  - ``metadata``: The metadata of the file deleted

  """
  client = get_authorized_client(auth_info)
  metadata = client.file_delete(path)
  return metadata

def metadata(auth_info, ID):
  """Delete the file specified by the path

  Args:
  - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
  - ``ID``: A hashed ID that points to a file, relative to /Dropbox/Apps/Accordion/

  Returns:
  - ``metadata``: The metadata of the file deleted

  """
  client = get_authorized_client(auth_info)
  f, metadata = client.get_file_and_metadata()
  return metadata

def remaining_space(auth_info):
  """Returns the remaining space (in bytes) of the account corresponding to auth_info

  Args:
  - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user

  Returns:
  - ``quota - shared_quota - normal_quota``: The remaining space of the account corresponding to auth_info

  """
  client = get_authorized_client(auth_info)
  account_info = client.account_info()
  quota = account_info['quota_info']['quota']
  shared_quota = account_info['quota_info']['shared']
  normal_quota = account_info['quota_info']['normal']
  return quota - shared_quota - normal_quota

def total_space(auth_info):
  client = get_authorized_client(auth_info)
  account_info = client.account_info()
  quota = account_info['quota_info']['quota']
  return quota