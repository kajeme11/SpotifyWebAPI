import json

from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
# print(client_id, client_secrete)

# Use Spotify's for developers client id and client secret to get access token
def get_token():
    authorization = client_id + ":" + client_secret
    auth_bytes = authorization.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content_Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

# Use access token in Authorization
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

#Search for an artist
# def find_artist(token, artist):
#     url = "https://api.spotify.com/v1/search"
#     headers = get_auth_header(token)
#     q


access_token = get_token()
print(access_token)