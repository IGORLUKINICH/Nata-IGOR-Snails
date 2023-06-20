# Snail Race (Бега улиток)

<img height="200" src="C:\Users\Игорь\Desktop\istockphoto-163838915-612x612.jpg" width="200"/>

### *Описание игры*
```
Вряд ли вы получите много адреналина от бегущих... 
улиток. Все улитки (изображаемые с помощью символа @ в качестве раковины 
и v в качестве двух глазных стебельков) медленно, но верно 
движутся к финишной прямой. В гонках может участвовать 
до восьми улиток, оставляющих позади определенный след слизи, каждая со 
своим, выбранным пользователем именем. 

```
### *Как играть?*
```
В начале игры указываем количество игроков, длину беговой дистанции, 
имена игроков , и запускается игра.
В соответствии с местом в гонке выбирается определенный след каждого участика гонки.
С помощью клавиш ПРОБЕЛ и W можно ускорять и замедлять прохождение участниками гонки.
Участники гонки передвигаються при прохождении трассы рандомно, 
также рандомно выбираються и возникающие на их пути препятствия
```
### Необходимые программы и модули

Для коректного запуска файла `NATA IGOR Snails.py` необходимо установить 
Python версии не ниже 3.10, также VS Code версии не ниже 1.79, 
еще модули PyLance, Keyboard.

Данная игра была протестирована на работоспособность на следующей платформе:
OS Windows 10 Pro 22H2, Python 3.11.2, VS Code 1.79.2, модули PyLance, Keyboard.

### Запуск игры

Файл`NATA IGOR Snails.py` запускается с помощью команды RUN в VS Code:

```
RUN `NATA IGOR Snails.py`
```
### Скрин игрового процесса

<img height="720" src="C:\Users\Игорь\Desktop\Игра на VS Code.jpg" width="900"/>

### Внесенные изменения
```
Видоизменили состояние улиток с помощью функции set_text_color(color), 
generate_random_color(), clear_screen() и display_snail(name, progress, color):
1. Добавили цвет в соответсвии с местом в гонке 
    - 1. Зелёный; 2.Жёлтый; 3.Синий; 4-8.Красный;

С помощью функции keyboard добавили ускорение по клавише "space"
Теперь можно нажать клавишу "Space" во время гонки, 
чтобы ускорить движение улиток. Обратить внимание, 
что кнопка "Space" работает только в активном окне консоли.

Использовали модуль 'time' для создания плавного движения
Это позволит улиткам перемещаться по трассе с плавным анимированным движением. 
Можно изменить задержку (time.sleep) для изменения скорости анимации.

Добавили поддержку ничьих на случай, если улитки достигнут финишной прямой одновременно.
```
### Основные функции работы приложения
```
 Функция для задания цвета текста в консоли (Windows):
def set_text_color(color):
    import ctypes
```
```
 Функция для генерации случайного цвета в соответствии с местом в гонке:
def generate_random_color(rank):
```
```
 Функция для отображения улитки с заданным цветом:
def display_snail(name, progress, color):
```
```
и многое другое
```