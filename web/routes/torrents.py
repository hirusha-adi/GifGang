import services
from flask import redirect, render_template, request, url_for
from utils import WebsiteData, count_total_visits_amount, log, logf


def torrents_index():
    return render_template(
        "torrents/index.html",
        show_torrents_index=True
    )
