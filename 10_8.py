def read_file_content(file_name):
    try:
        with open(file_name, encoding='utf-8') as file_object:
            # 'dog_file_object.read()' returns a string value
            read_content = file_object.read()
    except FileNotFoundError:
        print('Please, make sure the file is located in this current directory.')

    else:
        print(read_content)


read_file_content('dogs.txt')
# Pops
# Mel
# Max
read_file_content('cats.txt')
# Please, make sure the file is located in this current directory.
read_file_content('Message/cats.txt')
# Puss
# Lizzy
# Peach-Fuzz

