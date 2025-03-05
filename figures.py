import matplotlib.pyplot as plt
import random

# Данные для построения графика
#x = [1, 2, 3, 4, 5]
#y = [1, 3, 3, 7, 9]

# Генерируем список x из 4 случайных целых чисел от -5 до 5
x = [random.randint(-5, 5) for _ in range(4)]
y = [random.randint(-5, 5) for _ in range(4)]

# Добавляем первую точку в конец списка
x.append(x[0])
y.append(y[0])

# Построение графика с использованием plt.plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Ось така херня, малята')

# Добавление подписи осей и заголовка
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Пример графика с plt.plot")

# Отображение легенды
plt.legend()

# Вывод графика на экран
plt.show()



