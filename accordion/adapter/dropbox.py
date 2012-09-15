from dropbox import client, rest, session
from abstract import AbstractAdapter

APP_KEY = 'id9ana8urw7ed3z'
APP_SECRET = 'ducj44njp6wjhbw'
ACCESS_TYPE = 'app_folder'

class DropboxAdapter(AbstractAdapter):

  @staticmethod
  def _get_authorized_client(auth_info):
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
  def read(auth_info, ID):
    """Get the file whose name is ID.

    Args:
    - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
    - ``ID``: A hashed ID that points to a file, relative to /Dropbox/Apps/Accordion/

    Returns:
    - ``f``: The file specified by the path; you need to call f.read() to actually get the content
    - ``metadata``: The metadata of the file

    """
    client = DropboxAdapter.get_authorized_client(auth_info)
    f, metadata = client.get_file_and_metadata('/'+ID)
    return f, metadata

  @staticmethod
  def update(auth_info, local_path, ID, overwrite):
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
    client = DropboxAdapter.get_authorized_client(auth_info)
    f = open(local_path)
    metadata = client.put_file('/'+ID, f, overwrite)
    return metadata

  @staticmethod
  def delete(auth_info, ID):
    """Delete the file specified by the path

    Args:
    - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
    - ``ID``: A hashed ID that points to a file, relative to /Dropbox/Apps/Accordion/

    Returns:
    - ``metadata``: The metadata of the file deleted

    """
    client = DropboxAdapter.get_authorized_client(auth_info)
    metadata = client.file_delete(path)
    return metadata

  @staticmethod
  def metadata(auth_info, ID):
    """Delete the file specified by the path

    Args:
    - ``auth_info``: A dictionary of (key, secret) representing the access token Dropbox assigned to this app and user
    - ``ID``: A hashed ID that points to a file, relative to /Dropbox/Apps/Accordion/

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