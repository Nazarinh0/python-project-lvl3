import os
import re
import requests


def download(page_url, path=os.getcwd()):
    page = requests.get(page_url)
    file_name = get_dest_name(page_url)
    html = page.text
    full_file_name = os.path.join(path, file_name)
    print(full_file_name)
    with open(full_file_name, 'w') as f:
        f.write(html)
    return file_name


def get_dest_name(source):
    # cut scheme from url for future output file name
    match = re.search(r"(?<=//).*", source)
    # output file name will always end with .html
    name = re.sub(r"\W", "-", match.group()) + '.html'
    return name

print(download("http://ru.hexlet.io/courses"))
