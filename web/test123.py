from utils import Important as I
import requests

r = requests.get(
    f"https://g.tenor.com/v1/trending?key={I.tenor_api_key}&limit=1").json()

print(r["results"][0]["title"])
print(r["results"][0]["content_description"])
print(r["results"][0]["media"][0]["gif"]["url"])
