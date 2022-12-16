# Write a simple lottery drawing program. The lottery drawing should consist of six different
# numbers between 1 and 48

from random import sample

num_list = [str(num + 1) for num in range(0, 48)]
output_list = sample(num_list, 6)
print(output_list)
print(' '.join(output_list))

# ['3', '24', '30', '14', '16', '32']
# 3 24 30 14 16 32
# ['35', '18', '26', '8', '20', '29']
# 35 18 26 8 20 29
# ['29', '5', '30', '6', '48', '39']
# 29 5 30 6 48 39