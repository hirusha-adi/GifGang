import requests
import random as rand


class Giphy:
    def __init__(self):
        self._api_key = None

    def random(self, limit: int = 5):
        giphy_url_list = []
        for _ in range(limit):
            r = requests.get(
                f"https://api.giphy.com/v1/gifs/random?api_key={self._api_key}")
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

        r = requests.get(
            f"https://api.giphy.com/v1/gifs/trending?api_key={self._api_key}&limit={limit}&offset={offset}")
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

    def search(self, query: str = "random", limit: int = 5, offset: int = None):

        if offset is None:
            offset = rand.randint(1, 4990 - limit)

        giphy_url_list = []

        r = requests.get(
            f'https://api.giphy.com/v1/gifs/search?api_key={self._api_key}&limit={limit}&offset={offset}&q={query}')
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


class Picsum:
    def __init__(self):
        pass

    def images(self, limit: int = 5, height: int = 200, width: int = 300):
        picsum_url_list = []
        for number in range(limit):
            picsum_url_list.append(
                f"https://picsum.photos/{height}/{width}?random={number}")
        return picsum_url_list


class Tenor:
    def __init__(self):
        self._api_key = None

    def random(
        self,
        limit: int = 5,
        locale: str = "en_US",
        ar_range: str = "all",
        contentfilter: str = "off"
    ):
        tenor_url_list = []

        r = requests.get(
            f'https://g.tenor.com/v1/random?key={self._api_key}&limit={limit}&locale={locale}&ar_range={ar_range}&contentfilter={contentfilter}')
        if 300 > r.status_code >= 200:
            data = r.json()
            for result in data["results"]:
                try:
                    tenor_url_list.append(
                        {
                            "title": str(result["content_description"]),
                            "url": result["media"][0]["gif"]["url"]
                        }

                    )
                except Exception as e:
                    print(e)

        return tenor_url_list
