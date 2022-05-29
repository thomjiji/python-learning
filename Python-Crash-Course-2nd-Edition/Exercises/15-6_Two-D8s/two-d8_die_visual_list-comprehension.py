from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6
die_1, die_2 = Die(6), Die(6)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(10000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling two D8 1000 times.', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')