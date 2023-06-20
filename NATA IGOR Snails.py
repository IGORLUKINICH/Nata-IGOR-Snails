import random    # импортируем модули
import time
import sys
import keyboard
import ctypes

# Задаем константы:
MAX_NUM_SNAILS = 8    # максимум количества участников
MAX_NAME_LENGTH = 20  # максимум длины имени участника,отображаемого в игре
FINISH_LINE = 60      # длина игрового поля между линиями START-ом и FINISH-ем

print('''Snail Race, by Al Sweigart al@inventwithpython.com        

@_-' <— snail

''')                  # выводим на экран название игры 


# Функция для задания цвета текста в консоли (Windows), для её работы используем модуль ctypes 
def set_text_color(color): 
    import ctypes           

    STD_OUTPUT_HANDLE = -11
    ctypes.windll.kernel32.SetConsoleTextAttribute(
        ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE), color
    )                                

# Функция для генерации случайного цвета в соответствии с местом в гонке:
def generate_random_color(rank):  
    if rank == 1:
        return 10  # Зеленый
    elif rank == 2:
        return 14  # Желтый
    elif rank == 3:
        return 11  # Синий
    else:
        return 12  # Красный


# Функция для очистки экрана работает с помощью модуля OS, предназначенного для работы с операционной системой
def clear_screen():
    import os

    os.system("cls" if os.name == "nt" else "clear")    # это команда очистки консоли 


# Функция для отображения улитки с заданным цветом:
def display_snail(name, progress, color):               # здесь присваивается имя, движение, цвет улитки
    spaces = progress
    set_text_color(color)
    print((" " * spaces) + name[:MAX_NAME_LENGTH])      # выводиться на экран начало движения и имя улитки
    print(("." * progress) + "@_-' ")                   # выводиться на экран путь (в цвете) перемещения улитки
    set_text_color(7)                                   # Возвращаем стандартный белый цвет текста


# Генерация случайных препятствий:
def generate_obstacles(finish_line):
    obstacles = []                                                   # сгенерированный список препятствий
    for _ in range(5):                                              # Генерируем 5 раз выбор препятствий
        obstacle_type = random.choice(["rock", "puddle", "stump"])  # рандомно по одному случаю извлекаем препятствия для движения улитки
    obstacle_position = random.randint(5, finish_line - 5)          
    obstacles.append((obstacle_type, obstacle_position))            # добавляем все препятствия в список
    return obstacles                                                # возвращаем список препятсвий


# Спрашиваем, сколько улиток должно участвовать в бегах:
while True:                                                         
    # Спрашиваем снова, пока игрок не введет число.
    print("How many snails will race? Max:", MAX_NUM_SNAILS)        
    response = input("> ")                                          # Пользователь вводит количество участников
    if response.isdecimal():                                        # Метод возвращает True если введенные числа - десятичные
        numSnailsRacing = int(response)                             # Присваиваем номер позиции участника 
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print("Enter a number between 2 and", MAX_NUM_SNAILS)           

# Спрашиваем длину трассы:
while True:
    print("Enter the length of the track:")                         
    response = input("> ")                                          # Пользователь вводит длину трассы
    if response.isdecimal():                                        # Метод возвращает True если введенные числа - десятичные
        track_length = int(response)
    if track_length > 0:                                            # Длинна может быть целочисленной больше 0
        break
    print("Please enter a positive integer.")

FINISH_LINE = track_length                                           # Обновляем длину финишной прямой
obstacles = generate_obstacles(FINISH_LINE)                           # Обновляем препятствия

# Ввод имен всех улиток:
snailNames = []  # Список имен улиток в виде строковых значений.
for i in range(1, numSnailsRacing + 1):                             # 
    while True:
        # Продолжаем спрашивать, пока игрок не введет допустимое имя.
        print("Enter snail #" + str(i) + "'s name:")                 # Ввод  имени участника
        name = input("> ")
        if len(name) == 0:                                           # Обработка ошибки по проверки правильности ввода имени
            print("Please enter a name.")
        elif name in snailNames:
            print("Choose a name that has not already been used.")
        else:
            break  # Введено приемлемое имя.
    snailNames.append(name)                                          # добавляем имя улитки в список участников

