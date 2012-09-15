import json
import pprint

from google_drive import GoogleDriveAdapter

auth_info = {'credentials': '{"_module": "oauth2client.client", "_class": "OAuth2Credentials", "access_token": "ya29.AHES6ZR3ueKC3lUxwN6hudE2Vjebo8qG7nhAMn6rnP9E2Lh-z1MhtYE", "token_uri": "https://accounts.google.com/o/oauth2/token", "invalid": false, "client_id": "264243535898-6ariku6s0jbmq7n5e941kl9nr331o72d.apps.googleusercontent.com", "id_token": null, "client_secret": "rkBdfBaMNCZ6QpJhdCJpaFjT", "token_expiry": "2012-09-15T19:33:46Z", "refresh_token": "1/ebT_w5MbESqAuCQILiqTKj6X8fOyR_4RWEFg9qokzwE", "user_agent": null}'}

# json.loads(auth_info['credentials'])

pprint.pprint(GoogleDriveAdapter.read(auth_info, "doc.txt"))