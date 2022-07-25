with open('learning_python.txt') as learning_python_object:
    # 'read' method is a function that allows the content of the object-file to be read
    # It returns a string which is the entire content of the file
    contents = learning_python_object.read()
    # 'rstrip' method removes all white spaces that are present on the right side of the string
    print(contents.rstrip())


with open('learning_python.txt') as learning_python_object:
    # 'readlines' method returns a list of which its individual item is each lie of content of the object-file
    content_lines = learning_python_object.readlines()
    for each_line in content_lines:
        print(each_line.rstrip())


with open('learning_python.txt') as learning_python_object:
    for read_line in learning_python_object:
        print(read_line.rstrip())