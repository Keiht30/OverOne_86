# 8_1

# city = {'Россия': 'Москва',
#         'Украина': 'Киев',
#         'Италия': 'Рим',
#         'Испания': 'Мадрид',
#         'Болгария': 'София'
#         }
# city_1 = input('Введите столицу какой страны вы хотите узнать: ').title()
# for key in city:
#     if key == city_1:
#         print(f'{city_1} - столица {city[key]}')
#
# city_1 = input('Введите столицу какой страны вы хотите узнать: ').title()
# for key in city:
#     if city[key] == city_1:
#         print(f'{city_1} является столицей {key}')
#  8_2

# a = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
#      8: 'eight', 9: 'nine',
#      10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
#      14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
#      20: 'twenty'}
# for key in range(len(a)):
#     if int(key) % 2 != 0:
#         del a[key]
# print(a)

# 8_2 вариант 2
# objects = [i for i in range((int(input('Введите первый ключ: '))), ((int(input('Введите последний ключ: '))) + 1))]
# categories = [(input('Введите значение ключа:').lower().split()) for i in range(len(objects))]
#
# a_dict = {key: value for key, value in zip(objects, categories)}
# for key in range(len(a_dict) + 1):
#     if key % 2 != 0:
#         del a_dict[key]
# print(a_dict)

# # 8_3 Задача!
# # Рита и Дина под впечетлениям после просмотра мультика Трям здрасте ! решили придумать никому не извесный язык (Тилимилитрямский) в котором  слова
# # перевернуты наоборот и в концы добовляется "трям" Необходимо написать программу  которая будет сначала создавать словарь
# # ключом которого будет слова на нашем языке, а значение -этоже слово на тилимилитрямском языке , далее  по слову введенному с клавиатуры на нашем
# # языке выдавать перевод на тилимилитрямский, если такого слова нет то вывести соответствующее сообщение
#
# n = [str(i) for i in input('Введите список слов  для создания словаря: ').lower().split()]
# tili_mili = [str(i[::-1]) + 'трям ' for i in n]
# dictionary_translation = {key: value for key, value in zip(n, tili_mili)}
# pi = input('Введите слово для поиска в словаре: ').lower()
# for key, value in dictionary_translation.items():
#     if key == pi:
#         print(value)
#         break
# else:
#     print('Такого слова в словаре нет, если хотите узнать перевод запишите слово в словарь')
