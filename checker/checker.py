#! /usr/bin/python3
import argparse
import re

import requests
import threading

METHODS = {
    'get': requests.get,
    'post': requests.post,
    'put': requests.put,
    'patch': requests.patch,
    'options': requests.options,
    'delete': requests.delete,
    'head': requests.head
}

result = {}


def func_threads(url):
    checking_threads = []
    for name, method in METHODS.items():
        checking_thread = threading.Thread(
            target=check_url, args=(url, name, method)
        )
        checking_threads.append(checking_thread)
        checking_thread.start()
    for thread in checking_threads:
        thread.join()


def check_url(url, name, method):
    result[url] = {}
    response = None
    if url.startswith('http'):
        try:
            response = method(url)
        except Exception:
            pass
    else:
        try:
            response = method(f'http://{url}')
            result[url][name] = response.status_code
        except Exception:
            pass
    if response:
        if response.status_code != 405:
            result[url][name] = response.status_code


def check_in_thread(filename=''):
    url_regex = re.compile(
        r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}'
        r'([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'
    )
    try:
        with open(filename, 'r') as file:
            print('Please wait...')
            for line in file:
                url = url_regex.search(line)
                if url:
                    func_threads(url.group())
                else:
                    print(f'Строка "{line}" не является ссылкой')
    except FileNotFoundError:
        return('No such file or directory')
    sorted_result = sort_result(result)
    return sorted_result


def sort_result(result):
    new_result = {}
    for key, value in result.items():
        value = dict(sorted(value.items()))
        new_result[key] = value
    return new_result


def main():
    parser = argparse.ArgumentParser(description='url file to check')
    parser.add_argument('filename', type=str, help='file contains urls')
    args = parser.parse_args()
    filename = args.filename
    print(check_in_thread(filename))


if __name__ == '__main__':
    main()
