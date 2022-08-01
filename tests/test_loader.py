import os.path
import tempfile
import requests_mock
from page_loader import download


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
