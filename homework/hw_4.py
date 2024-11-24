import numpy as np
from bashplotlib.histogram import plot_hist
arr = np.random.normal(size=1000, loc=0, scale=1)
plot_hist(arr, bincount=50)

# bashplotlib — это пакет python и инструмент командной
# строки для создания базовых графиков в терминале.
# Это быстрый способ визуализации данных, когда у вас нет графического интерфейса