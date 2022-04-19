import os
import random

import requests
from utils import Config, FileNames, Important, Process, WebsiteData, log


def eporner(request, query):
    eporner_usage = False
    eporner_list = []
    if Important.eporner_usage:
        if WebsiteData.adult_search["api_usage"]["eporner"]["usage"]:
            eporner_usage = True
            _final_url = WebsiteData.adult_search["api_usage"]["eporner"]["api_url"]
            _final_url += f'?per_page={int(WebsiteData.adult_search["api_usage"]["eporner"]["limit"]) + 2}'
            _final_url += f'&thumbsize={WebsiteData.adult_search["api_usage"]["eporner"]["thumbsize"]}'
            _final_url += f'&order={WebsiteData.adult_search["api_usage"]["eporner"]["order"]}'
            _final_url += f'&format=json'
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

                log(f'EPORNER: Search Videos\n\tQuery: {query}\n\tLimit: {WebsiteData.adult_search["api_usage"]["eporner"]["limit"]}\n\tThumbnail Size: {WebsiteData.adult_search["api_usage"]["eporner"]["thumbsize"]}\n\tOrder: {WebsiteData.adult_search["api_usage"]["eporner"]["order"]}',
                    ipaddr=request.remote_addr)

            else:
                eporner_usage = False

    return {
        "eporner_usage": eporner_usage,
        "eporner_list": eporner_list
    }


def redtube(request, query):
    redtube_usage = False
    redtube_list = []
    if Important.redtube_usage:
        if WebsiteData.adult_search["api_usage"]["redtube"]["usage"]:
            redtube_usage = True
            _final_url = WebsiteData.adult_search["api_usage"]["redtube"]["api_url"]
            _final_url += f'?data={WebsiteData.adult_search["api_usage"]["redtube"]["data"]}'
            _final_url += f'&thumbsize={WebsiteData.adult_search["api_usage"]["redtube"]["thumbsize"]}'
            _final_url += f'&search=json'
            _final_url += f'&search={query}'

            r = requests.get(_final_url)
            if 300 > r.status_code >= 200:
                data = r.json()
                for result in data["videos"]:
                    redtube_list.append(
                        {
                            "title": result["video"]["title"],
                            "url": result["video"]["default_thumb"],
                            "src_url": result["video"]["url"]
                        }
                    )

                log(
                    f'REDTUBE: Search Videos\n\tQuery: {query}\n\tData: {WebsiteData.adult_search["api_usage"]["redtube"]["data"]}\n\tThumbnail Size: {WebsiteData.adult_search["api_usage"]["redtube"]["thumbsize"]}',
                    ipaddr=request.remote_addr)

            else:
                redtube_usage = False

    return {
        "redtube_usage": redtube_usage,
        "redtube_list": redtube_list
    }
