from random import choice


class RandomWalk():
    """ A class to generate random walks. """

    def __init__(self, numPoints=5000):
        """ Initialize attributes of a walk. """
        self.numPoints = numPoints

        # all walks start at (0, 0)
        self.xValues = [0]
        self.yValues = [0]

    def fillWalk(self):
        """ Calculate all the points in the walk. """

        # keep taking steps until the walk reaches the desired length
        while len(self.xValues) < self.numPoints:
            # decide which direction to go and how far to go in that direction
            xDirection = choice([1, -1])
            xDistance = choice([0, 1, 2, 3, 4])
            xStep = xDirection * xDistance

            yDirection = choice([1, -1])
            yDistance = choice([0, 1, 2, 3, 4])
            yStep = yDirection * yDistance

            # reject moves that go nowhere
            if xStep == 0 and yStep == 0:
                continue

            # calculate the next x and y values
            nextX = self.xValues[-1] + xStep
            nextY = self.yValues[-1] + yStep

            self.xValues.append(nextX)
            self.yValues.append(nextY)
