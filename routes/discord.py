from flask import redirect, render_template, request, url_for
from utils import WebsiteData, count_total_visits_amount, log, logf, Vars


def discord_index():
    count_total_visits_amount()
    logf(request=request, page="discord")
    log(f'Requested `/discord` - discord_index()',
        ipaddr=request.remote_addr)

    return render_template(
        "discord/index.html",
        web_title="Discord Bot | GifGang",
    )


def discord_join_server():
    count_total_visits_amount()
    logf(request=request, page="discord/join")
    log(f'Requested `/discord/join` - discord_join_server()',
        ipaddr=request.remote_addr)

    return redirect(WebsiteData.discord["web_links"]["invite_to_server"])


def discord_view_help():
    count_total_visits_amount()
    logf(request=request, page="discord/help")
    log(f'Requested `/discord/help` - discord_view_help()',
        ipaddr=request.remote_addr)

    return redirect(WebsiteData.discord["web_links"]["commands_help_link"])
