import os
import random

import requests
from utils import Config, FileNames, Important, WebsiteData, log


def getAll(request, page):
    stars_usage = False
    stars_list = []
    if Important.redtube_usage:
        if WebsiteData.adult_stars["api_usage"]["usage"]:
            stars_usage = True

            # API Request for pornstars list
            # https://api.redtube.com/
            # ?data=redtube.Stars.getStarDetailedList   | ["redtube.Stars.getStarList", "redtube.Stars.getStarDetailedList"]
            # &output=json                              | ["json", "xml"]
            # &page=5                                   | [1-1046]

            _final_url = str(WebsiteData.adult_stars["api_usage"]["api_url"])
            _final_url += f'?data={WebsiteData.adult_stars["api_usage"]["data"]}'
            _final_url += f'&output=json'
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
            else:
                stars_usage = False

            log(f'REDTUBE: Pornstar List\n\tData: {WebsiteData.adult_stars["api_usage"]["data"]}\n\tPage Number: {page}',
                ipaddr=request.remote_addr)

            current_page = int(page)
            first_page = 1
            last_page = 1046

            if current_page == 1:
                previous_page_1 = 1
                previous_page_2 = 1
                previous_page_3 = 1
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 2:
                previous_page_1 = 1
                previous_page_2 = 1
                previous_page_3 = 1
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 3:
                previous_page_1 = 2
                previous_page_2 = 1
                previous_page_3 = 1
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 4:
                previous_page_1 = 3
                previous_page_2 = 2
                previous_page_3 = 1
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 5:
                previous_page_1 = 4
                previous_page_2 = 3
                previous_page_3 = 2
                previous_page_4 = 1
                show_dots_left = False
            elif current_page == 6:
                previous_page_1 = 5
                previous_page_2 = 4
                previous_page_3 = 3
                previous_page_4 = 2
                show_dots_left = True
            else:
                previous_page_1 = current_page - 1
                previous_page_2 = previous_page_1 - 1
                previous_page_3 = previous_page_2 - 1
                previous_page_4 = previous_page_3 - 1
                show_dots_left = True

            if current_page == (last_page):
                next_page_1 = last_page
                next_page_2 = last_page
                next_page_3 = last_page
                next_page_4 = last_page
                show_dots_right = False
            elif current_page == (last_page-1):
                next_page_1 = last_page + 1
                next_page_2 = last_page
                next_page_3 = last_page
                next_page_4 = last_page
                show_dots_right = False
            elif current_page == (last_page-2):
                next_page_1 = last_page + 1
                next_page_2 = last_page + 2
                next_page_3 = last_page
                next_page_4 = last_page
                show_dots_right = False
            elif current_page == (last_page-3):
                next_page_1 = last_page + 1
                next_page_2 = last_page + 2
                next_page_3 = last_page + 3
                next_page_4 = last_page
                show_dots_right = False
            elif current_page == (last_page-4):
                next_page_1 = last_page + 1
                next_page_2 = last_page + 2
                next_page_3 = last_page + 3
                next_page_4 = last_page + 4
                show_dots_right = False
            else:
                next_page_1 = current_page + 1
                next_page_2 = next_page_1 + 1
                next_page_3 = next_page_2 + 1
                next_page_4 = next_page_3 + 1
                show_dots_right = True

            log(f'Processed all Page Numbers List', ipaddr=request.remote_addr)

    return {
        "stars_usage": stars_usage,
        "stars_list": stars_list,
        "current_page": current_page,
        "first_page": first_page,
        "last_page": last_page,
        "previous_page_1": previous_page_1,
        "previous_page_2": previous_page_2,
        "previous_page_3": previous_page_3,
        "previous_page_4": previous_page_4,
        "next_page_1": next_page_1,
        "next_page_2": next_page_2,
        "next_page_3": next_page_3,
        "next_page_4": next_page_4,
        "show_dots_right": show_dots_right,
        "show_dots_left": show_dots_left
    }
