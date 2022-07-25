def check_speed(speed):
    if speed < 70:
        print('Ok')
    else:
        increase = speed - 70
        print(f'Points: {increase / 5}')
        if (increase / 5) > 12:
            print('License suspended')


check_speed(120) #Points: 10.0
check_speed(150)
# Points: 16.0
# License suspended