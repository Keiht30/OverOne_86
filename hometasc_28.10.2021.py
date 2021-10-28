# Вариант  № 1


def calculat_num(num, action, num1):
	if action == '+':
		return num + num1
	elif action == '-':
		return num - num1
	elif action == '*':
		return num * num1
	elif action == "**":
		return num ** num1
	elif action == "%":
		return (num * num1) / 100.0
	elif action == '/' and num1 != 0:
		return num / num1
	else:
		print("На 0 делить нельзя!")


a = int(input('Введите первое число: '))
b = input('Выберите действие,\n добавление + \n вычитание - \n '
          'умножение *\n найти процент от числа % \n деление / \n возведение в степень ** :  ')
c = int(input('Введите второе число: '))

print(calculat_num(num=a, action=b, num1=c))

# Вариант № 2

# def sum_num(num, num1):
# 	return num + num1
#
#
# def subtraction_num(num, num1):
# 	return num - num1
#
#
# def multiplication_num(num, num1):
# 	return num * num1
#
#
# def division_num(num, num1):
# 	if num1 != 0:
# 		return (num / num1)
# 	else:
# 		return ('На 0 делить нельзя!')
#
#
# def percentage_of_the_num(num, num1):
# 	return (num * num1) / 100.0
#
#
# def exponentiation_num(num, num1):
# 	return num ** num1
#
#
# print(f'Сумма чисел равна = ', sum_num(int(input("Введите слагаемое: ")), int(input("Введите слагаемое: "))))
# print(f'Разность чисел равна = ',
#       subtraction_num(int(input("Введите уменьшаемое: ")), int(input("Введите вычитаемое: "))))
# print(f'Произведение чисел равно =',
#       multiplication_num(int(input("Введите первый множитель : ")), int(input("Введите второй множитель: "))))
# print(division_num(int(input("Введите делимое : ")), int(input("Введите делитель: "))))
# print(f'Процент от числа равнен = ',
#       percentage_of_the_num(int(input("Введите первое число : ")), int(input("Введите второе число : "))))
# print(exponentiation_num(int(input("Введите число: ")), int(input("Введите степень : "))))
