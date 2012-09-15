import json
import pprint as pp

import os
import sys

sys.path.insert(0, '../')

from accordion.adapter.google_drive import GoogleDriveAdapter

auth_info = {'credentials': '{"_module": "oauth2client.client", "_class": "OAuth2Credentials", "access_token": "ya29.AHES6ZSdKGAYkDqGRZnN5IIEDcwOotSfOB8z8sOEAMcLj2_TJIAL", "token_uri": "https://accounts.google.com/o/oauth2/token", "invalid": false, "client_id": "949611273173.apps.googleusercontent.com", "id_token": null, "client_secret": "nDnBSUvbZm7fzWfpF2dC_uKq", "token_expiry": "2012-09-15T22:37:41Z", "refresh_token": "1/I5jrjJBmyHzzpw3RfSEh1Yd11jkU63wEi4uBd4mOQMI", "user_agent": null}'}

# json.loads(auth_info['credentials'])

ID = 'My document'
localFilePath = 'doc.txt'
# print GoogleDriveAdapter._get_gdfileid_from_id(auth_info, ID)

# content = GoogleDriveAdapter.read(auth_info, ID)
# print content

file = GoogleDriveAdapter.update(auth_info, localFilePath, localFilePath, True)

# metadata = GoogleDriveAdapter.delete(auth_info, localFilePath)
# print metadata

print GoogleDriveAdapter.metadata(auth_info, localFilePath)

# pprint.pprint(GoogleDriveAdapter.read(auth_info, "doc.txt"))