# Отображаем всех улиток на старте и игровое поле.
print("\n" * 1)  # ширина пробела между строкой ввода имени конечной улитки и строки START - FINICH
time.sleep(1)    # Пауза перед словами На старт!
print("                       На старт!")
time.sleep(1)    # Пауза перед словами Внимание!
print("                       Внимание!")
time.sleep(1)    # Пауза перед словами Марш!
print("                         Марш!")
time.sleep(2)    # Пауза перед началом запуска игры
print("START" + (" " * (FINISH_LINE - len("START")) + "FINISH"))                 
print("|>" + (" " * (FINISH_LINE - len("|")) + "|>"))
print("|>" + "                                                           " + "|>")
print("|" + "                                                            " + "|")
snailProgress = {}               # -  это ассоциативный массив, ключами которого служат имена улиток, 
                                #а значения представляют собой целые числа, показывающие, сколько знако-мест 
                                #проползла каждая улитка.                            
for snailName in snailNames:
    display_snail(snailName, 0, generate_random_color(1))      # Для имени улитки генерируем цвет 
    snailProgress[snailName] = 0

# time.sleep(1)  # Пауза перед началом гонок.

accelerate = True  # Флаг ускорения
pause = True  # Флаг паузы

while True:  # Основной цикл программы.
    # Выбираем случайным образом, каких улиток двигать вперед:
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

    # Проверяем, не достигли ли улитки финишной прямой при движении случайным образом:
    winners = []                                           # список победителей
    for snailName in snailNames:
        if snailProgress[snailName] == FINISH_LINE:
            winners.append(snailName)                      # добавление в список победителей

    if len(winners) > 0:                                   # проверка длинны пройденной трассы участником
        clear_screen()
        for snailName in winners:                          # цикл выявления победителя
            display_snail(snailName, FINISH_LINE, generate_random_color(1))  # Зеленый цвет для победителей
            print(snailName, "has won!")
        sys.exit()                  

    time.sleep(0.1)  # Задержка между шагами для создания плавного движения.


    # Проверяем, встречается ли препятствие на пути улитки:
    for snailName in snailNames:                                
        for obstacle_type, obstacle_position in obstacles:        
            if snailProgress[snailName] == obstacle_position:
                if obstacle_type == "rock":
                    snailProgress[snailName] -= 3  # Улитка останавливается на 3 шага назад
                elif obstacle_type == "puddle":
                    snailProgress[snailName] -= 1  # Улитка останавливается на 1 шаг назад
                elif obstacle_type == "stump":
                    snailProgress[snailName] -= 2  # Улитка останавливается на 2 шага назад

    # Если флаг ускорения установлен, двигаем улитки еще быстрее.
    if accelerate:
        for i in range(random.randint(1, numSnailsRacing // 2)):  
            randomSnailName = random.choice(snailNames)
            snailProgress[randomSnailName] += 1

    # Проверяем, не достигла ли улитка финишной прямой при ускорении:
    winners = []                                               # список победителей
    for snailName in snailNames:
        if snailProgress[snailName] == FINISH_LINE:
            winners.append(snailName)                          # добавление в список победителей

    if len(winners) > 0:                                       # проверка длинны пройденной трассы участником
        clear_screen()
        for snailName in winners:
            display_snail(
                                    snailName, FINISH_LINE, generate_random_color(1)
                )  # Зеленый цвет для победителей
            print(snailName, "has won!")
            sys.exit()

    # Обработка нажатия клавиши "Space" для ускорения гонки:
    if keyboard.is_pressed("space"):
        accelerate = True

    # Обработка нажатия клавиши "-" для паузы гонки:
    if keyboard.is_pressed("W"):
        pause = True

    #clear_screen()

    # Отображает стартовую и финишную прямые(Во время игового процесса):
    print("START" + (" " * (FINISH_LINE - len("START")) + "FINISH"))
    print("|>" + (" " * (FINISH_LINE - 1) + "|>"))
    print("|>" + "          Кто быстрей ?! - ЖМИ Пробел чтобы ускориться     " + "|>")
    print("|>" + "         Хочешь медленней ?! - ЖМИ 'W'чтобы замедлиться    " + "|>")
    print("|" + "                                                            " + "|")

    # Отображает улиток (с метками имен)
    sorted_snailNames = sorted(
        snailNames, key=lambda x: snailProgress[x], reverse=True  
    )  # Сортировка улиток по прогрессу 
    for i, snailName in enumerate(sorted_snailNames):
        display_snail(snailName, snailProgress[snailName], generate_random_color(i + 1))
 


