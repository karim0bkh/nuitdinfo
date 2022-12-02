# How to upload a video under 200 MiB using the api.video API

import requests
from nuit2 import generate_video
# Set up variables for endpoints
auth_url = "https://ws.api.video/auth/api-key"
create_url = "https://ws.api.video/videos"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "apiKey": "vd3yPED3CJSV5JSXDirevU9fJgHgWtDll2V9WQPLtQ9"
}

response = requests.request("POST", auth_url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")

auth_string = "Bearer " + token


# Set up headers for authentication
headers_bearer = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": auth_string
}

# Create a video container
captcha=generate_video()

payload2 = {
    "title": "captcha done by gdsc poly",
    "captcha": captcha[0]+"-"+captcha[1]+"-"+captcha[2]+"-"+captcha[3]+"-"+captcha[4]
}

response = requests.request("POST", create_url, json=payload2, headers=headers_bearer)
response = response.json()
videoId = response["videoId"]

# Create endpoint to upload video to
upload_url = create_url+"/" + videoId + "/source"

# Create upload video headers 
headers_upload = {
    "Accept": "application/vnd.api.video+json",
    "Authorization": auth_string
}
file = {"file": open(r"C:\Users\ASUS\Desktop\py\vids\\"+captcha[4], "rb")}
response = requests.request("POST", upload_url, files=file, headers=headers_upload)
json_response = response.json()
print(json_response)
