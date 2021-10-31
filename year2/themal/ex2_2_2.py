# load packages
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import random
import time


def SSE(X, Y):
    # Mean X and Y
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    # Total number of values
    n = len(X)
    numer = 0
    denom = 0
    for i in range(n):
        # method of least squares formula
        numer += (X[i] - mean_x) * (Y[i] - mean_y)
        denom += (X[i] - mean_x) ** 2
    m = numer / denom
    c = mean_y - (m * mean_x)

    # Printing coefficients
    print("Coefficients")
    print(m, c)
    return c, m

def plotting(c, m, X, Y):
    # Plotting Values and Regression Line

    max_x = np.max(X)
    min_x = np.min(X)

    print(max_x, min_x)
    # Calculating line values x and y
    # x = np.linspace(min_x, max_x, 10)
    plt.plot(X, Y, 'bo', color="red")

    # x = np.linspace(min_x, max_x, 1000)
    # plt.plot(x, 1 / x)

    # Ploting Line
    # plt.plot(x, y, color='#58b970', label='Regression Line')
    # Ploting Scatter Points


    plt.xlabel('Gas vol')
    plt.ylabel('Force')
    plt.legend()
    plt.show()


def main():
    # data measured in class (Oct 19, 2021)
    V = np.array([10, 9, 8, 7, 6, 5, 4, 3])  # Volume in mL
    M = np.array([0, 247, 444, 745, 1167, 1507, 2304, 3219])  # weight measured in grams
    c, m = SSE(V, M)
    plotting(c, m, V, M)


if __name__ == '__main__':
    main()