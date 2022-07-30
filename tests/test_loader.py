import os.path
import tempfile
import requests_mock
from page_loader import download


def test_loader_content():
    with requests_mock.Mocker() as m:
        page_url = 'http://ru.hexlet.io/courses'
        m.get(page_url, text = 'example text')
        expected = 'ru-hexlet-io-courses.html'
        with tempfile.TemporaryDirectory() as tmpdir:
            assert download(page_url, path=tmpdir) == expected
            with open(os.path.join(tmpdir, expected)) as f:
                assert f.read() == 'example text'


def test_loader_filename():
    with requests_mock.Mocker() as m:
        page_url = 'http://ru.hexlet.io/courses'
        m.get(page_url, text = 'example text')
        expected = 'ru-hexlet-io-courses.html'
        with tempfile.TemporaryDirectory() as tmpdir:
            assert download(page_url, path=tmpdir) == expected
