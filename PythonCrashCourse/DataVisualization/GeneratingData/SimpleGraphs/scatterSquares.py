import matplotlib.pyplot as plt

xValues = list(range(1, 1001, 20))
yValues = [x**2 for x in xValues]

# -----------------------
# example of RGB coloring and just a 'red' color
# plt.scatter(xValues, yValues, c=(0, 0, 1), edgecolors='red', s=50)
# <<<<<<<<<<<<<<<<<<<<<<<
# using a color map
plt.scatter(xValues, yValues, c=yValues,
            cmap=plt.cm.Blues, edgecolors='none', s=50)
# -----------------------

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
plt.axis([0, 1100, 0, 1100000])

# save the plot and trim white spaces with bbox param
plt.savefig("squaresPlot.png", bbox_inches='tight')
