from cProfile import label
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
x = np.linspace(0, 2, 100)  # Sample data.
arr = []
def sum_of_n_init(n):
    a = 0
    for i in range(1, n+1):
        # arr.append(i)
        arr.append(i)
        a = a + i
        print("Quando o i é " + str(i) + " o acumulador é = " + str(a))
        print(arr)
    return a

sum_of_n_init(10)

ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.plot(arr, arr, label='atv marise')
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend();  # Add a legend.

# arr.sort()
# print(arr)
# plt.plot(arr)
# plt.ylabel('f(n)')

plt.show()