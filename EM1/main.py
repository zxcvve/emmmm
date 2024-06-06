import numpy as np
from tabulate import tabulate

# Функция для генерации случайных величин и вычисления статистик
def simulate_cosine_random_variable(N, q):
    # Генерация N значений из равномерного распределения на интервале (0, 1)
    u = np.random.uniform(0, 1, N)
    
    # Преобразование значений с использованием обратной функции f(x) = cos(x)
    # f^(-1)(y) = arccos(y)
    # Поскольку f(x) определена на интервале (pi/2, 0), ее значения (cos(x)) будут на интервале (0, 1)
    # x = np.arccos(u * np.cos(0))
    x = np.sin(u)
    # x = u**4
    
    # Вычисление среднего и дисперсии
    mean = np.mean(x)
    variance = np.var(x)
    
    return x, mean, variance

# Точные значения среднего и дисперсии для f(x) = cos(x) на интервале (pi/2, 0)
exact_mean = exact_mean = 1 - np.cos(1)

sin_1 = np.sin(1)
cos_1 = np.cos(1)

exact_variance = (1 / (1 - 0)) * ((sin_1 - exact_mean)**2)


# Параметры
q = 14
N_values = [1, 250, 500, 1000]

# Список для хранения результатов
results = []

# Симуляция для каждого значения N
for N in N_values:
    if N == 0:
        # Для N = 0, просто добавляем нули в список результатов
        results.append([N, '', '', '', '', '', ''])
    else:
        x, mean, variance = simulate_cosine_random_variable(N, q)
        delta_mean = abs(exact_mean - mean)
        delta_variance = abs(exact_variance - variance)
        results.append([N, exact_mean, mean, delta_mean, exact_variance, variance, delta_variance])

# Вывод результатов в виде таблицы
headers = ["N", "Exact Mean", "Mean", "Delta1", "Exact Variance", "Variance", "Delta 2"]
print(tabulate(results, headers=headers, tablefmt="grid"))
