
import logging
import os
import time
from threading import Thread

from flask import Flask, render_template

from routes.admin import (admin_download_log_file, admin_login_page,
                          admin_login_page_verify, admin_logout,
                          admin_panel_page, admin_save_settings,
                          admin_setting_sfw, admin_settings,
                          admin_settings_nsfw, adult_route_main)
from routes.adult import (adult_categories, adult_hentai, adult_index,
                          adult_pins, adult_search, adult_search_no_query,
                          adult_search_post, adult_stars, adult_stars_no_page)
from routes.original import (about, all_links, index, pins, public_stats,
                             restricted, search, search_no_query, search_post)
from utils import Config, count_total_visits_amount, log
from utils.vars import COUNT, COUNT_TODAY

app = Flask(__name__)
log("Initiated Flask App: 'app'")
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)
log("Disabled the default `werkzeug` logging")

app.secret_key = "VerySecret12345"


app.add_url_rule("/", 'index', index)
app.add_url_rule("/pins", 'pins', pins)
app.add_url_rule("/search", 'search_no_query', search_no_query)
app.add_url_rule("/search/<query>", 'search', search)
app.add_url_rule("/search_post", 'search_post', search_post)
app.add_url_rule("/about", 'about', about)
app.add_url_rule("/links", 'all_links', all_links)
app.add_url_rule("/all_links", 'all_links', all_links)
app.add_url_rule("/restricted", 'restricted', restricted)
app.add_url_rule("/stats", 'public_stats', public_stats)

app.add_url_rule("/adult", 'adult_index', adult_index)
app.add_url_rule("/adult/pins", 'adult_pins', adult_pins)
app.add_url_rule("/adult/categories", 'adult_categories', adult_categories)
app.add_url_rule("/adult/pornstars", 'adult_stars_no_page', adult_stars_no_page)
app.add_url_rule("/adult/stars", 'adult_stars_no_page', adult_stars_no_page)
app.add_url_rule("/adult/pornstars/<page>", 'adult_stars', adult_stars)
app.add_url_rule("/adult/stars/<page>", 'adult_stars', adult_stars)
app.add_url_rule("/adult/search_post", 'adult_search_post', adult_search_post)
app.add_url_rule("/adult/adult_search_no_query", 'adult_search_no_query', adult_search_no_query)
app.add_url_rule("/adult/search/<query>", 'adult_search', adult_search)
app.add_url_rule("/adult/hentai", 'adult_hentai', adult_hentai)

app.add_url_rule("/admin", 'adult_route_main', adult_route_main)
app.add_url_rule("/admin/login", 'admin_login_page', admin_login_page)
app.add_url_rule("/admin/login/verify", 'admin_login_page_verify', admin_login_page_verify)
app.add_url_rule("/admin/download/log/latest", 'admin_download_log_file', admin_download_log_file)
app.add_url_rule("/admin/panel", 'admin_panel_page', admin_panel_page)
app.add_url_rule("/admin/settings/<mode>/<site>", 'admin_save_settings', admin_save_settings)
app.add_url_rule("/admin/settings", 'admin_settings', admin_settings)
app.add_url_rule("/admin/settings/<site>", 'admin_setting_sfw', admin_setting_sfw)
app.add_url_rule("/admin/settings/adult/<site>", 'admin_settings_nsfw', admin_settings_nsfw)
app.add_url_rule("/logout", 'admin_logout', admin_logout)



@app.errorhandler(404)
def page_not_found(e):
    count_total_visits_amount()
    return render_template('404.html'), 404


def reload_daily_count():
    global COUNT_TODAY
    while True:
        COUNT_TODAY = 0
        time.sleep(86400)


def runWebServer():
    reset_count_24h = Thread(target=reload_daily_count)
    reset_count_24h.start()

    print(
        f"[+] The server will run on:\n\t[*] SFW: http://{'localhost' if (Config.host == '0.0.0.0') or (Config.host == '127.0.0.1') else Config.host}:{Config.port}/\n\t[*] NSFW: http://{'localhost' if (Config.host == '0.0.0.0') or (Config.host == '127.0.0.1') else Config.host}:{Config.port}/adult\n\t[*] Host: {Config.host}\n\t[*] Port: {Config.port}\n\t[*] Debug Mode: {Config.debug}")
    app.run(Config.host,
            port=Config.port,
            debug=Config.debug,
            )


if __name__ == "__main__":
    runWebServer()
