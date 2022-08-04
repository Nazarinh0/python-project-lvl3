### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nazarinh0/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/Nazarinh0/python-project-lvl3/actions)
### Code Climate:
[![Maintainability](https://api.codeclimate.com/v1/badges/aec025e1107b61dd06b9/maintainability)](https://codeclimate.com/github/Nazarinh0/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/aec025e1107b61dd06b9/test_coverage)](https://codeclimate.com/github/Nazarinh0/python-project-lvl3/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# Page-loader

Page-loader is web page downloader.

- The page is downloaded in html format.
- Content is downloaded only that which is located on the same domain.
- Can be used as CLI tool or library

## Installation and usage
### Install
`python3 -m pip install git+https://github.com/nazarinh0/python-project-lvl3`

### Use as a library
```
from page_loader import download

path_to_page = download(url, actual_path=os.getcwd())
print(path_to_page)
```

### Use as a CLI
```
usage: page-loader [options] <url>

description: web page downloader

positional arguments:
  url

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         output the version number
  -o [dir], --output [dir]
                        output dir (default: working directory)
```

### Logging

Logs are written to .page-loader-errors.log (this file creates in the working directory).
