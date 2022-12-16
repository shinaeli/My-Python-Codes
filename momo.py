# import turtle
# wn = turtle.Screen()
# wn.bgcolor("pink")
# wn.title("Yo! Shine")
#
# momo = turtle.Turtle()
# momo.color("red")
# momo.pensize(5)
#
# momo.right(60)
# momo.left(30)
# momo.forward(90)
#
# wn.mainloop()

n = int(input('enter a number between 0 and 101: '))
if n % 2 != 0:
    print('Weird')
elif (n % 2 == 0) and (n in range(2, 6)):
    print('Not Weird')
elif (n % 2 == 0) and (n in range(6, 21)):
    print('Weird')
elif (n % 2 == 0) and (n in range(21, 101)):
    print('Not Weird')

n = int(input('enter a number: '))
for i in range(1, n):
    print(i * str(i))
# OR
n = int(input('enter a number: '))
for i in range(1, n):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((((10 ** i) - 1) // 9) * i
# OR
n = int(input('enter a number: '))
for i in range(1, n):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((i * (10 ** i)) // 9)
