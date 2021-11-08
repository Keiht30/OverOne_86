import random


# # home_13.8
#
# nums = [int(i) for i in input().split()]
#
#
# def sort_num(nums):
#     ls_positive = []
#     ls_zero = []
#     ls_negative = []
#     for num in nums:
#         num = int(num)
#         if num > 0:
#             ls_positive.append(num)
#         elif num == 0:
#             ls_zero.append(num)
#         else:
#             ls_negative.append(num)
#
#     return len(ls_negative), len(ls_zero), len(ls_positive)
#
#
# print(*sort_num(nums), sep='\n')

# home_13.9

# print(sum(([int(i) for i in input().split()])))

# list_numbers = [int(i) for i in input().split()]
# count = sum(map(lambda item: item, list_numbers))
# print(count)


# hometask_13.4

#
# def rand_num(min_n, max_n, count_n):
#     d = []
#     for i in range(count_n):
#         x = random.randrange(min_n, max_n)
#         d.append(x)
#     return d
#
#
# a = int(input('Введите кол-во чисел: '))
# b = int(input('Введите минимальное число: '))
# c = int(input('Введите максимальное число: '))
# rand_user = rand_num(count_n=a, min_n=b, max_n=c)
# print(rand_user)
#

# hometask_13.6

# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n - 1) * n
#
#
# print(fac(int(input())))

