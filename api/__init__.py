from dotenv import load_dotenv
import os
import base64
from requests import post, get
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
def find_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    #get first artist by artist name
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        return None
    else:
        return json_result[0]


access_token = get_token()
# print(access_token)
artist = find_artist(access_token, "ACDC")
print(artist)
print(artist["name"])


