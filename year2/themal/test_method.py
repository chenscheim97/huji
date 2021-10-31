import matplotlib.pyplot as plt
import numpy as np


def dis_sum(k, n):
    return sum([(M[i] - (k * 1) / V[i] + n) ** 2 for i in range(len(V))])


# data measured in class (Oct 19, 2021)
W = [0, 247, 444, 745, 1167, 1507, 2304, 3219]  # Wight measurement
D = [10, 9, 8, 7, 6, 5, 4, 3]  # piston bar (density)

V = np.array(D)  # crating vector
M = np.array([x * 9.8 / 1000 for x in W])  # unit transfer and vector representation

# plotting measurements results
plt.figure("Measuring P and V")
plt.plot(M, V, "o")
plt.xlabel("mass (gr)")
plt.ylabel("volume (mL)")

# Plot results
results = [k for k in range(0, 500)]
best = 10 ** 9
final_k = 0
final_n = 0

for k in results:
    for n in range(10, 200):
        r = dis_sum(k, n / 10)
        if r < best:
            print(k, n / 10, r)
            best = r
            final_k = k
            final_n = n / 10

plt.plot([final_k * 1 / (i / 100) - final_n for i in range(200, 1200)], [(i / 100) for i in range(200, 1200)])
plt.grid(linewidth=1)
plt.show()
