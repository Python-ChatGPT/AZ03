import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
# alpha=0.5 делает точки полупрозрачными, что может быть полезно для визуализации плотности точек.
plt.scatter(x, y, alpha=0.5)
plt.title('Диаграмма рассеяния')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()