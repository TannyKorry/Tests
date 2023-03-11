from pprint import pprint

######################  Задача 1  ######################
# 'Дан список с визитами по городам и странам. Напишите код, который возвращает'
# 'отфильтрованный список geo_logs, содержащий только визиты из России.'


def filtr_geo_logs():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    res = []
    for visits in geo_logs:
        for country in visits.values():
            if 'Россия' in country:
                res.append(visits)
    return res


######################  Задача 2  ######################
# Выведите на экран все уникальные гео-ID из значений словаря ids. Т. е. список вида [213, 15, 54, 119, 98, 35]


def create_list():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    user_list = []
    user_set = set()
    for users in ids.values():
        user_set |= set(users)
        user_list = list(user_set)
    return user_list


######################  Задача 3  ######################

# Дан список поисковых запросов. Получить распределение количества слов в них.
# Т. е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.


def count_word_requests():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
    count_dict = {}
    res = {}
    for text in queries:
        word_count = len(text.split())
        if word_count in count_dict:
            count_dict[word_count] += 1
        else:
            count_dict[word_count] = 1
    for word_count, quantity_queries in count_dict.items():
        res[word_count] = (str(round(quantity_queries / len(queries) * 100)) + '%')
    return res


######################  Задача 4  ######################

# Дана статистика рекламных каналов по объемам продаж. Напишите скрипт, который возвращает название канала с
# максимальным объемом. Т.е. в данном примере скрипт должен возвращать 'yandex'.


def unpack_dict():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    stats_list = list(stats.items())
    name_sales = max(stats_list, key=lambda i: i[1])
    return name_sales[0]


######################  Задача 5  ######################

# Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100]
# (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}


def convert_list_to_dicts():
    random_list = ['2018-01-01', 'yandex', 'cpc', 100]
    interim_dict = {}
    final_dict = {}
    value = random_list[-1]
    for key in random_list[-2::-1]:
        interim_dict[key] = value
        value = interim_dict
        final_dict = interim_dict
        interim_dict = {}
    return final_dict


if __name__ == '__main__':
    print('\n')
    pprint(filtr_geo_logs())
    print(f'\n{create_list()}\n')
    print(f'\n{count_word_requests()}\n')
    print(f'{unpack_dict()}\n')
    print(convert_list_to_dicts())
