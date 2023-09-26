import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


l0, l1 = [], []

print("Enter two numbers separated by a space in the form of 'x_value y_value' to store values or enter 'l' to use skl or 'm' to use lsm to start processing stored input")

while True:

    x = input("Input: ").lstrip().rstrip().lower()

    if x == 'l':
            
            if len(l0) < 2:
                print("Cannot proceed without storing atleast 2 pairs of data")
                pass

            print("\nProcessing via SciKit-Learn...\n")
            X = np.array(l0).reshape((-1, 1))
            Y = np.array(l1)

            model = LinearRegression().fit(X, Y)
            slope, intercept = float(model.coef_[0]), float(model.intercept_)
            break

    elif x == 'm':

        if len(l0) < 2:
                print("Cannot proceed without storing atleast 2 pairs of data")
                pass
        
        print("\nProcessing via Least Square Method...\n")
        meanx = sum(l0)/len(l0)
        meany = sum(l1)/len(l1)

        num = 0
        den = 0

        for i in range(len(l0)):
            num += (l0[i] - meanx) * (l1[i] - meany)
            den += (l0[i] - meanx) ** 2
        
        slope = num/den
        intercept = meany - slope*meanx
        break

    else:

        vals = x.split()

        if len(vals) != 2:

            print("Incorrect number of numbers entered")

        else:

            l0.append(float(vals[0]))
            l1.append(float(vals[1]))


print(f"Slope: {slope}")
print(f"Equation: y = {slope}x + {intercept}")

plt.scatter(l0, l1)

points = []

for i in l0:

    points.append(slope*i + intercept)

plt.plot(l0, points)
plt.show()