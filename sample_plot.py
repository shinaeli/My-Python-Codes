import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
savings = [1200, 1320, 1537, 2055, 2500, 1679, 3000, 3320, 3618, 2845, 2513, 3440]

# plt.style.available
plt.style.use('seaborn-dark')

fig, ax = plt.subplots()
# ax.plot(savings, months, linewidth=4)
#
# ax.set_title('A Savings Data', fontsize=14)
# ax.set_xlabel('Month', fontsize=15)
# ax.set_ylabel('Monthly Savings', fontsize=15)
# ax.tick_params(axis='both', labelsize=13)
# 'scatter' method is used to plot individual points or co-ordinates
# ax.scatter(2, 4, s=200)
# ax.scatter(months, savings, s=100)
# ax.scatter(months, savings, c='yellow', s=100)
# ax.scatter(months, savings, c=(0, 1, 0.6), s=100)
ax.scatter(months, savings, c=savings, cmap=plt.cm.Reds, s=100)

plt.show()
# plt.saveFig('no_whitespaces_monthly_saving.png', bbox_inches='tight')
# plt.saveFig('monthly_savings.png')