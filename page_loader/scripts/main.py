"""Main script"""
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Loads a page from url and saves it to HTML'
    )
    parser.add_argument('page_url')
    parser.add_argument(
        '--output',
        help='path to existing directory, in which HTML will be saved')
    args = parser.parse_args()

if __name__ == '__main__':
    main()