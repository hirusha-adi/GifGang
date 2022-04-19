import os
import random

import requests
from utils import Config, FileNames, Important, Process, WebsiteData, log


def localserverml(request):
    hentai_localserverml_api_usage = False
    hentai_localserverml_api_list = []
    hentai_localserverml_api_list_request_list = []
    if Important.localserverml_usage:
        if WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["usage"]:
            hentai_localserverml_api_usage = True
            for _ in range(int(WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["limit"])):
                _final_url = WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["api_url"]
                _random_choice = random.choice(
                    WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["localserverml_enpoints"])
                _final_url += f'{_random_choice}'

                hentai_localserverml_api_list_request_list.append(
                    _final_url)

                try:
                    r = requests.get(_final_url)
                    if 300 > r.status_code >= 200:
                        url = r.text
                        if url.startswith('"') or url.endswith('"'):
                            hentai_localserverml_api_list.append(url[1:-2])
                        else:
                            hentai_localserverml_api_list.append(url)
                except:
                    pass

            log(
                f'LocalServer.ml API\n\tCount: {WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["limit"]}\n\tAll URL List: {hentai_localserverml_api_list_request_list}', ipaddr=request.remote_addr)

    return {
        "hentai_localserverml_api_usage": hentai_localserverml_api_usage,
        "hentai_localserverml_api_list": hentai_localserverml_api_list,
        "hentai_localserverml_api_list_request_list": hentai_localserverml_api_list_request_list
    }


def nekos_life(request):
    hentai_nekoslife_usage = False
    hentai_nekoslife_list = []
    hentai_nekoslife_list_request_list = []

    if Important.nekoslife_usage:
        if WebsiteData.adult_hentai["api_usage"]["nekoslife"]["usage"]:
            hentai_nekoslife_usage = True
            for _ in range(int(WebsiteData.adult_hentai["api_usage"]["nekoslife"]["limit"])):
                _final_url = WebsiteData.adult_hentai["api_usage"]["nekoslife"]["api_url"]
                _random_choice = random.choice(
                    WebsiteData.adult_hentai["api_usage"]["nekoslife"]["nekoslife_endpoints"])
                _final_url += f'{_random_choice}'

                hentai_nekoslife_list_request_list.append(_final_url)

                try:
                    r = requests.get(_final_url)
                    if 300 > r.status_code >= 200:
                        data = r.json()
                        try:
                            hentai_nekoslife_list.append(data["url"])
                        except KeyError:
                            hentai_nekoslife_list.append(data["neko"])
                except:
                    pass

            log(
                f'Nekos.Life API:\n\tCount: {WebsiteData.adult_hentai["api_usage"]["nekoslife"]["limit"]}\n\tAll Url List: {hentai_nekoslife_list_request_list}', ipaddr=request.remote_addr)

    return {
        "hentai_nekoslife_usage": hentai_nekoslife_usage,
        "hentai_nekoslife_list": hentai_nekoslife_list,
        "hentai_nekoslife_list_request_list": hentai_nekoslife_list_request_list
    }
