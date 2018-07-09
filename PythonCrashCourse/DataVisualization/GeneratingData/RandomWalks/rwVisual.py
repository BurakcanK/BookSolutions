import matplotlib.pyplot as plt

from randomWalk import RandomWalk


# keep making new walks, as long as the program is active
while True:
    # make a random walk, and plot the points
    rw = RandomWalk(50000)
    rw.fillWalk()

    # set the size of the plotting window
    plt.figure(figsize=(10, 6))

    pointNumbers = list(range(rw.numPoints))

    plt.scatter(rw.xValues, rw.yValues, c=pointNumbers,
                cmap=plt.cm.Blues, edgecolors='none', s=1)

    # emphasize the first and last points
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.xValues[-1], rw.yValues[-1],
                c='red', edgecolors='none', s=50)

    # remove the axes
    plt.axis('off')

    plt.show()

    keepRunning = input("Make another walk ? (y/n): ")
    if keepRunning == 'n':
        break
