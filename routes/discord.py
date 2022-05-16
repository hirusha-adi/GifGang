import services
from flask import redirect, render_template, request, url_for
from utils import WebsiteData, count_total_visits_amount, log, logf, Vars


def discord_index():
    count_total_visits_amount()
    logf(request=request, page="discord")
    log(f'Requested `/discord` - discord_index()',
        ipaddr=request.remote_addr)

    return render_template(
        "discord/index.html",
        web_title="Discord Bot | GifGang"
    )
