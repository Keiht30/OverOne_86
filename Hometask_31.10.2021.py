# # Hometask_13_3
#
# def get_even(lst, filter=None):
#     if filter is None:
#         return lst
#
#     res = []
#     for x in lst:
#         if filter(x):
#             res.append(x)
#
#     return res
#
#
# list_1 = [int(i) for i in input().split()]
# list_res = get_even(list_1, lambda x: x % 2 == 0)
#
# print(list_res)

# Hometask_13_1

#
# def sum_nambers(nums):
#     res = []
#     for num in nums:
#         sum_num = 0
#         while num != 0:
#             last = num % 10
#             sum_num += last
#             num = num // 10
#         res.append(sum_num)
#         res.sort()
#     return res
#
#
# list_1 = [int(i) for i in input().split()]
# list_res = sum_nambers(list_1)
# print(list_res)

# Hometask_13_2


def f(x):
    if x <= -2:
        return 1 - (x + 2) * (x + 2)
    elif -2 < x <= 2:
        return -x / 2
    else:
        return (x - 2) * (x - 2) + 1


d = f(float(input()))
print(d)
