import requests
import random as rand


class Eporner:
    def __init__(self):
        self.__random_query_lis = [
            "amateur",
            "anal",
            "asian",
            "blonde",
            "bigtits",
            "blowjob",
            "creampie",
            "cumshot",
            "double penetration",
            "ebony",
            "facials",
            "group",
            "hentai",
            "interracial",
            "latina",
            "japanese",
            "lingerie",
            "lesbian",
            "masturbation",
            "mature",
            "milf",
            "pov",
            "public",
            "redhead",
            "squirting",
            "wildcrazy",
            "teens",
            "cuckold",
            "oral",
            "cumshot facial",
            "pussy",
            "pussy licking",
            "deep throat",
            "cum on tits",
            "threesome",
            "bondage",
            "bdsm",
            "celebrity"
        ]

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
                        "src_url": result["url"]
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
                        "src_url": result["url"]
                    }
                )

        return eporner_list
