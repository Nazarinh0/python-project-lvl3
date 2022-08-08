import os


def test_entrypoint():
    exit_status = os.system('page-loader --help')
    assert exit_status == 0