import json
import pprint
import httplib2

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2Credentials

from abstract import AbstractAdapter

class GoogleDriveAdapter(AbstractAdapter):

  @staticmethod
  def _get_drive_service(auth_info):
    """Get an Google Drive service object using stored credential information.

    Args:
      - ``auth_info``: A dictionary of credential information, directly from credentials.to_json()

    Returns:
      - ``drive_service``: The Google Drive service object to do all the file operations

    """

    # j = json.loads()
    credentials = OAuth2Credentials.from_json(auth_info['credentials'])
    http = httplib2.Http()
    http = credentials.authorize(http)
    
    return build('drive', 'v2', http=http)

  @staticmethod
  def _get_gdfileid_from_id(auth_info, ID):
    drive_service = GoogleDriveAdapter._get_drive_service(auth_info)
    param = {'maxResults': 1, 'q': "title = '"+ ID + "'", 'fields': 'items/id'}
    file_list_info = drive_service.files().list(**param).execute()
    if len(file_list_info['items']) == 0:
      return None
    else:
      return file_list_info['items'][0]['id']

  @staticmethod
  def read(auth_info, ID):
    
    """Get the file whose name is ID.

    Args:
    - ``auth_info``: A dictionary of credential information, directly from credentials.to_json()
    - ``ID``: A hashed ID that points to a file

    Returns:
    - ``f``: The file specified by the path; you need to call f.read() to actually get the content
    - ``metadata``: The metadata of the file

    """

    drive_service = GoogleDriveAdapter._get_drive_service(auth_info)
    file_id = GoogleDriveAdapter._get_gdfileid_from_id(auth_info, ID)
    
    if file_id != None:
      file = drive_service.files().get(fileId=file_id).execute()
      download_url = file['downloadUrl']
      if download_url:
        resp, content = drive_service._http.request(download_url)
        if resp.status == 200:
          return content
    else:
      return None
    
  @staticmethod
  def update(auth_info, local_path, ID, overwrite):
    """Upload the file specified by the ID. Overwrite (update) if the file already exists.

    Args:
    - ``auth_info``: A dictionary of credential information, directly from credentials.to_json()
    - ``ID``: A hashed ID that points to a file

    Returns:
      - ``metadata``: The metadata of the file specified by the path 

    """
    
    drive_service = GoogleDriveAdapter._get_drive_service(auth_info)
    media_body = MediaFileUpload(ID, mimetype='binary/octet-stream', resumable=True)
    body = {
      'title': ID,
      'description': '',
      'mimeType': 'binary/octet-stream'
    }
      
    file_id = GoogleDriveAdapter._get_gdfileid_from_id(auth_info, ID)
    print file_id
    if file_id != None:
      # We are updating an existing file
      updated_file = drive_service.files().update(fileId=file_id, body=body, media_body=media_body).execute()
      return updated_file
    else:    
      # We are uploading a new file
      inserted_file = drive_service.files().insert(body=body, media_body=media_body).execute()
      return inserted_file
    
  @staticmethod
  def delete(auth_info, ID):
    """Delete the file specified by the ID

    Args:
      - ``auth_info``: A dictionary of credential information, directly from credentials.to_json()
      - ``ID``: A hashed ID that points to a file

    Returns:
      - ``metadata``: The metadata of the file deleted

    """
    
    drive_service = GoogleDriveAdapter._get_drive_service(auth_info)
    param = {'maxResults': 1, 'q': "title = '"+ ID + "'"}
    file_list_info = drive_service.files().list(**param).execute()
    file_id = file_list_info['items'][0]['id']
    drive_service.files().delete(fileId=file_id).execute()
    return file_list_info['items'][0]

  @staticmethod
  def metadata(auth_info, ID):
    """Delete the file specified by the ID

    Args:
      - ``auth_info``: A dictionary of credential information, directly from credentials.to_json()
      - ``ID``: A hashed ID that points to a file

    Returns:
      - ``metadata``: The metadata of the file deleted

    """

    drive_service = GoogleDriveAdapter._get_drive_service(auth_info)
    file_id = GoogleDriveAdapter._get_gdfileid_from_id(auth_info, ID)
    file_metadata = drive_service.files().get(fileId=file_id).execute()
    return file_metadata