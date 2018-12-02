import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

x = [12, 13, 12, 15, 17]
y = [2, 4, 1, 5, 3]

plt.plot(x, label="x")
plt.plot(y, label="y")
plt.legend()
plt.show()