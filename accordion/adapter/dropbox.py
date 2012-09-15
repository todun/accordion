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
    sess.set_token(auth_info[0], auth_info[1])
    return client.DropboxClient(sess)

  @staticmethod
  def read(self, auth_info, path):
    """Get the file specified by the path.

    Args:
      - ``auth_info``: A tuple of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /Dropbox/accordion/

    Returns:
      - ``out``: The file specified by the path 
      - ``metadata``: The metadata of the file

    """
    client = get_authorized_client(auth_info)
    
    return client.get_file_and_metadata('/'+path).read()

  @staticmethod
  def update(self, auth_info, path):
    """Upload the file specified by the path

    Args:
      - ``auth_info``: A tuple of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /

    Returns:
      - ``metadata``: The metadata of the file specified by the path 

    """
    client = get_authorized_client(auth_info)
    f = open(path)
    metadata = client.put_file('/'+path, f)
    return metadata

  @staticmethod
  def delete(self, auth_info, path):
    """Delete the file specified by the path

    Args:
      - ``auth_info``: A tuple of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /

    Returns:
      - ``metadata``: The metadata of the file deleted

    """
    client = get_authorized_client(auth_info)
    metadata = client.file_delete(path)
    return metadata

  @staticmethod
  def metadata(self, auth_info, path):
    """Delete the file specified by the path

    Args:
      - ``auth_info``: A tuple of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /

    Returns:
      - ``metadata``: The metadata of the file deleted

    """
    client = get_authorized_client(auth_info)
    f, metadata = client.get_file_and_metadata()
    return metadata