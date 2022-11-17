from checker.checker import check_urls


def test_no_args():
    """Без передачи параметров."""
    result = check_urls()
    right_result = 'No such file or directory'
    assert result == right_result, (
        'Ошибка запуска без параметров.'
    )


def test_file():
    """Тестовый файл"""
    filename = 'fixture_file.txt'
    result = check_urls(filename)
    right_result = (
        {'https://stackoverflow.com/':
            {'get': 200,
             'post': 200,
             'put': 200,
             'patch': 200,
             'options': 200,
             'delete': 200,
             'head': 200},
         'www.avito.ru':
            {'head': 301},
         'strange_string.sd': {},
         'gmail.com':
            {'get': 200,
             'post': 200,
             'put': 200,
             'patch': 200,
             'options': 200,
             'delete': 200,
             'head': 301}
         }
    )
    assert result == right_result, (
        'Неправильный результат работы.'
    )
