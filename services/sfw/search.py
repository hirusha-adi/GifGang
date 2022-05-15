import os
import random

import requests
from utils import Config, FileNames, Important, WebsiteData, log


def others(request, query):
    thecatapi_url_list = []
    thecatapi_usage = False
    dogceo_url_list = []
    dogceo_usage = False
    nekoslife_url_list = []
    nekoslife_usage = False

    if WebsiteData.search["custom_api_usage"]:
        query_lowered = str(query).lower()
        if any(word in query_lowered.split() for word in WebsiteData.search["custom_api_data_all_keywords_list"]):

            for one_custom in WebsiteData.search["custom_api_data"]:
                if any(word in query_lowered.split() for word in one_custom["keywords"]):

                    # The Cat API
                    if one_custom["api_info"]["name"] == "theCatAPI":
                        if Important.thecatapi_usage:  # global check
                            if one_custom["api_info"]["usage"]:  # local check
                                thecatapi_usage = True
                                r = requests.get(
                                    str(one_custom["api_info"]["api_url"])
                                    + "?limit=" +
                                    str(one_custom["api_info"]["limit"]) +
                                    "&size=" + str(one_custom["api_info"]["size"]) +
                                    "&mime_types=" +
                                    str(one_custom["api_info"]["mime_types"]) +
                                    "&order=" +
                                    str(one_custom["api_info"]["order"]) +
                                    "&has_breeds=" +
                                    str(one_custom["api_info"]["has_breeds"])
                                )
                                if 300 > r.status_code >= 200:
                                    data = r.json()
                                    for result in data:
                                        thecatapi_url_list.append(
                                            result["url"])
                                else:
                                    thecatapi_usage = False

                            log(f'TheCatAPI: Random Cat Images\n\tLimit: {one_custom["api_info"]["api_url"]}\n\tSize: {one_custom["api_info"]["size"]}\n\tMime Types: {one_custom["api_info"]["mime_types"]}\n\tOrder: {one_custom["api_info"]["order"]}\n\tHas Breeds: {one_custom["api_info"]["has_breeds"]}',
                                ipaddr=request.remote_addr)

                    # dogCEO API
                    if one_custom["api_info"]["name"] == "dogCEO":
                        if Important.dogceo_usage:
                            if one_custom["api_info"]["usage"]:
                                dogceo_usage = True
                                r = requests.get(
                                    str(one_custom["api_info"]["api_url"])
                                    + "/" +
                                    str(one_custom["api_info"]["limit"])
                                )
                                if 300 > r.status_code >= 200:
                                    data = r.json()
                                    for result in data["message"]:
                                        dogceo_url_list.append(result)
                                else:
                                    dogceo_usage = False

                            log(f'DogCEO: Random Dog Images\n\tLimit: {one_custom["api_info"]["limit"]}',
                                ipaddr=request.remote_addr)

                    # Anime Stuff - (nekoslife)
                    if one_custom["api_info"]["name"] == "nekoslife":
                        if Important.nekoslife_usage:
                            if one_custom["api_info"]["usage"]:
                                nekoslife_usage = True
                                full_url_list_nekos_life = []
                                _limit = int(
                                    one_custom["api_info"]["limit"]) - 1
                                while len(nekoslife_url_list) <= _limit:
                                    _final_url = one_custom["api_info"]["api_url_list"][random.randint(
                                        0, int(len(one_custom["api_info"]["api_url_list"]))-1)]
                                    full_url_list_nekos_life.append(_final_url)
                                    r1 = requests.get(_final_url)
                                    if 300 > r1.status_code >= 200:
                                        data = r1.json()
                                        try:
                                            nekoslife_url_list.append(
                                                data["url"])
                                        except KeyError:
                                            nekoslife_url_list.append(
                                                data["neko"])

                            log(f'Nekos.Life: Random Anime Images\n\tLimit: {_limit}\n\tURL List: {full_url_list_nekos_life}',
                                ipaddr=request.remote_addr)
    return {
        "thecatapi_url_list": thecatapi_url_list,
        "thecatapi_usage": thecatapi_usage,
        "dogceo_url_list": dogceo_url_list,
        "dogceo_usage": dogceo_usage,
        "nekoslife_url_list": nekoslife_url_list,
        "nekoslife_usage": nekoslife_usage
    }


def gihpy(request, query):
    giphy_url_list = []
    giphy_usage = False
    if Important.giphy_usage:
        if WebsiteData.search["api_usage"]["giphy"]["usage"]:
            giphy_usage = True
            offset = random.randint(
                1, 4990 - int(WebsiteData.search["api_usage"]["giphy"]["limit"]))
            r = requests.get(
                f'{WebsiteData.search["api_usage"]["giphy"]["api_url"]}?api_key={Important.giphy_api_key}&limit={WebsiteData.search["api_usage"]["giphy"]["limit"]}&offset={offset}&q={query}')
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

            log(
                f'GIPHY: Search GIF\n\tCount: {WebsiteData.search["api_usage"]["giphy"]["limit"]}\n\tOffset: {offset}', ipaddr=request.remote_addr)

        if len(giphy_url_list) == 0:
            giphy_usage = False
            log(f'GIPHY: GIF Url List was empty.\n\tDisabling `giphy_usage`',
                ipaddr=request.remote_addr)

    return {
        "giphy_url_list": giphy_url_list,
        "giphy_usage": giphy_usage
    }


def tenor(request, query):
    tenor_url_list = []
    tenor_usage = False
    if Important.tenor_usage:
        if WebsiteData.search["api_usage"]["tenor"]["usage"]:
            tenor_usage = True
            r = requests.get(
                f'{WebsiteData.search["api_usage"]["tenor"]["api_url"]}?key={Important.tenor_api_key}&limit={WebsiteData.search["api_usage"]["tenor"]["limit"]}&locale={WebsiteData.search["api_usage"]["tenor"]["locale"]}&ar_range={WebsiteData.search["api_usage"]["tenor"]["ar_range"]}&contentfilter={WebsiteData.search["api_usage"]["tenor"]["contentfilter"]}&q={query}')
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data["results"]:
                    tenor_url_list.append(
                        {
                            "title": str(result["content_description"]),
                            "url": result["media"][0]["gif"]["url"]
                        }
                    )
            else:
                tenor_usage = False

            log(
                f'TENOR: Search GIF\n\tCount: {WebsiteData.search["api_usage"]["tenor"]["limit"]}\n\tLocale: {WebsiteData.search["api_usage"]["tenor"]["locale"]}\n\tAR-Range: {WebsiteData.search["api_usage"]["tenor"]["ar_range"]}\n\tContent Filter: {WebsiteData.search["api_usage"]["tenor"]["contentfilter"]}', ipaddr=request.remote_addr)

    return {
        "tenor_url_list": tenor_url_list,
        "tenor_usage": tenor_usage
    }
