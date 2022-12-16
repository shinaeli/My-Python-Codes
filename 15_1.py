import matplotlib.pyplot as plotter

nums = range(1, 50001)
cubed = [num ** 3 for num in nums]

plotter.style.use('seaborn-dark')
fig, ax = plotter.subplots()
ax.set_title('Cube of Numbers', fontsize=15)
ax.set_xlabel('Numbers', fontsize=13)
ax.set_ylabel('Cubes', fontsize=13)
ax.tick_params(axis='both', labelsize=10)
ax.plot(nums, cubed, linewidth=5)

plotter.show()


# print(cubed)

