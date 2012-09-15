import json

from apiclient.discovery import build
from apiclient.http import MediaFileUpload

class GoogleDriveAdapter(AbstractAdapter):

  @staticmethod
  def get_drive_service(auth_info):
    """Get an Google Drive service object using stored credential information.

    Args:
      - ``auth_info``: A dictionary of credential information, directly from credentials.to_json()

    Returns:
      - ``drive_service``: The Google Drive service object to do all the file operations

    """

    credentials.from_json(json.load())
    http = httplib2.Http()
    http = credentials.authorize(http)
    
    return build('drive', 'v2', http=http)

  @staticmethod
  def read(self, auth_info, path):
    """Get the file specified by the path.

    Args:
    - ``auth_info``: A dictionary of credential information, directly from credentials.to_json()
      - ``path``: The path pointing toward the file, relative to /accordion/

    Returns:
      - ``out``: The file specified by the path 
      - ``metadata``: The metadata of the file

    """

    file_id = _get_file_id_from_path(path)
    file = drive_service.files().get(fileId=file_id).execute()
    
    download_url = file['downloadUrl']
    if download_url:
      resp, content = drive_service._http.request(download_url)
      if resp.status == 200:
        return content
    
  @staticmethod
  def update(self, auth_info, path):
    """Upload the file specified by the path. Overwrite if the file already exists.

    Args:
    - ``auth_info``: A dictionary of credential information, directly from credentials.to_json()
      - ``path``: The path pointing toward the file, relative to /accordion/

    Returns:
      - ``metadata``: The metadata of the file specified by the path 

    """
    
    media_body = MediaFileUpload(path, mimetype='binary/octet-stream', resumable=True)
    body = {
      'title': path,
      'description': '',
      'mimeType': 'binary/octet-stream'
    }
        
    file_id = _get_file_id_from_path(path)
    if file_id == None:
      updated_file = service.files().update(fileId=file_id, body=file, media_body=media_body).execute()
      return updated_file
    else:    
      inserted_file = drive_service.files().insert(body=body, media_body=media_body).execute()
      return inserted_file
    
  @staticmethod
  def delete(self, auth_info, path):
    """Delete the file specified by the path

    Args:
      - ``auth_info``: A tuple of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /

    Returns:
      - ``metadata``: The metadata of the file deleted

    """
    
    param = {'maxResults': 1, 'q': "title = '"+ path + "'", 'fields': 'items/id'}
    file_list_info = drive_service.files().list(**param).execute()
    file_id = file_list_info['items'][0]['id']
    service.files().delete(fileId=file_id).execute()
    return file_list_info['items'][0]

  @staticmethod
  def metadata(self, auth_info, path):
    """Delete the file specified by the path

    Args:
      - ``auth_info``: A tuple of (key, secret) representing the access token Dropbox assigned to this app and user
      - ``path``: The path pointing toward the file, relative to /

    Returns:
      - ``metadata``: The metadata of the file deleted

    """
    file_id = _get_file_id_from_path(path)
    file_metadata = service.files().get(fileId=file_id).execute()
    return file_metadata
    
  def _get_file_id_from_path(path):
    param = {'maxResults': 1, 'q': "title = '"+ path + "'", 'fields': 'items/id'}
    file_list_info = drive_service.files().list(**param).execute()
    if len(file_list_info['items']) == 0:
      return None
    else:
      return file_list_info['items'][0]['id']