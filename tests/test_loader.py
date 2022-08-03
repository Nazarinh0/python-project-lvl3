import os.path
import tempfile
import requests_mock
from page_loader import download


def read(file, binary=False):
    if not binary:
        with open(file, 'r') as f:
            return f.read()
    with open(file, 'rb') as file:
        return file.read()


def test_loader_content():
    with requests_mock.Mocker() as m:
        page_url = 'http://ru.hexlet.io/courses'
        m.get(page_url, text='example text\n')
        with tempfile.TemporaryDirectory() as tmpdir:
            download(page_url, path=tmpdir)
            with open(os.path.join(tmpdir, 'ru-hexlet-io-courses.html')) as f:
                assert f.read() == 'example text\n'


def test_loader_filename():
    with requests_mock.Mocker() as m:
        page_url = 'http://ru.hexlet.io/courses'
        m.get(page_url, text='example text\n')
        with tempfile.TemporaryDirectory() as tmpdir:
            expected = tmpdir + '/' + 'ru-hexlet-io-courses.html'
            assert download(page_url, path=tmpdir) == expected


def test_download_file_exist():
    with requests_mock.Mocker() as m:
        page_url = 'http://ru.hexlet.io/courses/python-oop-basics'
        rss_url = 'https://ru.hexlet.io/lessons.rss'
        link_url = 'https://ru.hexlet.io/courses/python-oop-basics'
        html_content = 'tests/fixtures/ru-hexlet-io-courses-python-oop-basics.html'

        m.get(page_url, text=read(html_content))
        m.get(rss_url, text =read('tests/fixtures/ru-hexlet-io-lessons.rss'))
        m.get(link_url, text=read(html_content))

        with tempfile.TemporaryDirectory() as tmpdir:
            expected = tmpdir + '/' + 'ru-hexlet-io-courses-python-oop-basics.html'
            assert download(page_url, path=tmpdir) == expected
