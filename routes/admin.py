import os

from flask import (redirect, render_template, request, send_file, session,
                   url_for)
from utils import (FileNames, Important, Settings, Update, WebsiteData,
                   count_total_visits_amount, log, logf, Vars)


def adult_route_main():
    count_total_visits_amount()

    logf(request=request, page=f"admin")

    log(f'Request `/admin` - adult_route_main()',
        ipaddr=request.remote_addr)

    return redirect(url_for('admin_login_page'))


def admin_login_page():
    count_total_visits_amount()

    logf(request=request, page=f"admin/login")

    log(f'Request `/admin/login` - admin_login_page()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return redirect(url_for('admin_panel_page'))
    except KeyError:
        session["token"] = ""

    return render_template(
        "admin/login.html"
    )


def admin_login_page_verify():
    count_total_visits_amount()

    logf(request=request, page=f"admin/login/verify")

    log(f'Request `/admin/login/verify` - admin_login_page_verify()',
        ipaddr=request.remote_addr)

    try:
        username = request.form.get("uname")
        password = request.form.get("pass")
    except:
        return redirect(url_for('admin_login_page'))

    if (username == Settings.Admin.username) and (password == Settings.Admin.password):
        session["token"] = Settings.Admin.token
        return redirect(url_for("admin_panel_page"))
    else:
        return redirect(url_for('admin_login_page'))


def admin_download_log_file():
    count_total_visits_amount()

    logf(request=request, page="admin/download/log/latest")

    log(f'Requested `/admin/download/log/latest` - admin_download_log_file()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return send_file(FileNames._log_file)

        else:
            return redirect(url_for("admin_login_page"))
    except:
        return redirect(url_for("admin_login_page"))


def admin_panel_page():
    count_total_visits_amount()

    logf(request=request, page="admin/panel")

    log(f'Requested `/admin/panel` - admin_panel_page()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:

            percentage_of_today_from_total = round(
                ((Vars.COUNT_TODAY/Vars.COUNT)*100), 2)

            percentage_target_today = round(
                ((Vars.COUNT_TODAY/Settings.Admin.targets_today)*100), 2)
            percentage_target_all = round(
                ((Vars.COUNT/Settings.Admin.targets_all)*100), 2)

            try:
                final_log_file_name = os.listdir(
                    os.path.join(os.getcwd(), "logs"))[-1]
                final_log_file = os.path.join(
                    os.getcwd(),
                    "logs",
                    final_log_file_name
                )

                with open(final_log_file, "r", encoding="utf-8") as log_file_content:
                    log_file_lines = log_file_content.readlines()[-5:]

                log_file_lines_last_5 = log_file_lines[::-1]

            except Exception as e:
                print(e)
                final_log_file_name = str(e)
                log_file_lines_last_5 = []

            return render_template(
                "admin/panel.html",
                total_requests_all_time=Vars.COUNT,
                total_requests_last_24h=Vars.COUNT_TODAY,
                percentage_of_today_from_total=percentage_of_today_from_total,
                final_log_file_name=final_log_file_name,
                log_file_lines_last_5=log_file_lines_last_5,
                percentage_target_today=percentage_target_today,
                percentage_target_all=percentage_target_all,
                admin_profile_picture=Settings.Admin.profile_pic,
            )

        else:
            return redirect(url_for("admin_login_page"))
    except:
        return redirect(url_for("admin_login_page"))


def admin_save_settings(mode, site):
    count_total_visits_amount()

    logf(request=request, page=f"admin/settings/{mode}/{site}")

    log(f'Requested `/admin/settings/{mode}/{site} - admin_save_settings(mode, site)',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            site = str(site)
            mode = str(mode)

            if mode == "sfw":

                if site == "important":
                    ImportantGiphyUsage = request.form.get(
                        'ImportantGiphyUsage')
                    ImportantGiphyApiBaseURL = request.form.get(
                        'ImportantGiphyApiBaseURL')
                    ImportantGiphyAPIKey = request.form.get(
                        'ImportantGiphyAPIKey')

                    ImportantPicsumUsage = request.form.get(
                        'ImportantPicsumUsage')
                    ImportantPicsumApiBaseURL = request.form.get(
                        'ImportantPicsumApiBaseURL')

                    ImportantTenorUsage = request.form.get(
                        'ImportantTenorUsage')
                    ImportantTenorApiBaseURL = request.form.get(
                        'ImportantTenorApiBaseURL')

                    ImportantOtherTheCatAPI = request.form.get(
                        'ImportantOtherTheCatAPI')
                    ImportantOtherDogCEO = request.form.get(
                        'ImportantOtherDogCEO')
                    ImportantOtherNekosLife = request.form.get(
                        'ImportantOtherNekosLife')
                    ImportantOtherEPorner = request.form.get(
                        'ImportantOtherEPorner')
                    ImportantOtherRedTube = request.form.get(
                        'ImportantOtherRedTube')
                    ImportantOtherLocalServerML = request.form.get(
                        'ImportantOtherLocalServerML')

                    Update.Important(
                        giphy_usage=ImportantGiphyUsage,
                        giphy_api_url_base=ImportantGiphyApiBaseURL,
                        giphy_api_key=ImportantGiphyAPIKey,
                        picsum_usage=ImportantPicsumUsage,
                        picsum_api_url_base=ImportantPicsumApiBaseURL,
                        tenor_usage=ImportantTenorUsage,
                        tenor_api_key=ImportantTenorApiBaseURL,
                        thecatapi_usage=ImportantOtherTheCatAPI,
                        dogceo_usage=ImportantOtherDogCEO,
                        nekoslife_usage=ImportantOtherNekosLife,
                        eporner_usage=ImportantOtherEPorner,
                        redtube_usage=ImportantOtherRedTube,
                        localserverml_usage=ImportantOtherLocalServerML
                    )

                    return redirect(url_for('admin_setting_sfw', site='important'))

                elif site == "index":
                    IndexMainTitle = request.form.get('IndexMainTitle')

                    IndexGiphyUsage = request.form.get('IndexGiphyUsage')
                    IndexGiphyRandomUsage = request.form.get(
                        'IndexGiphyRandomUsage')
                    IndexGiphyRandomLimit = request.form.get(
                        'IndexGiphyRandomLimit')
                    IndexGiphyRandomAPIurl = request.form.get(
                        'IndexGiphyRandomAPIurl')
                    IndexGiphyTrendingUsage = request.form.get(
                        'IndexGiphyTrendingUsage')
                    IndexGiphyTrendingLimit = request.form.get(
                        'IndexGiphyTrendingLimit')
                    IndexGiphyTendingAPIurl = request.form.get(
                        'IndexGiphyTendingAPIurl')

                    IndexPicsumUsage = request.form.get('IndexPicsumUsage')
                    IndexPicsumLimit = request.form.get('IndexPicsumLimit')
                    IndexPicsumApiURL = request.form.get('IndexPicsumApiURL')

                    IndexTenorUsage = request.form.get('IndexTenorUsage')
                    IndexTenorLimit = request.form.get('IndexTenorLimit')
                    IndexTenorLocale = request.form.get('IndexTenorLocale')
                    IndexTenorArRange = request.form.get('IndexTenorArRange')
                    IndexTenorContentFilter = request.form.get(
                        'IndexTenorContentFilter')
                    IndexTenorApiURL = request.form.get('IndexTenorApiURL')

                    IndexTheCatAPIUsage = request.form.get(
                        'IndexTheCatAPIUsage')
                    IndexTheCatAPILimit = request.form.get(
                        'IndexTheCatAPILimit')
                    IndexTheCatAPISize = request.form.get('IndexTheCatAPISize')
                    IndexTheCatAPIMineTypes = request.form.get(
                        'IndexTheCatAPIMineTypes')
                    IndexTheCatAPIOrder = request.form.get(
                        'IndexTheCatAPIOrder')
                    IndexTheCatAPIHasBreeds = request.form.get(
                        'IndexTheCatAPIHasBreeds')
                    IndexTheCatAPIAPIUrl = request.form.get(
                        'IndexTheCatAPIAPIUrl')

                    IndexDogCEOUsage = request.form.get('IndexDogCEOUsage')
                    IndexDogCEOLimit = request.form.get('IndexDogCEOLimit')
                    IndexDogCEOApiURL = request.form.get('IndexDogCEOApiURL')

                    IndexNekosLifeUsage = request.form.get(
                        'IndexNekosLifeUsage')
                    IndexNekosLifeLimit = request.form.get(
                        'IndexNekosLifeLimit')
                    IndexNekosLifeURLlist = request.form.get(
                        'IndexNekosLifeURLlist')

                    Update.Index(
                        IndexMainTitle=IndexMainTitle,
                        IndexGiphyUsage=IndexGiphyUsage,
                        IndexGiphyRandomUsage=IndexGiphyRandomUsage,
                        IndexGiphyRandomLimit=IndexGiphyRandomLimit,
                        IndexGiphyRandomAPIurl=IndexGiphyRandomAPIurl,
                        IndexGiphyTrendingUsage=IndexGiphyTrendingUsage,
                        IndexGiphyTrendingLimit=IndexGiphyTrendingLimit,
                        IndexGiphyTendingAPIurl=IndexGiphyTendingAPIurl,
                        IndexPicsumUsage=IndexPicsumUsage,
                        IndexPicsumLimit=IndexPicsumLimit,
                        IndexPicsumApiURL=IndexPicsumApiURL,
                        IndexTenorUsage=IndexTenorUsage,
                        IndexTenorLimit=IndexTenorLimit,
                        IndexTenorLocale=IndexTenorLocale,
                        IndexTenorArRange=IndexTenorArRange,
                        IndexTenorContentFilter=IndexTenorContentFilter,
                        IndexTenorApiURL=IndexTenorApiURL,
                        IndexTheCatAPIUsage=IndexTheCatAPIUsage,
                        IndexTheCatAPILimit=IndexTheCatAPILimit,
                        IndexTheCatAPISize=IndexTheCatAPISize,
                        IndexTheCatAPIMineTypes=IndexTheCatAPIMineTypes,
                        IndexTheCatAPIOrder=IndexTheCatAPIOrder,
                        IndexTheCatAPIHasBreeds=IndexTheCatAPIHasBreeds,
                        IndexTheCatAPIAPIUrl=IndexTheCatAPIAPIUrl,
                        IndexDogCEOUsage=IndexDogCEOUsage,
                        IndexDogCEOLimit=IndexDogCEOLimit,
                        IndexDogCEOApiURL=IndexDogCEOApiURL,
                        IndexNekosLifeUsage=IndexNekosLifeUsage,
                        IndexNekosLifeLimit=IndexNekosLifeLimit,
                        IndexNekosLifeURLlist=IndexNekosLifeURLlist
                    )

                    return redirect(url_for('admin_setting_sfw', site='index'))

                elif site == "search":
                    SearchMainTitle = request.form.get('SearchMainTitle')

                    SearchGiphyUsage = request.form.get('SearchGiphyUsage')
                    SearchGiphyLimit = request.form.get('SearchGiphyLimit')
                    SearchGiphyOffset = request.form.get('SearchGiphyOffset')
                    SearchGiphyApiURL = request.form.get('SearchGiphyApiURL')

                    SearchTenorUsage = request.form.get('SearchTenorUsage')
                    SearchTenorLimit = request.form.get('SearchTenorLimit')
                    SearchTenorLocale = request.form.get('SearchTenorLocale')
                    SearchTenorArRange = request.form.get('SearchTenorArRange')
                    SearchTenorContentFilter = request.form.get(
                        'SearchTenorContentFilter')
                    SearchTenorApiURL = request.form.get('SearchTenorApiURL')

                    SearchSmartModeUsage = request.form.get(
                        'SearchSmartModeUsage')
                    SearchSmartModeKeywordsList = request.form.get(
                        'SearchSmartModeKeywordsList')

                    SearchTheCatAPIUsage = request.form.get(
                        'SearchTheCatAPIUsage')
                    SearchTheCatAPIName = request.form.get(
                        'SearchTheCatAPIName')
                    SearchTheCatAPIKeywordList = request.form.get(
                        'SearchTheCatAPIKeywordList')
                    SearchTheCatAPILimit = request.form.get(
                        'SearchTheCatAPILimit')
                    SearchTheCatAPISize = request.form.get(
                        'SearchTheCatAPISize')
                    SearchTheCatAPIMineTypes = request.form.get(
                        'SearchTheCatAPIMineTypes')
                    SearchTheCatAPIOrder = request.form.get(
                        'SearchTheCatAPIOrder')
                    SearchTheCatAPIHasBreeds = request.form.get(
                        'SearchTheCatAPIHasBreeds')
                    SearchTheCatAPIApiURL = request.form.get(
                        'SearchTheCatAPIApiURL')

                    SearchDogCEOUsage = request.form.get('SearchDogCEOUsage')
                    SearchDogCEOName = request.form.get('SearchDogCEOName')
                    SearchDogCEOKeywordsList = request.form.get(
                        'SearchDogCEOKeywordsList')
                    SearchDogCEOLimit = request.form.get('SearchDogCEOLimit')
                    SearchDogCEOApiURL = request.form.get('SearchDogCEOApiURL')

                    SearchNekosLifeUsage = request.form.get(
                        'SearchNekosLifeUsage')
                    SearchNekosLifeName = request.form.get(
                        'SearchNekosLifeName')
                    SearchNekosLifeKeywordList = request.form.get(
                        'SearchNekosLifeKeywordList')
                    SearchNekosLifeLimit = request.form.get(
                        'SearchNekosLifeLimit')
                    SearchNekosLifeURLlist = request.form.get(
                        'SearchNekosLifeURLlist')

                    Update.Search(
                        SearchMainTitle=SearchMainTitle,
                        SearchGiphyUsage=SearchGiphyUsage,
                        SearchGiphyLimit=SearchGiphyLimit,
                        SearchGiphyOffset=SearchGiphyOffset,
                        SearchGiphyApiURL=SearchGiphyApiURL,
                        SearchTenorUsage=SearchTenorUsage,
                        SearchTenorLimit=SearchTenorLimit,
                        SearchTenorLocale=SearchTenorLocale,
                        SearchTenorArRange=SearchTenorArRange,
                        SearchTenorContentFilter=SearchTenorContentFilter,
                        SearchTenorApiURL=SearchTenorApiURL,
                        SearchSmartModeUsage=SearchSmartModeUsage,
                        SearchSmartModeKeywordsList=SearchSmartModeKeywordsList,
                        SearchTheCatAPIUsage=SearchTheCatAPIUsage,
                        SearchTheCatAPIName=SearchTheCatAPIName,
                        SearchTheCatAPIKeywordList=SearchTheCatAPIKeywordList,
                        SearchTheCatAPISize=SearchTheCatAPISize,
                        SearchTheCatAPILimit=SearchTheCatAPILimit,
                        SearchTheCatAPIMineTypes=SearchTheCatAPIMineTypes,
                        SearchTheCatAPIOrder=SearchTheCatAPIOrder,
                        SearchTheCatAPIHasBreeds=SearchTheCatAPIHasBreeds,
                        SearchTheCatAPIApiURL=SearchTheCatAPIApiURL,
                        SearchDogCEOUsage=SearchDogCEOUsage,
                        SearchDogCEOName=SearchDogCEOName,
                        SearchDogCEOLimit=SearchDogCEOLimit,
                        SearchDogCEOApiURL=SearchDogCEOApiURL,
                        SearchDogCEOKeywordsList=SearchDogCEOKeywordsList,
                        SearchNekosLifeUsage=SearchNekosLifeUsage,
                        SearchNekosLifeName=SearchNekosLifeName,
                        SearchNekosLifeKeywordList=SearchNekosLifeKeywordList,
                        SearchNekosLifeLimit=SearchNekosLifeLimit,
                        SearchNekosLifeURLlist=SearchNekosLifeURLlist
                    )

                    return redirect(url_for('admin_setting_sfw', site='search'))

                elif site == "pins":

                    PinsMainTitle = request.form.get('PinsMainTitle')

                    Update.Pins(
                        PinsMainTitle=PinsMainTitle
                    )

                    return redirect(url_for('admin_setting_sfw', site='pins'))

                elif site == "age":
                    AgeVerifyMainTitle = request.form.get('AgeVerifyMainTitle')
                    AgeVerifyMainSubTopic = request.form.get(
                        'AgeVerifyMainSubTopic')
                    AgeVerifyMainBody = request.form.get('AgeVerifyMainBody')
                    AgeVerifyButtonsYes = request.form.get(
                        'AgeVerifyButtonsYes')
                    AgeVerifyButtonsNo = request.form.get('AgeVerifyButtonsNo')

                    Update.AgeVerify(
                        AgeVerifyMainTitle=AgeVerifyMainTitle,
                        AgeVerifyMainSubTopic=AgeVerifyMainSubTopic,
                        AgeVerifyMainBody=AgeVerifyMainBody,
                        AgeVerifyButtonsYes=AgeVerifyButtonsYes,
                        AgeVerifyButtonsNo=AgeVerifyButtonsNo
                    )

                    return redirect(url_for('admin_setting_sfw', site='age'))

                else:
                    AdminUserName = request.form.get('AdminUserName')
                    AdminUserPassword = request.form.get('AdminUserPassword')
                    AdminUserToken = request.form.get('AdminUserToken')
                    AdminUserProfilePicURL = request.form.get(
                        'AdminUserProfilePicURL')
                    TodaysTarget = request.form.get('TodaysTarget')
                    AllTimesTarget = request.form.get('AllTimesTarget')

                    Update.SettingsAdmin(
                        username=AdminUserName,
                        password=AdminUserPassword,
                        token=AdminUserToken,
                        profile_pic=AdminUserProfilePicURL,
                        targets_today=TodaysTarget,
                        targets_all=AllTimesTarget
                    )

                    return redirect(url_for('admin_setting_sfw', site='admin'))

            elif mode == "nsfw":

                if site == "index":

                    AdultIndexMainTitle = request.form.get(
                        'AdultIndexMainTitle')
                    AdultIndexMainRandomSearchWordsList = request.form.get(
                        'AdultIndexMainRandomSearchWordsList')

                    AdultIndexhEpornerUsage = request.form.get(
                        'AdultIndexhEpornerUsage')
                    AdultIndexhEpornerLimit = request.form.get(
                        'AdultIndexhEpornerLimit')
                    AdultIndexhEpornerThumbSize = request.form.get(
                        'AdultIndexhEpornerThumbSize')
                    AdultIndexhEpornerOrder = request.form.get(
                        'AdultIndexhEpornerOrder')
                    AdultIndexhEpornerAPIUrl = request.form.get(
                        'AdultIndexhEpornerAPIUrl')

                    AdultIndexhRedTubeUsage = request.form.get(
                        'AdultIndexhRedTubeUsage')
                    AdultIndexhRedTubeLimit = request.form.get(
                        'AdultIndexhRedTubeLimit')
                    AdultIndexhRedTubeData = request.form.get(
                        'AdultIndexhRedTubeData')
                    AdultIndexhRedTubeThumbSize = request.form.get(
                        'AdultIndexhRedTubeThumbSize')
                    AdultIndexhRedTubeAPIUrl = request.form.get(
                        'AdultIndexhRedTubeAPIUrl')

                    Update.AdultIndex(
                        AdultIndexMainTitle=AdultIndexMainTitle,
                        AdultIndexMainRandomSearchWordsList=AdultIndexMainRandomSearchWordsList,
                        AdultIndexhEpornerUsage=AdultIndexhEpornerUsage,
                        AdultIndexhEpornerLimit=AdultIndexhEpornerLimit,
                        AdultIndexhEpornerThumbSize=AdultIndexhEpornerThumbSize,
                        AdultIndexhEpornerOrder=AdultIndexhEpornerOrder,
                        AdultIndexhEpornerAPIUrl=AdultIndexhEpornerAPIUrl,
                        AdultIndexhRedTubeUsage=AdultIndexhRedTubeUsage,
                        AdultIndexhRedTubeLimit=AdultIndexhRedTubeLimit,
                        AdultIndexhRedTubeData=AdultIndexhRedTubeData,
                        AdultIndexhRedTubeThumbSize=AdultIndexhRedTubeThumbSize,
                        AdultIndexhRedTubeAPIUrl=AdultIndexhRedTubeAPIUrl
                    )

                    return redirect(url_for('admin_settings_nsfw', site='index'))

                elif site == "pins":

                    AdultPinsMainTitle = request.form.get('AdultPinsMainTitle')
                    AdultPinsMainOtherTitle = request.form.get(
                        'AdultPinsMainOtherTitle')
                    AdultCategoriesTitle = request.form.get(
                        'AdultCategoriesTitle')

                    Update.AdultPins(
                        AdultPinsMainTitle=AdultPinsMainTitle,
                        AdultPinsMainOtherTitle=AdultPinsMainOtherTitle,
                        AdultCategoriesTitle=AdultCategoriesTitle
                    )

                    return redirect(url_for('admin_settings_nsfw', site='pins'))

                elif site == "stars":

                    AdultStarsMainTitle = request.form.get(
                        'AdultStarsMainTitle')

                    AdultStarsRedTubeUsage = request.form.get(
                        'AdultStarsRedTubeUsage')
                    AdultStarsRedTubeData = request.form.get(
                        'AdultStarsRedTubeData')
                    AdultStarsRedTubeApiURL = request.form.get(
                        'AdultStarsRedTubeApiURL')

                    Update.AdultStars(
                        AdultStarsMainTitle=AdultStarsMainTitle,
                        AdultStarsRedTubeUsage=AdultStarsRedTubeUsage,
                        AdultStarsRedTubeData=AdultStarsRedTubeData,
                        AdultStarsRedTubeApiURL=AdultStarsRedTubeApiURL
                    )

                    return redirect(url_for('admin_settings_nsfw', site='stars'))

                elif site == "search":

                    AdultSearchMainTitle = request.form.get(
                        'AdultSearchMainTitle')

                    AdultSearchEpornerUsage = request.form.get(
                        'AdultSearchEpornerUsage')
                    AdultSearchEpornerLimit = request.form.get(
                        'AdultSearchEpornerLimit')
                    AdultSearchEpornerOrder = request.form.get(
                        'AdultSearchEpornerOrder')
                    AdultSearchEpornerThumbSize = request.form.get(
                        'AdultSearchEpornerThumbSize')
                    AdultSearchEpornerApiURL = request.form.get(
                        'AdultSearchEpornerApiURL')

                    AdultSearchRedTubeUsage = request.form.get(
                        'AdultSearchRedTubeUsage')
                    AdultSearchRedTubeLimit = request.form.get(
                        'AdultSearchRedTubeLimit')
                    AdultSearchRedTubeData = request.form.get(
                        'AdultSearchRedTubeData')
                    AdultSearchRedTubeThumbSize = request.form.get(
                        'AdultSearchRedTubeThumbSize')
                    AdultSearchRedTubeApiURL = request.form.get(
                        'AdultSearchRedTubeApiURL')

                    Update.AdultSearch(
                        AdultSearchMainTitle=AdultSearchMainTitle,
                        AdultSearchEpornerUsage=AdultSearchEpornerUsage,
                        AdultSearchEpornerLimit=AdultSearchEpornerLimit,
                        AdultSearchEpornerThumbSize=AdultSearchEpornerThumbSize,
                        AdultSearchEpornerOrder=AdultSearchEpornerOrder,
                        AdultSearchEpornerApiURL=AdultSearchEpornerApiURL,
                        AdultSearchRedTubeUsage=AdultSearchRedTubeUsage,
                        AdultSearchRedTubeLimit=AdultSearchRedTubeLimit,
                        AdultSearchRedTubeData=AdultSearchRedTubeData,
                        AdultSearchRedTubeThumbSize=AdultSearchRedTubeThumbSize,
                        AdultSearchRedTubeApiURL=AdultSearchRedTubeApiURL
                    )

                    return redirect(url_for('admin_settings_nsfw', site='search'))

                elif site == "hentai":

                    AdultHentaiMainTitle = request.form.get(
                        'AdultHentaiMainTitle')

                    AdultHentaiLocalServerUsage = request.form.get(
                        'AdultHentaiLocalServerUsage')
                    AdultHentaiLocalServerLimit = request.form.get(
                        'AdultHentaiLocalServerLimit')
                    AdultHentaiLocalServerApiURL = request.form.get(
                        'AdultHentaiLocalServerApiURL')
                    AdultHentaiLocalServerEndpointsList = request.form.get(
                        'AdultHentaiLocalServerEndpointsList')

                    AdultHentaiNekosLifeUsage = request.form.get(
                        'AdultHentaiNekosLifeUsage')
                    AdultHentaiNekosLifeLimit = request.form.get(
                        'AdultHentaiNekosLifeLimit')
                    AdultHentaiNekosLifeApiURL = request.form.get(
                        'AdultHentaiNekosLifeApiURL')
                    AdultHentaiNekosLifeEndpointsList = request.form.get(
                        'AdultHentaiNekosLifeEndpointsList')

                    Update.AdultHentai(
                        AdultHentaiMainTitle=AdultHentaiMainTitle,
                        AdultHentaiLocalServerUsage=AdultHentaiLocalServerUsage,
                        AdultHentaiLocalServerLimit=AdultHentaiLocalServerLimit,
                        AdultHentaiLocalServerApiURL=AdultHentaiLocalServerApiURL,
                        AdultHentaiLocalServerEndpointsList=AdultHentaiLocalServerEndpointsList,
                        AdultHentaiNekosLifeUsage=AdultHentaiNekosLifeUsage,
                        AdultHentaiNekosLifeLimit=AdultHentaiNekosLifeLimit,
                        AdultHentaiNekosLifeApiURL=AdultHentaiNekosLifeApiURL,
                        AdultHentaiNekosLifeEndpointsList=AdultHentaiNekosLifeEndpointsList
                    )

                    return redirect(url_for('admin_settings_nsfw', site='hentai'))

        else:
            return redirect(url_for("admin_login_page"))
    except:
        return redirect(url_for("admin_login_page"))


def admin_settings():
    count_total_visits_amount()

    logf(request=request, page="admin/settings")

    log(f'Requested `/admin/settings` - admin_settings()',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:
            return redirect(url_for('admin_setting', site="admin"))
        else:
            return redirect(url_for("admin_login_page"))
    except Exception as e:
        return redirect(url_for("admin_login_page"))


def admin_setting(site):
    count_total_visits_amount()

    logf(request=request, page="admin/settings/<site>")

    log(f'Requested `/admin/settings/<site>` - admin_setting(site)',
        ipaddr=request.remote_addr)

    try:
        if session["token"] == Settings.Admin.token:

            site = str(site)
            print(site)
            if site in ("main", "sfw"):
                return render_template(
                    "admin/settings.html",
                    show_all_sfw_settings=True,
                    index_data=WebsiteData.index,
                    age_verify_data=WebsiteData.age_verify,
                    search_data=WebsiteData.search,
                    pins_data=WebsiteData.pins,
                )
            elif site in ("adult", "nsfw"):
                return render_template(
                    "admin/settings.html",
                    show_all_nsfw_settings=True,
                    adult_pins_data=WebsiteData.adult_pins,
                    adult_stars_data=WebsiteData.adult_stars,
                    adult_search_data=WebsiteData.adult_search,
                    adult_hentai_data=WebsiteData.adult_hentai,
                    adult_index_data=WebsiteData.adult_index,
                )
            else:
                return render_template(
                    "admin/settings.html",
                    show_all_main_settings=True,
                    admin_settings_data=Settings.Admin,
                    import_settings_data=Important,
                )
        else:
            return redirect(url_for("admin_login_page"))
    except Exception as e:
        print(e)
        return redirect(url_for("admin_login_page"))


def admin_logout():
    count_total_visits_amount()

    logf(request=request, page="/logout")

    log(f'Requested `/logout` - count_total_visits_amount()',
        ipaddr=request.remote_addr)

    session["token"] = ""
    return redirect(url_for('admin_login_page'))
