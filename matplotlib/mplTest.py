from matplotlib import pyplot as plt

x_vals = [1, 2, 3, 4]
y_vals = [5, 4, 6, 2]

plt.scatter(x_vals, y_vals)

other_x_vals = [1, 2, 3, 4]
other_y_vals = [4, 2, 3, 9]

plt.plot(other_x_vals, other_y_vals, color="red")

plt.title("sample plot")

plt.xlabel("x values")
plt.ylabel("y values")

plt.show()