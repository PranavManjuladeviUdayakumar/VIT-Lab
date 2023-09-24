import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


l0, l1 = [], []
print("Enter two numbers separated by a space in the form of 'x_value y_value' to store values or enter a blank input to start processing stored input")
while True:
    x = input("Input: ").lstrip().rstrip()
    if (x == '' or x == '/n'):
        if len(l0) < 2:
            print("Cannot proceed without storing atleast 2 pairs of data")
            pass
        else:
            print("\nProcessing...\n")
            break
    else:
        vals = x.split()
        if len(vals) != 2:
            print("Incorrect number of numbers entered")
        else:
            l0.append(float(vals[0]))
            l1.append(float(vals[1]))

x = np.array(l0).reshape((-1, 1))
y = np.array(l1)

model = LinearRegression().fit(x, y)
slope, intercept = float(model.coef_[0]), float(model.intercept_)
print(f"Slope: {slope}")
print(f"Equation: y = {slope}x + {intercept}")

plt.scatter(l0, l1)

points = []
for i in l0:
    points.append(slope*i + intercept)

plt.plot(l0, points)
plt.show()
