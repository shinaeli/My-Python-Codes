with open('learning_python.txt') as learning_python_object:
    all_lines = learning_python_object.readlines()

    for each_line in all_lines:
        output = each_line.replace('Python', 'C')
        print(each_line.rstrip())
        print(output.rstrip())