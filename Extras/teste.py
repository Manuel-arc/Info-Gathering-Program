import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


url = "https://google-search3.p.rapidapi.com/api/v1/search/q=Presidente+Portugal"

headers = {
    "X-User-Agent": "desktop",
    "X-Proxy-Location": "EU",
    "X-RapidAPI-Host": "google-search3.p.rapidapi.com",
    "X-RapidAPI-Key": "5b4e1e59aemsh8717f6da43b402ep167eabjsn0ce7d789fd96"
}

response = requests.request("GET", url, headers=headers)

jprint(response.json()['results'])