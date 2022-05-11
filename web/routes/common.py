import services
from flask import redirect, render_template, request, url_for
from utils import WebsiteData, count_total_visits_amount, log, logf, Vars


def restricted():
    count_total_visits_amount()

    logf(request=request, page="restricted")

    log(f'Request `/restricted` - restricted()',
        ipaddr=request.remote_addr)
    log(
        f'Returning `age_verify.html`\n\tTitle={WebsiteData.age_verify["title"]}\n\tBody Title={WebsiteData.age_verify["body_title"]}\n\tBody Text={WebsiteData.age_verify["text"]}\n\tYes Button Text={WebsiteData.age_verify["buttons"]["yes"]}\n\tNo Button Text={WebsiteData.age_verify["buttons"]["no"]}',
        ipaddr=request.remote_addr)

    return render_template(
        "age_verify.html",
        web_title=WebsiteData.age_verify["title"],
        body_title=WebsiteData.age_verify["body_title"],
        age_verify_text=WebsiteData.age_verify["text"],
        button_yes=WebsiteData.age_verify["buttons"]["yes"],
        button_no=WebsiteData.age_verify["buttons"]["no"],
    )


def search_everything_page():
    return render_template("search.html")
