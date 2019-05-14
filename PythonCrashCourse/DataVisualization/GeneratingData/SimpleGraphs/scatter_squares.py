import matplotlib.pyplot as plt

x_values = list(range(1, 1001, 20))
y_values = [x**2 for x in x_values]

# -----------------------
# example of RGB coloring and just a "red" color
# plt.scatter(x_values, y_values, c=(0, 0, 1), edgecolors="red", s=50)
# <<<<<<<<<<<<<<<<<<<<<<<
# using a color map
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors="none", s=50)
# -----------------------

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)

# set size of tick labels
plt.tick_params(axis="both", which="major", labelsize=14)

# set the range for each axis
plt.axis([0, 1100, 0, 1100000])

# save the plot and trim white spaces with bbox param
plt.savefig("squares_plot.png", bbox_inches="tight")
