import random
# 'random.random()' is used to generate random numbers mainly between '0' ad '1'
print(random.random())

for iterator in range(5):
    # 'randint()' is used to generate a random integer from a range of numbers
    # it accepts only two arguments which are mainly the lower and upper bound of range of numbers to be generated
    outcome = random.randint(1, 6)
    print(outcome)

# 'random.choice()' is used to randomly select an item from a list
# it accepts only the list as its argument
names_of_aspirants = ['James', 'Tobi', 'Dija', 'George', 'Philemon', 'Joyce']
print(random.choice(names_of_aspirants))