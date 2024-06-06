import numpy as np
from tabulate import tabulate

# Функция для генерации случайных величин и вычисления статистик
def simulate_cosine_random_variable(N, q):
    # Генерация N значений из равномерного распределения на интервале (0, 1)
    u = np.random.uniform(0, 1, N)
    
    x = u**(1/4)
    mean = np.mean(x)
    variance = np.var(x)
    
    return x, mean, variance

# Точные значения среднего и дисперсии для f(x) = cos(x) на интервале (pi/2, 0)
exact_mean = 0.8
exact_variance = 0.0267

# Параметры
q = 15
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
