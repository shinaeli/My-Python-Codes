def show_stars(rows):
    if rows == 0:
        print('Invalid Input')
    else:
        for count in range (1, rows+1):
            print('*' * count)


show_stars(5)
show_stars(10)
show_stars(15)
show_stars(20)