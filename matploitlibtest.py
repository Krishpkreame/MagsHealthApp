import matplotlib.pyplot as plt
fig, ax = plt.subplots(nrows=1, ncols=1)  # create figure & 1 axis
plt.style.use('dark_background')
ax.hist([0, 1, 2], [10, 20, 3])

fig.savefig('img/graph.png')   # save the figure to file
plt.close(fig)    # close the figure window
