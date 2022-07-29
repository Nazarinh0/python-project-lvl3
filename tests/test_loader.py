import os.path

import requests_mock
from page_loader import download

def test_loader():
    with requests_mock.Mocker() as m:
        page_url = 'http://ru.hexlet.io/courses'
        m.get(page_url, text = 'example text')
        expected = 'ru-hexlet-io-courses.html'
        assert download(page_url) == expected
        with open(os.path.join(os.getcwd(), expected)) as f:
            assert f.read() == 'example text'
