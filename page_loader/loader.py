import os
import re
from urllib.parse import urljoin, urlparse
import requests
import logging.config
from bs4 import BeautifulSoup
from page_loader.logger_config import LOGGING_CONFIG
from page_loader.logger_config import log_info, log_error
from progress.bar import ShadyBar


logging.config.dictConfig(LOGGING_CONFIG)


def download(page_url, path):
    check_log = 'Check .page-loader-errors.log for details'
    check_url = 'Failed to access the site. Check your internet access or url:'

    from page_loader import ExpectedException


    try:
        page = get_data(page_url)
        page.raise_for_status()
    except requests.RequestException as error:
        log_error.error(error)
        log_info.info(f'\n{check_url} {page_url}\n{check_log}')
        raise ExpectedException(error)

    log_info.info('Successful connection!')
    file_name = get_dest_name(page_url) + '.html'
    dir_name = get_dest_name(page_url) + '_files'
    dir_path = os.path.join(path, dir_name)
    os.mkdir(dir_path)
    log_info.info(f'Directory was created: {dir_path}')
    html = get_resources(page, dir_name, page_url, dir_path)
    file_path = os.path.join(path, file_name)
    with open(file_path, 'w') as f:
        f.write(html)
    log_info.info(f'HTML file was downloaded while pathing to {file_path}')
    return file_path


def get_dest_name(source):
    # cut scheme from url for future output file name
    match = re.search(r"(?<=//).*", source)
    name = re.sub(r"\W", "-", match.group())
    return name


def get_resources(source, directory, page_url, dir_path):
    tag_attr_dict = {
        'img': 'src',
        'link': 'href',
        'script': 'src',
    }
    soup = BeautifulSoup(source.content, "html.parser")
    tags = soup.findAll(['img', 'link', 'script'])
    len_for_bar = len(tags)
    if not tags:
        log_error.error(f"Attributes src weren't found in {tags}\n")

    with ShadyBar('Downloading',
                  max=len_for_bar,
                  suffix='%(percent)d%%') as bar:
        for tag in tags:
            bar.next()
            attr = tag_attr_dict[tag.name]
            url = tag.get(attr)
            full_url = urljoin(page_url, url)
            if urlparse(full_url).netloc == urlparse(page_url).netloc:
                file_ext = os.path.splitext(full_url)
                if file_ext[1] == '':
                    file_name = get_dest_name(file_ext[0]) + '.html'
                else:
                    file_name = get_dest_name(file_ext[0]) + file_ext[1]
                download_file(full_url, file_name, dir_path)
                tag[attr] = os.path.join(directory, file_name)
    return soup.prettify()


def download_file(url, file_name, dir_name):
    response = get_data(url)
    with open(os.path.join(dir_name, file_name), 'wb') as file:
        # file.write(response.content)
        for chunk in response.iter_content(chunk_size=1024):
            # filter out keep-alive new chunks
            if chunk:
                file.write(chunk)


def get_data(link):
    from page_loader import ExpectedException

    check_log = 'Check .page-loader-errors.log for details'
    check_url = 'Failed to access the site. Check your internet access or url:'

    try:
        response = requests.get(link)
        response.raise_for_status()
    except requests.RequestException as error:
        log_error.error(error)
        log_info.info(f'\n{check_url} {link}\n{check_log}')
        raise ExpectedException(error)
    return response
