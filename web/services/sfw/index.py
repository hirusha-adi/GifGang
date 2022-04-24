import os
import random

import requests
from utils import Config, FileNames, Important, WebsiteData, log


def giphy(request):
    giphy_url_list = []
    giphy_usage = False
    if Important.giphy_usage:
        if WebsiteData.index["api_usage"]["giphy"]["usage"]:
            giphy_usage = True

            # Random
            if WebsiteData.index["api_usage"]["giphy"]["random"]:
                for _ in range(int(WebsiteData.index["api_usage"]["giphy"]["random_limit"])):
                    r = requests.get(
                        f'{WebsiteData.index["api_usage"]["giphy"]["random_api_url"]}?api_key={Important.giphy_api_key}')
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

                log(
                    f'GIPHY: Random One by One: True - {int(WebsiteData.index["api_usage"]["giphy"]["random_limit"])}',
                    ipaddr=request.remote_addr)

            # Trending
            if WebsiteData.index["api_usage"]["giphy"]["trending"]:
                offset = random.randint(
                    1, 4990 - int(WebsiteData.index["api_usage"]["giphy"]["trending_limit"]))
                r = requests.get(
                    f'{WebsiteData.index["api_usage"]["giphy"]["trending_api_url"]}?api_key={Important.giphy_api_key}&limit={WebsiteData.index["api_usage"]["giphy"]["trending_limit"]}&offset={offset}')
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
            f'GIPHY: Trending List: True\n\tOffset: {offset}\n\tCount: {WebsiteData.index["api_usage"]["giphy"]["trending_limit"]}\n\tActual Length: {len(giphy_url_list)}',
            ipaddr=request.remote_addr)

    return {
        "giphy_url_list": giphy_url_list,
        "giphy_usage": giphy_usage,
        "offset": offset
    }


def picsum(request):
    picsum_url_list = []
    picsum_usage = False
    if Important.picsum_usage:
        if WebsiteData.index["api_usage"]["picsum"]["usage"]:
            picsum_usage = True
            for number in range(int(WebsiteData.index["api_usage"]["picsum"]["limit"])):
                picsum_url_list.append(
                    str(WebsiteData.index["api_usage"]["picsum"]["api_url"]) + str(number))

        log(
            f'PICSUM: Random Images\n\tCount: {int(WebsiteData.index["api_usage"]["picsum"]["limit"])}',
            ipaddr=request.remote_addr)

    return {
        "picsum_url_list": picsum_url_list,
        "picsum_usage": picsum_usage
    }


def tenor(request):
    tenor_url_list = []
    tenor_usage = False
    if Important.tenor_usage:
        if WebsiteData.index["api_usage"]["tenor"]["usage"]:
            tenor_usage = True
            r = requests.get(
                f'{WebsiteData.index["api_usage"]["tenor"]["api_url"]}?key={Important.tenor_api_key}&limit={WebsiteData.index["api_usage"]["tenor"]["limit"]}&locale={WebsiteData.index["api_usage"]["tenor"]["locale"]}&ar_range={WebsiteData.index["api_usage"]["tenor"]["ar_range"]}&contentfilter={WebsiteData.index["api_usage"]["tenor"]["contentfilter"]}')
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
            f'TENOR: Random Images\n\tCount: {WebsiteData.index["api_usage"]["tenor"]["limit"]}\n\tLocale: {WebsiteData.index["api_usage"]["tenor"]["locale"]}\n\tAR-Range: {WebsiteData.index["api_usage"]["tenor"]["ar_range"]}\n\tContent Filter: {WebsiteData.index["api_usage"]["tenor"]["contentfilter"]}',
            ipaddr=request.remote_addr)

    return {
        "tenor_url_list": tenor_url_list,
        "tenor_usage": tenor_usage
    }


def cats(request):
    thecatapi_url_list = []
    thecatapi_usage = False
    if Important.thecatapi_usage:
        if WebsiteData.index["api_usage"]["theCatAPI"]["usage"]:
            thecatapi_usage = True
            r = requests.get(
                str(WebsiteData.index["api_usage"]["theCatAPI"]["api_url"])
                + "?limit=" +
                str(WebsiteData.index["api_usage"]["theCatAPI"]["limit"]) +
                "&size=" + str(WebsiteData.index["api_usage"]["theCatAPI"]["size"]) +
                "&mime_types=" +
                str(WebsiteData.index["api_usage"]["theCatAPI"]["mime_types"]) +
                "&order=" +
                str(WebsiteData.index["api_usage"]["theCatAPI"]["order"]) +
                "&has_breeds=" +
                str(WebsiteData.index["api_usage"]
                    ["theCatAPI"]["has_breeds"])
            )
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data:
                    thecatapi_url_list.append(result["url"])
            else:
                thecatapi_usage = False

        log(
            f'TheCatAPI: Random Images\n\tCount: {WebsiteData.index["api_usage"]["theCatAPI"]["limit"]}\n\tSize: {WebsiteData.index["api_usage"]["theCatAPI"]["size"]}\n\tMime Types: {WebsiteData.index["api_usage"]["theCatAPI"]["mime_types"]}\n\tOrder: {WebsiteData.index["api_usage"]["theCatAPI"]["order"]}\n\tHas Breeds: {WebsiteData.index["api_usage"]["theCatAPI"]["has_breeds"]}',
            ipaddr=request.remote_addr)

    return {
        "thecatapi_url_list": thecatapi_url_list,
        "thecatapi_usage": thecatapi_usage
    }


def dogs(request):
    dogceo_url_list = []
    dogceo_usage = False
    if Important.dogceo_usage:
        if WebsiteData.index["api_usage"]["dogCEO"]["usage"]:
            dogceo_usage = True
            r = requests.get(
                str(WebsiteData.index["api_usage"]["dogCEO"]["api_url"])
                + "/" +
                str(WebsiteData.index["api_usage"]["dogCEO"]["limit"])
            )
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data["message"]:
                    dogceo_url_list.append(result)
            else:
                dogceo_usage = False

        log(
            f'DogCEO: Random Images\n\tCount: {WebsiteData.index["api_usage"]["dogCEO"]["limit"]}',
            ipaddr=request.remote_addr)

    return {
        "dogceo_url_list": dogceo_url_list,
        "dogceo_usage": dogceo_usage
    }


def nekos_life(request):
    nekoslife_url_list = []
    nekoslife_usage = False
    selected_url_list = []
    if Important.nekoslife_usage:
        if WebsiteData.index["api_usage"]["nekoslife"]["usage"]:
            nekoslife_usage = True
            _limit = int(
                WebsiteData.index["api_usage"]["nekoslife"]["limit"]) - 1
            while len(nekoslife_url_list) <= _limit:
                _final_url = WebsiteData.index["api_usage"]["nekoslife"]["api_url_list"][random.randint(
                    0, int(len(WebsiteData.index["api_usage"]["nekoslife"]["api_url_list"]))-1)]
                selected_url_list.append(_final_url)
                r1 = requests.get(_final_url)
                if 300 > r1.status_code >= 200:
                    data = r1.json()
                    try:
                        nekoslife_url_list.append(data["url"])
                    except KeyError:
                        nekoslife_url_list.append(data["neko"])

        log(
            f'Nekos.Life: Random Images\n\tLimit:{WebsiteData.index["api_usage"]["nekoslife"]["limit"]}\n\tSelected URL List: {selected_url_list}',
            ipaddr=request.remote_addr)

    return {
        "nekoslife_url_list": nekoslife_url_list,
        "nekoslife_usage": nekoslife_usage,
        "selected_url_list": selected_url_list
    }
