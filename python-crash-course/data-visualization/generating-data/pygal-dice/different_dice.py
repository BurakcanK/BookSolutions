import pygal

from die import Die

# create a D6 and a D10
die1 = Die()
die2 = Die(10)

# make some rolls and store the results in a list
results = list()
for _ in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

# analyze the results
frequencies = list()
max_result = die1.num_sides + die2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = [str(i) for i in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file("different_dice.svg")
