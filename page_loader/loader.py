import re

import requests


def download(page_url, path):
    page = requests.get(page_url)
    name = get_dest_name(page_url)
    html = page.text

    return name


def get_dest_name(source):
    # get url address without scheme for future output file name
    match = re.search(r"(?<=//).*", source)
    # output file name will always be html
    name = re.sub(r"\W", "-", match.group()) + '.html'
    return name

print(get_dest_name('https://ru.hexlet.io/courses'))
