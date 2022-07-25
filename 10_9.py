def read_file_content(file_name):
    try:
        with open(file_name, encoding='utf-8') as file_object:
            # 'dog_file_object.read()' returns a string value
            read_content = file_object.read()
    except FileNotFoundError:
        pass

    else:
        print(read_content)


read_file_content('dogs.txt')
# Pops
# Mel
# Max
read_file_content('cats.txt')
read_file_content('Message/cats.txt')
# Puss
# Lizzy
# Peach-Fuzz

