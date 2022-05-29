import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the simulated path of pollen grain in the walk
plt.style.use('seaborn-colorblind')
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth=1)

plt.show()