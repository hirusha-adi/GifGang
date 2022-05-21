import requests
import random as rand


class Eporner:
    def __init__(self):
        self.__random_query_lis = ["amateur", "anal", "asian", "blonde", "bigtits", "blowjob", "creampie", "cumshot", "double penetration", "ebony", "facials", "group", "hentai", "interracial", "latina", "japanese", "lingerie", "lesbian",
                                   "masturbation", "mature", "milf", "pov", "public", "redhead", "squirting", "wildcrazy", "teens", "cuckold", "oral", "cumshot facial", "pussy", "pussy licking", "deep throat", "cum on tits", "threesome", "bondage", "bdsm", "celebrity"]

    def random(self, limit: int = 5, thumbsize: str = "big", order: str = "top-weekly", format: str = "json"):
        eporner_list = []

        _final_url = "https://www.eporner.com/api/v2/video/search/"
        _final_url += f'?per_page={limit + 1}'
        _final_url += f'&thumbsize={thumbsize}'
        _final_url += f'&order={order}'
        _final_url += f'&format={format}'
        _final_url += f'&query={rand.choice(self.__random_query_lis)}'

        r = requests.get(_final_url)

        if 300 > r.status_code >= 200:
            data = r.json()
            for result in data["videos"]:
                eporner_list.append(
                    {
                        "title": result["title"],
                        "url": result["default_thumb"]["src"],
                        "src_url": result["url"],
                        "keywords": result["keywords"],
                        "views": result["views"],
                        "rate": result["rate"],
                        "uploaded_on": result["added"],
                        "length": result["length_min"],
                        "embed": result["embed"]
                    }
                )

        return eporner_list

    def search(self, query: str = "hardcore", limit: int = 5, thumbsize: str = "big", order: str = "top-weekly", format: str = "json"):
        eporner_list = []

        _final_url = "https://www.eporner.com/api/v2/video/search/"
        _final_url += f'?per_page={limit + 1}'
        _final_url += f'&thumbsize={thumbsize}'
        _final_url += f'&order={order}'
        _final_url += f'&format={format}'
        _final_url += f'&query={query}'

        r = requests.get(_final_url)

        if 300 > r.status_code >= 200:
            data = r.json()
            for result in data["videos"]:
                eporner_list.append(
                    {
                        "title": result["title"],
                        "url": result["default_thumb"]["src"],
                        "src_url": result["url"],
                        "keywords": result["keywords"],
                        "views": result["views"],
                        "rate": result["rate"],
                        "uploaded_on": result["added"],
                        "length": result["length_min"],
                        "embed": result["embed"]
                    }
                )

        return eporner_list


class RedTube:
    def __init__(self):
        self.__random_query_lis = ["amateur", "anal", "asian", "blonde", "bigtits", "blowjob", "creampie", "cumshot", "double penetration", "ebony", "facials", "group", "hentai", "interracial", "latina", "japanese", "lingerie", "lesbian",
                                   "masturbation", "mature", "milf", "pov", "public", "redhead", "squirting", "wildcrazy", "teens", "cuckold", "oral", "cumshot facial", "pussy", "pussy licking", "deep throat", "cum on tits", "threesome", "bondage", "bdsm", "celebrity"]

    def stars(self, page="1", output: str = "json"):
        stars_list = []

        _final_url = "https://api.redtube.com/"
        _final_url += f'?data=redtube.Stars.getStarDetailedList'
        _final_url += f'&output={output}'
        _final_url += f'&page={page}'

        r = requests.get(_final_url)
        if 300 > r.status_code >= 200:
            data = r.json()
            for star in data["stars"]:
                stars_list.append(
                    {
                        "title": star["star"],
                        "url": star["star_thumb"],
                        "src_url": star["star_url"]
                    }
                )

        return stars_list

    def random(self, size: str = "big", output: str = "json"):
        redtube_list = []

        _final_url = "https://api.redtube.com/"
        _final_url += f'?data=redtube.Videos.searchVideos'
        _final_url += f'&thumbsize={size}'
        _final_url += f'&output={output}'
        _final_url += f'&search={rand.choice(self.__random_query_lis)}'

        r = requests.get(_final_url)
        if 300 > r.status_code >= 200:
            data = r.json()
            for result in data["videos"]:
                redtube_list.append(
                    {
                        "title": result["video"]["title"],
                        "url": result["video"]["default_thumb"],
                        "src_url": result["video"]["url"],
                        "views": result["video"]["views"],
                        "rating": result["video"]["rating"],
                        "ratings": result["video"]["ratings"],
                        "embed_url": result["video"]["embed_url"],
                        "publish_date": result["video"]["publish_date"],
                        "duration": result["video"]["duration"]
                    }
                )

        return redtube_list

    def search(self, query: str = "hardcore", size: str = "big", output: str = "json"):
        redtube_list = []

        _final_url = "https://api.redtube.com/"
        _final_url += f'?data=redtube.Videos.searchVideos'
        _final_url += f'&thumbsize={size}'
        _final_url += f'&output={output}'
        _final_url += f'&search={query}'

        r = requests.get(_final_url)
        if 300 > r.status_code >= 200:
            data = r.json()
            for result in data["videos"]:
                redtube_list.append(
                    {
                        "title": result["video"]["title"],
                        "url": result["video"]["default_thumb"],
                        "src_url": result["video"]["url"],
                        "views": result["video"]["views"],
                        "rating": result["video"]["rating"],
                        "ratings": result["video"]["ratings"],
                        "embed_url": result["video"]["embed_url"],
                        "publish_date": result["video"]["publish_date"],
                        "duration": result["video"]["duration"]
                    }
                )

        return redtube_list
