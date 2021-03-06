import requests
import random as rand


class Giphy:
    def __init__(self, api_key):
        self._api_key = api_key

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
    def __init__(self, api_key):
        self._api_key = api_key

    def random(self, limit: int = 5, locale: str = "en_US", ar_range: str = "all", contentfilter: str = "off"):
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

    def search(self, query: str = "random", limit: int = 5, locale: str = "en_US", ar_range: str = "all", contentfilter: str = "off"):
        tenor_url_list = []

        r = requests.get(
            f'https://g.tenor.com/v1/search?key={self._api_key}&limit={limit}&locale={locale}&ar_range={ar_range}&contentfilter={contentfilter}&q={query}')
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


class Cats:
    def __init__(self):
        pass

    def theCatAPI(limit: int = 5, size: str = "med", mime_types: str = "jpg,gif,png", order: str = "RANDOM", has_breeds=0):
        thecatapi_url_list = []
        r = requests.get(
            f'https://api.thecatapi.com/v1/images/search?limit={limit}&size={size}&mime_types={mime_types}&order={order}&has_breeds={has_breeds}'
        )
        if 300 > r.status_code >= 200:
            data = r.json()
            for result in data:
                thecatapi_url_list.append(result["url"])
        return thecatapi_url_list

    class CatsAsAService:
        def image(text=None, size="med", color=None, type=None, filter=None, width=None, height=None):
            final_url_list = []

            base_url = "https://cataas.com/"

            if text is None:
                base_url += "/cat"
            else:
                base_url += f"/cat/says/{text}"

            if not(size is None):
                base_url += f"?size={size}"
            else:
                base_url += f"?size=med"

            if not(color is None):
                base_url += f"&color={color}"

            if not(type is None):
                base_url += f"&type={type}"

            if not(filter is None):
                base_url += f"&filter={filter}"

            if not(width is None):
                base_url += f"&color={width}"

            if not(height is None):
                base_url += f"&height={height}"

            r = requests.get(base_url)

            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data:
                    final_url_list.append(result["url"])

            return final_url_list

        def gif(text=None, size="", color="", type="", filter="", width=None, height=None):
            final_url_list = []

            base_url = "https://cataas.com/"

            if text is None:
                base_url += "/cat/gif"
            else:
                base_url += f"/cat/gif/says/{text}"

            if not(size is None):
                base_url += f"?size={size}"
            else:
                base_url += f"?size=med"

            if not(color is None):
                base_url += f"&color={color}"

            if not(type is None):
                base_url += f"&type={type}"

            if not(filter is None):
                base_url += f"&filter={filter}"

            if not(width is None):
                base_url += f"&color={width}"

            if not(height is None):
                base_url += f"&height={height}"

            r = requests.get(base_url)

            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data:
                    final_url_list.append(result["url"])

            return final_url_list


class Dogs:
    def __init__(self):
        pass

    def images(self, limit: int = 5):
        final_url_list = []

        r = requests.get(f"https://dog.ceo/api/breeds/image/random/{limit}")
        if 300 > r.status_code >= 200:
            data = r.json()
            for result in data["message"]:
                final_url_list.append(result)

        return final_url_list


class NekosLife:
    def anime(category: str = "kiss"):
        final_url_list = []

        category = category.lower()
        if category in ("hug", "kiss", "lizard", "neko", "pat"):
            req_url = f"https://nekos.life/api/{category}"
        elif category in ("slap", "cuddle", "avatar", "poke", "feed"):
            req_url = f"https://nekos.life/api/v2/img/{category}"
        else:
            req_url = f"https://nekos.life/api/hug"

        r1 = requests.get(req_url)
        if 300 > r1.status_code >= 200:
            data = r1.json()
            try:
                final_url_list.append(data["url"])
            except KeyError:
                final_url_list.append(data["neko"])

        return final_url_list
