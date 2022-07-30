"""Main script"""
import argparse
from page_loader import download


def main():
    parser = argparse.ArgumentParser(
        description='Loads a page from url and saves it to HTML'
    )
    parser.add_argument('page_url')
    parser.add_argument(
        '--output',
        help='path to existing directory, in which HTML will be saved')
    args = parser.parse_args()
    print(download(args.page_url, args.output))


if __name__ == '__main__':
    main()
