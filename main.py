import random

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# x = list(range(0, 100))
# y = []
# for i in range(100):
#     n = random.randint(1, 100)
#     y.append(n)
x = []
y = []
for i in range(50):
    n = random.randint(1, 50)
    x.append(n)

for x_point in x:
    y.append(0.5*x_point+3.2)

mean_x = np.mean(x)
mean_y = np.mean(y)

x_minus_mean = []
y_minus_mean = []
x_minus_mean_squared = []
y_minus_mean_squared = []
x_multiply_y = []

data_size = len(x)

for x_value in x:
    new = x_value - mean_x
    x_minus_mean.append(new)
    x_minus_mean_squared.append(new**2)
for y_value in y:
    new = y_value - mean_y
    y_minus_mean.append(new)
    y_minus_mean_squared.append(new**2)
for i in range(data_size):
    x_multiply_y.append(x_minus_mean[i] * y_minus_mean[i])

denominator = sum(x_minus_mean_squared)
numerator = sum(x_multiply_y)

m = numerator / denominator
b = abs((m) * mean_x - mean_y)

predicted = []
predicted_minus_y = []
predicted_minus_y_squared = []
for i in range(data_size):
    x_value = x[i]
    prediction = (m * x_value) + b
    predicted.append(prediction)
    minus_y = prediction - y[i]
    predicted_minus_y.append(minus_y)
    predicted_minus_y_squared.append(minus_y**2)


prediction_denominator = sum(y_minus_mean_squared)
preidction_numerator = sum(predicted_minus_y_squared)

r_squared = preidction_numerator/prediction_denominator

#plot
max_x = np.max(x) + 100
min_x = np.min(y) - 100

plot_x = np.linspace(min_x, max_x, 100)
plot_y = float(b) + m * plot_x
plt.plot(plot_x, plot_y, label="Regression Line")
plt.scatter(x, y)
plt.legend()
plt.show()
print(r_squared)













