from checker.checker import check_in_thread, sort_result


def test_no_args():
    """Без передачи параметров."""
    result = check_in_thread()
    right_result = 'No such file or directory'
    assert result == right_result, (
        'Ошибка запуска без параметров.'
    )


def test_file():
    """Тестовый файл"""
    filename = 'fixture_file.txt'
    result = check_in_thread(filename)
    right_result = (
        {'https://stackoverflow.com/':
            {
             'delete': 200,
             'get': 200,
             'head': 200,
             'options': 200,
             'patch': 200,
             'post': 200,
             'put': 200,
             },
         'www.avito.ru':
            {
             'delete': 403,
             'get': 403,
             'head': 301,
             'options': 403,
             'patch': 403,
             'post': 403,
             'put': 403,
             },
         'strange_string.sd': {},
         'gmail.com':
            {
             'delete': 200,
             'get': 200,
             'head': 301,
             'options': 200,
             'patch': 200,
             'post': 200,
             'put': 200,
             }
         }
    )
    assert result == right_result, (
        'Неправильный результат работы.'
    )


def test_sort_result():
    test_dict = {
        'aaa': {'v': 4, 'z': 1, 'a': 3},
        'abb': {'d': 14, 'gz': 21, 'ga': 3}
    }
    right_result = {
        'aaa': {'a': 3, 'v': 4, 'z': 1},
        'abb': {'d': 14, 'ga': 3, 'gz': 21}
    }
    result = sort_result(test_dict)
    assert result == right_result
