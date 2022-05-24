import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

"""
`subplots()` function can generate one or more plots in the same figure.

The variable `fig` represents the entire figure or collection of plots. The variable ax represents the single plot in the
figure.

The variable `ax` represents the single plot in the figure.

`plot()` method will try to plot the data it's given in a meaningful way.
"""

plt.style.use('seaborn-colorblind')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick label
ax.tick_params(axis='both', labelsize=14)

plt.show()