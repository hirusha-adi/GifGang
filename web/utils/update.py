import json
from utils import Important, WebsiteData, FileNames, Settings


class Update:
    def Important(
        giphy_usage,
        giphy_api_url_base,
        giphy_api_key,
        picsum_usage,
        picsum_api_url_base,
        tenor_usage,
        tenor_api_key,
        thecatapi_usage,
        dogceo_usage,
        nekoslife_usage,
        eporner_usage,
        redtube_usage,
        localserverml_usage
    ):
        Important.giphy_usage = True if str(giphy_usage) == "2" else False
        Important.giphy_api_url_base = str(giphy_api_url_base)
        Important.giphy_api_key = str(giphy_api_key)
        Important.picsum_usage = True if str(picsum_usage) == "2" else False
        Important.picsum_api_url_base = picsum_api_url_base
        Important.tenor_usage = True if str(tenor_usage) == "2" else False
        Important.tenor_api_key = str(tenor_api_key)
        Important.thecatapi_usage = True if str(
            thecatapi_usage) == "2" else False
        Important.dogceo_usage = True if str(dogceo_usage) == "2" else False
        Important.nekoslife_usage = True if str(
            nekoslife_usage) == "2" else False
        Important.eporner_usage = True if str(eporner_usage) == "2" else False
        Important.redtube_usage = True if str(redtube_usage) == "2" else False
        Important.localserverml_usage = True if str(
            localserverml_usage) == "2" else False

        Important._data = {
            "giphy": {
                "usage": Important.giphy_usage,
                "api_url_base": Important.giphy_api_url_base,
                "api_key": Important.giphy_api_key,
            },
            "picsum": {
                "usage": Important.picsum_usage,
                "api_url_base": Important.picsum_api_url_base
            },
            "tenor": {
                "usage": Important.tenor_usage,
                "api_key": Important.tenor_api_key
            },
            "theCatAPI": {
                "usage": Important.thecatapi_usage
            },
            "dogCEO": {
                "usage": Important.dogceo_usage
            },
            "nekoslife": {
                "usage": Important.nekoslife_usage
            },
            "eporner": {
                "usage": Important.eporner_usage
            },
            "redtube": {
                "usage": Important.redtube_usage
            },
            "localserverml": {
                "usage": Important.localserverml_usage
            }
        }

        with open(FileNames.important_info_file, "w", encoding="utf-8") as _file:
            json.dump(Important._data, _file, indent=4)

    def SettingsAdmin(
        username, password, token, profile_pic, targets_today, targets_all
    ):
        Settings.Admin.username = username
        Settings.Admin.password = password
        Settings.Admin.token = token
        Settings.Admin.profile_pic = profile_pic

        try:
            Settings.Admin.targets_today = int(targets_today)
        except:
            Settings.Admin.targets_today = str(targets_today)

        try:
            Settings.Admin.targets_all = int(targets_all)
        except:
            Settings.Admin.targets_all = str(targets_all)

        Settings.Admin._admin_data = {
            "username": Settings.Admin.username,
            "password": Settings.Admin.password,
            "token": Settings.Admin.token,
            "profile_pic": Settings.Admin.profile_pic,
            "targets": {
                "today": Settings.Admin.targets_today,
                "all": Settings.Admin.targets_all
            }
        }

        with open(FileNames.admin_settings_file, "w", encoding="utf-8") as _file:
            json.dump(Settings.Admin._admin_data, _file, indent=4)

    def Index(
        IndexMainTitle,
        IndexGiphyUsage,
        IndexGiphyRandomUsage,
        IndexGiphyRandomLimit,
        IndexGiphyRandomAPIurl,
        IndexGiphyTrendingUsage,
        IndexGiphyTrendingLimit,
        IndexGiphyTendingAPIurl,
        IndexPicsumUsage,
        IndexPicsumLimit,
        IndexPicsumApiURL,
        IndexTenorUsage,
        IndexTenorLimit,
        IndexTenorLocale,
        IndexTenorArRange,
        IndexTenorContentFilter,
        IndexTenorApiURL,
        IndexTheCatAPIUsage,
        IndexTheCatAPILimit,
        IndexTheCatAPISize,
        IndexTheCatAPIMineTypes,
        IndexTheCatAPIOrder,
        IndexTheCatAPIHasBreeds,
        IndexTheCatAPIAPIUrl,
        IndexDogCEOUsage,
        IndexDogCEOLimit,
        IndexDogCEOApiURL,
        IndexNekosLifeUsage,
        IndexNekosLifeLimit,
        IndexNekosLifeURLlist
    ):
        WebsiteData.index["title"] = str(IndexMainTitle)

        WebsiteData.index["api_usage"]["giphy"]["usage"] = True if str(
            IndexGiphyUsage) == "2" else False
        WebsiteData.index["api_usage"]["giphy"]["random"] = True if str(
            IndexGiphyRandomUsage) == "2" else False
        try:
            WebsiteData.index["api_usage"]["giphy"]["random_limit"] = int(
                IndexGiphyRandomLimit)
        except:
            WebsiteData.index["api_usage"]["giphy"]["random_limit"] = str(
                IndexGiphyRandomLimit)
        WebsiteData.index["api_usage"]["giphy"]["random_api_url"] = str(
            IndexGiphyRandomAPIurl)
        WebsiteData.index["api_usage"]["giphy"]["trending"] = True if str(
            IndexGiphyTrendingUsage) == "2" else False
        try:
            WebsiteData.index["api_usage"]["giphy"]["trending_limit"] = int(
                IndexGiphyTrendingLimit)
        except:
            WebsiteData.index["api_usage"]["giphy"]["trending_limit"] = str(
                IndexGiphyTrendingLimit)
        WebsiteData.index["api_usage"]["giphy"]["trending_api_url"] = str(
            IndexGiphyTendingAPIurl)

        WebsiteData.index["api_usage"]["picsum"]["usage"] = True if str(
            IndexPicsumUsage) == "2" else False
        try:
            WebsiteData.index["api_usage"]["picsum"]["limit"] = int(
                IndexPicsumLimit)
        except:
            WebsiteData.index["api_usage"]["picsum"]["limit"] = str(
                IndexPicsumLimit)
        WebsiteData.index["api_usage"]["picsum"]["api_url"] = str(
            IndexPicsumApiURL)

        WebsiteData.index["api_usage"]["tenor"]["usage"] = True if str(
            IndexTenorUsage) == "2" else False

        try:
            WebsiteData.index["api_usage"]["tenor"]["limit"] = int(
                IndexTenorLimit)
        except:
            WebsiteData.index["api_usage"]["tenor"]["limit"] = str(
                IndexTenorLimit)

        WebsiteData.index["api_usage"]["tenor"]["locale"] = str(
            IndexTenorLocale)
        WebsiteData.index["api_usage"]["tenor"]["ar_range"] = str(
            IndexTenorArRange)
        WebsiteData.index["api_usage"]["tenor"]["contentfilter"] = str(
            IndexTenorContentFilter)
        WebsiteData.index["api_usage"]["tenor"]["api_url"] = str(
            IndexTenorApiURL)

        WebsiteData.index["api_usage"]["theCatAPI"]["usage"] = True if str(
            IndexTheCatAPIUsage) == "2" else False
        WebsiteData.index["api_usage"]["theCatAPI"]["size"] = str(
            IndexTheCatAPISize)
        WebsiteData.index["api_usage"]["theCatAPI"]["mime_types"] = str(
            IndexTheCatAPIMineTypes)
        WebsiteData.index["api_usage"]["theCatAPI"]["order"] = str(
            IndexTheCatAPIOrder)
        try:
            WebsiteData.index["api_usage"]["theCatAPI"]["limit"] = int(
                IndexTheCatAPILimit)
        except:
            WebsiteData.index["api_usage"]["theCatAPI"]["limit"] = str(
                IndexTheCatAPILimit)
        try:
            WebsiteData.index["api_usage"]["theCatAPI"]["has_breeds"] = int(
                IndexTheCatAPIHasBreeds)
        except:
            WebsiteData.index["api_usage"]["theCatAPI"]["has_breeds"] = str(
                IndexTheCatAPIHasBreeds)
        WebsiteData.index["api_usage"]["theCatAPI"]["api_url"] = str(
            IndexTheCatAPIAPIUrl)

        WebsiteData.index["api_usage"]["dogCEO"]["usage"] = True if str(
            IndexDogCEOUsage) == "2" else False
        try:
            WebsiteData.index["api_usage"]["dogCEO"]["limit"] = int(
                IndexDogCEOLimit)
        except:
            WebsiteData.index["api_usage"]["dogCEO"]["limit"] = str(
                IndexDogCEOLimit)
        WebsiteData.index["api_usage"]["dogCEO"]["api_url"] = str(
            IndexDogCEOApiURL)

        WebsiteData.index["api_usage"]["nekoslife"]["usage"] = True if str(
            IndexNekosLifeUsage) == "2" else False
        try:
            WebsiteData.index["api_usage"]["nekoslife"]["limit"] = int(
                IndexNekosLifeLimit)
        except:
            WebsiteData.index["api_usage"]["nekoslife"]["limit"] = str(
                IndexNekosLifeLimit)

        x = str(IndexNekosLifeURLlist)

        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])
        WebsiteData.index["api_usage"]["nekoslife"]["api_url_list"] = y

        WebsiteData._data["index"] = WebsiteData.index

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

    def Search(
        SearchMainTitle,
        SearchGiphyUsage,
        SearchGiphyLimit,
        SearchGiphyOffset,
        SearchGiphyApiURL,
        SearchTenorUsage,
        SearchTenorLimit,
        SearchTenorLocale,
        SearchTenorArRange,
        SearchTenorContentFilter,
        SearchTenorApiURL,
        SearchSmartModeUsage,
        SearchSmartModeKeywordsList,
        SearchTheCatAPIUsage,
        SearchTheCatAPIName,
        SearchTheCatAPIKeywordList,
        SearchTheCatAPISize,
        SearchTheCatAPILimit,
        SearchTheCatAPIMineTypes,
        SearchTheCatAPIOrder,
        SearchTheCatAPIHasBreeds,
        SearchTheCatAPIApiURL,
        SearchDogCEOUsage,
        SearchDogCEOName,
        SearchDogCEOLimit,
        SearchDogCEOApiURL,
        SearchDogCEOKeywordsList,
        SearchNekosLifeUsage,
        SearchNekosLifeName,
        SearchNekosLifeKeywordList,
        SearchNekosLifeLimit,
        SearchNekosLifeURLlist
    ):
        WebsiteData.search["title"] = SearchMainTitle

        WebsiteData.search["api_usage"]["giphy"]["usage"] = True if str(
            SearchGiphyUsage) == "2" else False
        try:
            WebsiteData.search["api_usage"]["giphy"]["limit"] = int(
                SearchGiphyLimit)
        except:
            WebsiteData.search["api_usage"]["giphy"]["limit"] = str(
                SearchGiphyLimit)
        try:
            WebsiteData.search["api_usage"]["giphy"]["offset"] = int(
                SearchGiphyOffset)
        except:
            WebsiteData.search["api_usage"]["giphy"]["offset"] = str(
                SearchGiphyOffset)
        WebsiteData.search["api_usage"]["giphy"]["api_url"] = str(
            SearchGiphyApiURL)

        WebsiteData.search["api_usage"]["tenor"]["usage"] = True if str(
            SearchTenorUsage) == "2" else False
        try:
            WebsiteData.search["api_usage"]["tenor"]["limit"] = int(
                SearchTenorLimit)
        except:
            WebsiteData.search["api_usage"]["tenor"]["limit"] = str(
                SearchTenorLimit)
        WebsiteData.search["api_usage"]["tenor"]["locale"] = str(
            SearchTenorLocale)
        WebsiteData.search["api_usage"]["tenor"]["ar_range"] = str(
            SearchTenorArRange)
        WebsiteData.search["api_usage"]["tenor"]["contentfilter"] = str(
            SearchTenorContentFilter)
        WebsiteData.search["api_usage"]["tenor"]["api_url"] = str(
            SearchTenorApiURL)

        WebsiteData.search["custom_api_usage"] = True if str(
            SearchSmartModeUsage) == "2" else False

        x = str(SearchSmartModeKeywordsList)

        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])

        WebsiteData.search["custom_api_data_all_keywords_list"] = y

        WebsiteData.search["custom_api_data"][0]["api_info"]["usage"] = True if str(
            SearchTheCatAPIUsage) == "2" else False
        WebsiteData.search["custom_api_data"][0]["api_info"]["name"] = str(
            SearchTheCatAPIName)

        x = str(SearchTheCatAPIKeywordList)

        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])

        WebsiteData.search["custom_api_data"][0]["keywords"] = y

        WebsiteData.search["custom_api_data"][0]["api_info"]["size"] = str(
            SearchTheCatAPISize)
        try:
            WebsiteData.search["custom_api_data"][0]["api_info"]["limit"] = int(
                SearchTheCatAPILimit)
        except:
            WebsiteData.search["custom_api_data"][0]["api_info"]["limit"] = str(
                SearchTheCatAPILimit)
        WebsiteData.search["custom_api_data"][0]["api_info"]["mime_types"] = str(
            SearchTheCatAPIMineTypes)
        WebsiteData.search["custom_api_data"][0]["api_info"]["order"] = str(
            SearchTheCatAPIOrder)
        try:
            WebsiteData.search["custom_api_data"][0]["api_info"]["has_breeds"] = int(
                SearchTheCatAPIHasBreeds)
        except:
            WebsiteData.search["custom_api_data"][0]["api_info"]["has_breeds"] = str(
                SearchTheCatAPIHasBreeds)
        WebsiteData.search["custom_api_data"][0]["api_info"]["api_url"] = str(
            SearchTheCatAPIApiURL)

        WebsiteData.search["custom_api_data"][1]["api_info"]["usage"] = True if str(
            SearchDogCEOUsage) == "2" else False
        WebsiteData.search["custom_api_data"][1]["api_info"]["name"] = str(
            SearchDogCEOName)
        try:
            WebsiteData.search["custom_api_data"][1]["api_info"]["limit"] = int(
                SearchDogCEOLimit)
        except:
            WebsiteData.search["custom_api_data"][1]["api_info"]["limit"] = str(
                SearchDogCEOLimit)
        WebsiteData.search["custom_api_data"][1]["api_info"]["api_url"] = str(
            SearchDogCEOApiURL)

        x = str(SearchDogCEOKeywordsList)

        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])

        WebsiteData.search["custom_api_data"][1]["keywords"] = y

        WebsiteData.search["custom_api_data"][2]["api_info"]["usage"] = True if str(
            SearchNekosLifeUsage) == "2" else False
        WebsiteData.search["custom_api_data"][2]["api_info"]["name"] = str(
            SearchNekosLifeName)
        try:
            WebsiteData.search["custom_api_data"][2]["api_info"]["limit"] = int(
                SearchNekosLifeLimit)
        except:
            WebsiteData.search["custom_api_data"][2]["api_info"]["limit"] = str(
                SearchNekosLifeLimit)

        x = str(SearchNekosLifeURLlist)

        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])

        WebsiteData.search["custom_api_data"][2]["api_info"]["api_url_list"] = y

        x = str(SearchNekosLifeKeywordList)

        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])

        WebsiteData.search["custom_api_data"][2]["keywords"] = y

        WebsiteData._data["search"] = WebsiteData.search

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

    def Pins(
        PinsMainTitle
    ):
        WebsiteData.pins["title"] = str(PinsMainTitle)
        WebsiteData._data["pins"] = WebsiteData.pins

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

    def AdultIndex(
        AdultIndexMainTitle,
        AdultIndexMainRandomSearchWordsList,

        AdultIndexhEpornerUsage,
        AdultIndexhEpornerLimit,
        AdultIndexhEpornerThumbSize,
        AdultIndexhEpornerOrder,
        AdultIndexhEpornerAPIUrl,

        AdultIndexhRedTubeUsage,
        AdultIndexhRedTubeLimit,
        AdultIndexhRedTubeData,
        AdultIndexhRedTubeThumbSize,
        AdultIndexhRedTubeAPIUrl
    ):

        WebsiteData.adult_index["title"] = str(AdultIndexMainTitle)

        x = str(AdultIndexMainRandomSearchWordsList)
        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])
        WebsiteData.adult_index["api_usage"]["random_search_word"] = y

        WebsiteData.adult_index["api_usage"]["eporner"]["usage"] = True if str(
            AdultIndexhEpornerUsage) == "2" else False
        try:
            WebsiteData.adult_index["api_usage"]["eporner"]["limit"] = int(
                AdultIndexhEpornerLimit)
        except:
            WebsiteData.adult_index["api_usage"]["eporner"]["limit"] = str(
                AdultIndexhEpornerLimit)
        WebsiteData.adult_index["api_usage"]["eporner"]["thumbsize"] = str(
            AdultIndexhEpornerThumbSize)
        WebsiteData.adult_index["api_usage"]["eporner"]["order"] = str(
            AdultIndexhEpornerOrder)
        WebsiteData.adult_index["api_usage"]["eporner"]["api_url"] = str(
            AdultIndexhEpornerAPIUrl)

        WebsiteData.adult_index["api_usage"]["redtube"]["usage"] = True if str(
            AdultIndexhRedTubeUsage) == "2" else False
        try:
            WebsiteData.adult_index["api_usage"]["redtube"]["limit"] = int(
                AdultIndexhRedTubeLimit)
        except:
            WebsiteData.adult_index["api_usage"]["redtube"]["limit"] = str(
                AdultIndexhRedTubeLimit)
        WebsiteData.adult_index["api_usage"]["redtube"]["data"] = str(
            AdultIndexhRedTubeData)
        WebsiteData.adult_index["api_usage"]["redtube"]["thumbsize"] = str(
            AdultIndexhRedTubeThumbSize)
        WebsiteData.adult_index["api_usage"]["redtube"]["api_url"] = str(
            AdultIndexhRedTubeAPIUrl)

        WebsiteData._data["adult_index"] = WebsiteData.adult_index

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

    def AdultPins(
        AdultPinsMainTitle,
        AdultPinsMainOtherTitle,
        AdultCategoriesTitle
    ):
        WebsiteData.adult_pins["title"] = str(AdultPinsMainTitle)
        WebsiteData.adult_pins["all_pins_title"] = str(AdultPinsMainOtherTitle)
        WebsiteData.adult_pins["all_categories_title"] = str(
            AdultCategoriesTitle)

        WebsiteData._data["adult_pins_and_categories"] = WebsiteData.adult_pins

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

    def AdultStars(
        AdultStarsMainTitle,
        AdultStarsRedTubeUsage,
        AdultStarsRedTubeData,
        AdultStarsRedTubeApiURL
    ):
        WebsiteData.adult_stars["title"] = str(AdultStarsMainTitle)

        WebsiteData.adult_stars["api_usage"]["usage"] = True if str(
            AdultStarsRedTubeUsage) == "2" else False
        WebsiteData.adult_stars["api_usage"]["api_url"] = str(
            AdultStarsRedTubeApiURL)
        WebsiteData.adult_stars["api_usage"]["data"] = str(
            AdultStarsRedTubeData)

        WebsiteData._data["adult_stars"] = WebsiteData.adult_stars

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

    def AdultSearch(
        AdultSearchMainTitle,
        AdultSearchEpornerUsage,
        AdultSearchEpornerLimit,
        AdultSearchEpornerThumbSize,
        AdultSearchEpornerOrder,
        AdultSearchEpornerApiURL,
        AdultSearchRedTubeUsage,
        AdultSearchRedTubeLimit,
        AdultSearchRedTubeData,
        AdultSearchRedTubeThumbSize,
        AdultSearchRedTubeApiURL
    ):
        WebsiteData.adult_search["title"] = str(AdultSearchMainTitle)

        WebsiteData.adult_search["api_usage"]["eporner"]["usage"] = True if str(
            AdultSearchEpornerUsage) == "2" else False
        try:
            WebsiteData.adult_search["api_usage"]["eporner"]["limit"] = int(
                AdultSearchEpornerLimit)
        except:
            WebsiteData.adult_search["api_usage"]["eporner"]["limit"] = str(
                AdultSearchEpornerLimit)
        WebsiteData.adult_search["api_usage"]["eporner"]["thumbsize"] = str(
            AdultSearchEpornerThumbSize)
        WebsiteData.adult_search["api_usage"]["eporner"]["order"] = str(
            AdultSearchEpornerOrder)
        WebsiteData.adult_search["api_usage"]["eporner"]["api_url"] = str(
            AdultSearchEpornerApiURL)

        WebsiteData.adult_search["api_usage"]["redtube"]["usage"] = True if str(
            AdultSearchRedTubeUsage) == "2" else False
        try:
            WebsiteData.adult_search["api_usage"]["redtube"]["limit"] = int(
                AdultSearchRedTubeLimit)
        except:
            WebsiteData.adult_search["api_usage"]["redtube"]["limit"] = str(
                AdultSearchRedTubeLimit)
        WebsiteData.adult_search["api_usage"]["redtube"]["data"] = str(
            AdultSearchRedTubeData)
        WebsiteData.adult_search["api_usage"]["redtube"]["thumbsize"] = str(
            AdultSearchRedTubeThumbSize)
        WebsiteData.adult_search["api_usage"]["redtube"]["api_url"] = str(
            AdultSearchRedTubeApiURL)

        WebsiteData._data["adult_search"] = WebsiteData.adult_search

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

    def AdultHentai(
        AdultHentaiMainTitle,
        AdultHentaiLocalServerUsage,
        AdultHentaiLocalServerLimit,
        AdultHentaiLocalServerApiURL,
        AdultHentaiLocalServerEndpointsList,

        AdultHentaiNekosLifeUsage,
        AdultHentaiNekosLifeLimit,
        AdultHentaiNekosLifeApiURL,
        AdultHentaiNekosLifeEndpointsList,
    ):

        WebsiteData.adult_hentai["title"] = str(AdultHentaiMainTitle)

        WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["usage"] = True if str(
            AdultHentaiLocalServerUsage) == "2" else False
        try:
            WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["limit"] = int(
                AdultHentaiLocalServerLimit)
        except:
            WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["limit"] = str(
                AdultHentaiLocalServerLimit)
        WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["api_url"] = str(
            AdultHentaiLocalServerApiURL)

        x = str(AdultHentaiLocalServerEndpointsList)
        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])
        WebsiteData.adult_hentai["api_usage"]["localserverml_api"]["localserverml_enpoints"] = y

        WebsiteData.adult_hentai["api_usage"]["nekoslife"]["usage"] = True if str(
            AdultHentaiNekosLifeUsage) == "2" else False
        try:
            WebsiteData.adult_hentai["api_usage"]["nekoslife"]["limit"] = int(
                AdultHentaiNekosLifeLimit)
        except:
            WebsiteData.adult_hentai["api_usage"]["nekoslife"]["limit"] = str(
                AdultHentaiNekosLifeLimit)
        WebsiteData.adult_hentai["api_usage"]["nekoslife"]["api_url"] = str(
            AdultHentaiNekosLifeApiURL)

        x = str(AdultHentaiNekosLifeEndpointsList)
        splitted = x.split(",")
        splitted[-1] = splitted[-1][:-1]
        splitted[0] = splitted[0][1:]
        y = []
        for i in splitted:
            y.append(str(i).strip()[1:-1])
        WebsiteData.adult_hentai["api_usage"]["nekoslife"]["nekoslife_endpoints"] = y

        WebsiteData._data["adult_hentai"] = WebsiteData.adult_hentai

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

    def AgeVerify(
        AgeVerifyMainTitle,
        AgeVerifyMainSubTopic,
        AgeVerifyMainBody,
        AgeVerifyButtonsYes,
        AgeVerifyButtonsNo
    ):
        WebsiteData.age_verify["title"] = str(AgeVerifyMainTitle)
        WebsiteData.age_verify["body_title"] = str(AgeVerifyMainSubTopic)
        WebsiteData.age_verify["text"] = str(AgeVerifyMainBody)

        WebsiteData.age_verify["buttons"]["yes"] = str(AgeVerifyButtonsYes)
        WebsiteData.age_verify["buttons"]["yes"] = str(AgeVerifyButtonsNo)

        WebsiteData._data["age_verify"] = WebsiteData.age_verify

        with open(FileNames.website_info_file, "w", encoding="utf-8") as _file:
            json.dump(WebsiteData._data, _file, indent=4)

