import requests 
import json
API_KEY = "AIzaSyAV1lJY8M6euS6HpW5xcHg_uvKGasdgTgA"
YT_CHANNEL = "@MrBeast"

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={YT_CHANNEL}&key={API_KEY}"
response = requests.get(url)
print(response)

data = response.json()
print(json.dumps(data, indent=4))