import pygal

from die import Die

# create two D6 dice
die1 = Die()
die2 = Die()

# make some rolls and store the results in a list
results = list()
for rollNum in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# analyze the results
frequencies = list()
maxResult = die1.numSides + die2.numSides

for value in range(2, maxResult + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('diceVisual.svg')
