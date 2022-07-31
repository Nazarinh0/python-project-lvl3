import os
import re
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup


def download(page_url, path):
    page = requests.get(page_url)
    file_name = get_dest_name(page_url) + '.html'
    dir_name = get_dest_name(page_url) + '_files'
    dir_path = os.path.join(path, dir_name)
    os.mkdir(dir_path)
    html = get_resources(page, dir_name, page_url)
    file_path = os.path.join(path, file_name)
    with open(file_path, 'w') as f:
        f.write(html)
    return file_name


def get_dest_name(source):
    # cut scheme from url for future output file name
    match = re.search(r"(?<=//).*", source)
    name = re.sub(r"\W", "-", match.group())
    return name


def get_resources(source, directory, page_url):
    tag_attr_dict = {
        'img': 'src',
        'link': 'href',
        'script': 'src',
    }
    soup = BeautifulSoup(source.content, "html.parser")
    tags = soup.findAll(['img', 'link', 'script'])
    for tag in tags:
        attr = tag_attr_dict[tag.name]
        url = tag.get(attr)
        full_url = urljoin(page_url, url)
        if urlparse(full_url).netloc == urlparse(page_url).netloc:
            file_ext = os.path.splitext(full_url)
            file_name = get_dest_name(file_ext[0]) + file_ext[1]
            download_file(full_url, file_name, directory)
            tag[attr] = os.path.join(directory, file_name)
    return soup.prettify()


def download_file(url, file_name, dir_name):
    response = requests.get(url, stream=True)
    with open(os.path.join(dir_name, file_name), 'wb') as file:
        # file.write(response.content)
        for chunk in response.iter_content(chunk_size=1024):
            # filter out keep-alive new chunks
            if chunk:
                file.write(chunk)
