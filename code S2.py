# удобное завершение программы
import sys
# простое и удобное время
import time
# элемент случайности
import random
# графический модуль
from tkinter import  *

# получает 4 числа. возвращает 1 число. Высчитывает расстояние между 2 точками на плоскости
def r(coord_x, coord_x2, coord_y, coord_y2):
    return ((coord_x - coord_x2) ** 2 + (coord_y - coord_y2) ** 2) ** 0.5

'''
    получает кооординаты (тела по рассматривемой оси, рассматриваемое тело по той же оси, аналогично для оставшийся оси), кол-во тел, начальные расстояние между ними и константу k
    возвращает силу по данной координате, с которой все тела действуют на выбранное (сила упругости)
'''

# расчет силы 
def count_f (coordS_first, our_coord_first, coordS_second, our_coord_second, n, array_r, k):
    sum_f = 0
    f = []
    # расчет суммарной силы
    for i in range(n):
        real_r = r(coordS_second[i], our_coord_second, coordS_first[i], our_coord_first)
        if (real_r != 0):
            f.append(k * (real_r - array_r[i]) * (our_coord_first - coordS_first[i]) / real_r)
            sum_f += f[len(f) - 1]
    return sum_f

#  получает старую скорость, ускорение и время. возвращает новую скорость
def count_v(old_v, a, time):
    return old_v + a * time

# получает силу и массу. возвращает ускорение
def count_a(f, m):
    return f / m

# получает скорость, старую координату и время. возвращает координату
def count_coord(start_coord, v, t):
    return v * t + start_coord

# создание холста

# ширина и длина холста
width_canvas = 1000
height_canvas = 1000

# холст
root = Tk()
canvas = Canvas(root, width = width_canvas, height = height_canvas, bg = "white")
canvas.pack()

# рисует точку по координатам и выводим координаты тела; получает х, у, номер тела для вывода и размер точки
def out(x, y, i, point_size):
    print("Тело номер %s имеет координаты" % i, x, 'и', y)
    canvas.create_oval(int(x + 1) - point_size, int(y + 1) - point_size, int(x + 1) + point_size, int(y + 1) + point_size, fill='black')


# автоматическое создание переменных

# сторона квадрата, образованного телами, четное
number_of_points_on_line = 6

# число тел
n = number_of_points_on_line * number_of_points_on_line

# массы
m = [-1] * n

# скорости по х
vx = [-1] * n

# скорости по у
vy = [-1] * n

# координаты
x = [-1] * n
y = [-1] * n

# промедуток между соседними телами
step = 10

# вспомогательная переменные
index = n - 1
# ввод нумерации в сетке
if (number_of_points_on_line % 2 == 1):
    helpvarx, helpvary = -(number_of_points_on_line // 2) * step, -(number_of_points_on_line // 2) * step
else:
    helpvarx, helpvary = -((number_of_points_on_line - 1) // 2) * step - step // 2, -((number_of_points_on_line - 1) // 2) * step - step // 2

start_helpvarx = helpvarx
# создание реальных значений для величин
while index >= 0:
    for j in range(number_of_points_on_line):
        x[index] = helpvarx
        y[index] = helpvary
        m[index] = 5
        vx[index] = 0
        vy[index] = 0
        index -= 1
        # проверка номера элемента
        if (index < 0):
            break

        x[index] = helpvarx * -1
        y[index] = helpvary * -1
        m[index] = 5
        vx[index] = 0
        vy[index] = 0
        index -= 1
        if (index < 0):
            break

        helpvarx += step
    helpvarx = start_helpvarx
    helpvary += step
    
# центрирование
for i in range(n):
    y[i] += height_canvas // 2
    x[i] += width_canvas // 2
array_r = [[-1] * n] * n

for i in range(0, n):
    
    for j in range(i, n):
        array_r[i][j] = r(x[i], x[j], y[i], y[j])
        array_r[j][i] = array_r[i][j]
    print(array_r[i])

# ускорения тел
ax = [-1] * n
ay = [-1] * n

# воздействия всех тел на рассматриваемое по оси х и у
fx = [-1] * (n - 1)
fy = [-1] * (n - 1)

# время между пересчетами
dt = 0.02

# время с начала работы модели
t = 0

# радиус точки на экране
point_size = 2

# константа K
k = 0.01


while t < 100:
    canvas.create_rectangle(0, 0, height_canvas, width_canvas, fill="white")

    
    for i in range(0, n):

        #вывод
        if (x[i] < 0 or y[i] < 0 or x[i] > width_canvas or y[i] > height_canvas):
            print("Выход за экран")
            sys.exit(0)
        out(x[i], y[i], i + 1, point_size)

        # пересчет значений по х для всех тел
        ax[i] = count_a(count_f(x, x[i], y, y[i], n, array_r[i], k), m[i])
        vx[i] = count_v(vx[i], ax[i], dt)
        x[i] = count_coord(x[i], vx[i], dt)

        # пересчет значений по у для всех тел
        ay[i] = count_a(count_f(y, y[i], x, x[i], n, array_r[i], k), m[i])
        vy[i] = count_v(vy[i], ay[i], dt)
        y[i] = count_coord(y[i], vy[i], dt)
    root.update()
    t += dt

root.mainloop()
