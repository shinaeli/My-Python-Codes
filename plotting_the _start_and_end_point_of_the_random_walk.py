import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots()
    # 'point_number' is a list of points which the 'cmap' method follows in displaying the magnitude of each point
    point_numbers = range(rw.num_points)
    # Plotting the points produced between the start and end points
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    # Plotting the starting point which has a co-ordinate of (0,0)
    ax.scatter(0, 0, c='red', edgecolors='none', s=100)
    # Plotting the final point which has a co-ordinate of (rw.x_values[-1], rw.y_values[-1])
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', edgecolors='none', s=100)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break