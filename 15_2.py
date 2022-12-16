import matplotlib.pyplot as plotter

nums = range(1, 50001)
cubed = [num ** 3 for num in nums]

plotter.style.use('seaborn')
fig, ax = plotter.subplots()
ax.set_title('Cube of Numbers', fontsize=20)
ax.set_xlabel('Numbers', fontsize=13)
ax.set_ylabel('Cubes', fontsize=13)
ax.tick_params(axis='both', labelsize=10)
# ax.plot(nums, cubed, linewidth=5)
ax.scatter(nums, cubed, c=cubed, cmap=plotter.cm.viridis, s=20)

plotter.show()


# print(cubed)

