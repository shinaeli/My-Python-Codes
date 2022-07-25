def create_list(*args):
    output = []

    if len(args) > 0:
        for item in args:
            output.append(item)

        print(args)

    print(output)


create_list('3', '7', '10', '27', '12', '198', 'Mercy', 48, 'Lamide')

# ('3', '7', '10', '27', '12', '198', 'Mercy', 48, 'Lamide')
# ['3', '7', '10', '27', '12', '198', 'Mercy', 48, 'Lamide']