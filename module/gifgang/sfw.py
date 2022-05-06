import requests
import random as rand

class Giphy:
    def __init__(self):
        self._api_key = None

    def random(self, limit: int=5):
        giphy_url_list = []
        for _ in range(limit):
            r = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={self._api_key}")
            if 300 > r.status_code >= 200:
                try:
                    data = r.json()
                    giphy_url_list.append(
                        {
                            "url": data["data"]["images"]["original"]["url"],
                            "title": data["data"]["title"]
                        }
                    )
                except Exception as e:
                    print(e)
        return giphy_url_list

    def trending(self, limit: int = 5, offset: int = None):
        if offset is None:
            offset = rand.randint(1, 4990 - limit)

        giphy_url_list = []

        r = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={self._api_key}&limit={limit}&offset={offset}")
        if 300 > r.status_code >= 200:
            try:
                data = r.json()
                for item in data["data"]:
                    giphy_url_list.append(
                        {
                            "url": item["images"]["original"]["url"],
                            "title": item["title"]
                        }
                    )
            except Exception as e:
                print(e)

        return giphy_url_list


    def search(self):
        pass