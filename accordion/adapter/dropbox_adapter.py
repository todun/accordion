from dropbox import client, rest, session

APP_KEY = 'id9ana8urw7ed3z'
APP_SECRET = 'ducj44njp6wjhbw'
ACCESS_TYPE = 'app_folder'

class DropboxAdapter:

  @staticmethod
  def get_authorized_client(auth_info):
    """Get an authorized client using auth_info.

    Args:
      - ``auth_info``: A tuple of (key, secret) representing the access token Dropbox assigned to this app and user

    Returns:
      - ``client.DropboxClient(sess)``: The authorized client

    """
    sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
    sess.set_token(auth_info['key'], auth_info['secret'])
    return client.DropboxClient(sess)

  @staticmethod
  def read(auth_info, path):
    """Get the file specified by the path.

    Args:
      - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /Dropbox/accordion/

    Returns:
      - ``f``: The file specified by the path; you need to call f.read() to actually get the content
      - ``metadata``: The metadata of the file

    """
    client = DropboxAdapter.get_authorized_client(auth_info)
    f, metadata = client.get_file_and_metadata('/'+path)
    return f, metadata

  @staticmethod
  def update(auth_info, local_path, remote_path, overwrite):
    """Upload the file specified by local_path to remote_path

    Args:
      - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``local_path``: A path pointing toward the file, relative to the local root
      - ``remote_path``: A path pointing toward the location where the file needs to be saved, not including file name

    Returns:
      - ``metadata``: The metadata of the file specified by the path 

    """
    client = DropboxAdapter.get_authorized_client(auth_info)
    f = open(local_path)
    metadata = client.put_file('/'+remote_path, f, overwrite)
    return metadata

  @staticmethod
  def delete(auth_info, path):
    """Delete the file specified by the path

    Args:
      - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /

    Returns:
      - ``metadata``: The metadata of the file deleted

    """
    client = DropboxAdapter.get_authorized_client(auth_info)
    metadata = client.file_delete(path)
    return metadata

  @staticmethod
  def metadata(auth_info, path):
    """Delete the file specified by the path

    Args:
      - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /

    Returns:
      - ``metadata``: The metadata of the file deleted

    """
    client = DropboxAdapter.get_authorized_client(auth_info)
    f, metadata = client.get_file_and_metadata()
    return metadata

  @staticmethod
  def remaining_space(auth_info):
    """Returns the remaining space (in bytes) of the account corresponding to auth_info

    Args:
      - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user

    Returns:
      - ``quota - shared_quota - normal_quota``: The remaining space of the account corresponding to auth_info

    """
    client = DropboxAdapter.get_authorized_client(auth_info)
    account_info = client.account_info()
    quota = account_info['quota_info']['quota']
    shared_quota = account_info['quota_info']['shared']
    normal_quota = account_info['quota_info']['normal']
    return quota - shared_quota - normal_quota