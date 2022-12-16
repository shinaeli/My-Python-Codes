from search_name_func import search_name
from students_record import students_register

user_input = input('Provide student\'s admission number(between 10000 and 32000): ')

admission_nums = []

for detail in students_register:
    admission_nums.append(detail['admission number'])

# print(admission_nums)


print(search_name(admission_nums, int(user_input)))
