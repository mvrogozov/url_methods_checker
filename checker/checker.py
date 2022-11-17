#! /usr/bin/python3
import argparse
import sys
import re
import requests


METHODS = {
    'get': requests.get,
    'post': requests.post,
    'put': requests.put,
    'patch': requests.patch,
    'options': requests.options,
    'delete': requests.delete,
    'head': requests.head
}


def check_urls(filename=''):

    url_regex = re.compile(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')

    result = {}
    try:
        with open(filename, 'r') as file:
            print('Please wait...')
            for line in file:
                url = url_regex.search(line)
                if url:
                    result[url.group()] = {}
                    for key, value in METHODS.items():
                        response = None
                        if line.startswith('http'):
                            try:
                                response = value(url.group())
                            except Exception:
                                pass
                        else:
                            try:
                                response = value(f'http://{url.group()}')
                            except Exception:
                                pass
                        if response:
                            if response.status_code != 405:
                                result[url.group()][key]=response.status_code
                else:
                    print(f'Строка "{line}" не является ссылкой')
    except FileNotFoundError:
        return('No such file or directory')
    return result


def main():
    parser = argparse.ArgumentParser(description='url file to check')
    parser.add_argument('filename', type=str, help='file contains urls')
    args = parser.parse_args()
    filename = args.filename
    print(check_urls(filename))


if __name__ == '__main__':
    main()
