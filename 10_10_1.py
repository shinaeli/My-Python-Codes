with open('Sweeney Todd The Barber Of Fleet Street.txt') as sweeney_object_file:
    line_list = sweeney_object_file.readlines()
    for line in line_list:
        print(line)
    get_content = sweeney_object_file.read()
    get_content_list = get_content.split()
    print(len(get_content_list))
    # 439803
    output_container = []
    for item in get_content_list:
        if item == 'the':
            output_container.append('the')
    print(len(output_container))