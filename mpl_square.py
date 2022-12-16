import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
# ax.plot(squares)

# ax.plot(squares, linewidth=3)
ax.plot(input_values, squares, linewidth=3)
ax.set_title('Squares of Numbers', fontsize=14)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Square of Values', fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()
