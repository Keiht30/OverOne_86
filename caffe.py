import pyttsx3
import math

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)


pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}
menu = []
for key in pastry.keys():
    menu.append(key)
# engine.say(f'Добрый день! Рады видеть  Вас в кондитерской "Кренделёк" сегодня у нас в меню  торт {menu}')
# engine.say('''Если вы хотите услышать состав торта , введите 1
# Уточнить стоимость  - введите 2
# уточнить остаток    - введите 3
# Уточнить  всю информацию - введите 4
# Если вы хотите приобрести торт, введите 5
# Для выхода из программы введите 0''')
# engine.runAndWait()
choice = int(input('Сделайте ваш выбор: '))
if choice == 0:
    engine.say(f'Будем рады видеть Вас в кондитерской "Кренделёк"!')
    engine.runAndWait()
    exit()
cake = input('Какой торт Вас интересует? ')
for k, v in pastry.items():
    if cake == k and choice == 1:
        engine.say(f'Торт {cake} состоит из {v[0]}')
        engine.runAndWait()
        amount = int(input('Какой вес  торта Вы хотите приобрести: '))
        if amount <= v[2]:
            total = amount * v[1] / 100
            total_1 = int(total)
            total_2 = (math.floor(total * 100) % 100)
            engine.say(f"С вас к оплате {total_1} рублей {total_2} копеек , спасибо за покупку!")
            engine.runAndWait()
            engine.say(f'торта осталось {v[2] - amount} грамм')
            engine.runAndWait()
        else:
            engine.say(
                f'К сожалению торта {cake} нет в таком количестве, остаток на данный момент составляет {v[2]} грамм')
            engine.runAndWait()
    elif cake == k and choice == 2:
        engine.say(f'Стоимость торта  {cake} составит {v[1]} рублей за 100 грамм')
        engine.runAndWait()
        amount = int(input('Какой вес  торта Вы хотите приобрести: '))
        if amount <= v[2]:
            total = amount * v[1] / 100
            total_1 = int(total)
            total_2 = (math.floor(total * 100) % 100)
            engine.say(f"С вас к оплате {total_1} рублей {total_2} копеек , спасибо за покупку!")
            engine.runAndWait()
            engine.say(f'торта осталось {v[2] - amount} грамм')
            engine.runAndWait()
        else:
            engine.say(
                f'К сожалению торта {cake} нет в таком количестве, остаток на данный момент составляет {v[2]} грамм')
            engine.runAndWait()
    elif cake == k and choice == 3:
        engine.say(f'На данный момент торта  {cake} осталось {v[2]} грамм')
        engine.runAndWait()
        amount = int(input('Какой вес  торта Вы хотите приобрести: '))
        if amount <= v[2]:
            total = amount * v[1] / 100
            total_1 = int(total)
            total_2 = (math.floor(total * 100) % 100)
            engine.say(f"С вас к оплате {total_1} рублей {total_2} копеек , спасибо за покупку!")
            engine.runAndWait()
            engine.say(f'торта осталось {v[2] - amount} грамм')
            engine.runAndWait()
        else:
            engine.say(
                f'К сожалению торта {cake} нет в таком количестве, остаток на данный момент составляет {v[2]} грамм')
            engine.runAndWait()
    elif cake == k and choice == 4:
        engine.say(f'Торт {cake} состоит из {v[0]}')
        engine.say(f'Стоимость торта  {cake} за 100 грамм составит  {v[1]} рублей')
        engine.say(f'На данный момент торта  {cake} осталось {v[2]} грамм')
        engine.runAndWait()
        amount = int(input('Какой вес  торта Вы хотите приобрести: '))
        if amount <= v[2]:
            total = amount * v[1] / 100
            total_1 = int(total)
            total_2 = (math.floor(total * 100) % 100)
            engine.say(f"С вас к оплате {total_1} рублей {total_2} копеек , спасибо за покупку!")
            engine.runAndWait()
            engine.say(f'торта осталось {v[2] - amount} грамм')
            engine.runAndWait()
        else:
            engine.say(
                f'К сожалению торта {cake} нет в таком количестве, остаток на данный момент составляет {v[2]} грамм')
            engine.runAndWait()
    elif cake == k and choice == 5:
        amount = int(input('Какой вес  торта Вы хотите приобрести: '))
        if amount <= v[2]:
            total = amount * v[1] / 100
            total_1 = int(total)
            total_2 = (math.floor(total * 100) % 100)
            engine.say(f"С вас к оплате {total_1} рублей {total_2} копеек , спасибо за покупку!")
            engine.runAndWait()
            engine.say(f'торта осталось {v[2] - amount} грамм')
            engine.runAndWait()
        else:
            engine.say(
                f'К сожалению торта {cake} нет в таком количестве, остаток на данный момент составляет {v[2]} грамм')
            engine.runAndWait()

