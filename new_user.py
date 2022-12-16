# class User:
#     def __init__(self, first_name, last_name, age, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age = age
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f'{self.first_name.title()} {self.last_name.title()} is {self.age}years old. Mail: {self.email}.')
#
#     def greet_user(self):
#         print(f'Welcome! {self.first_name.title()} {self.last_name.title()}.')
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         print(self.login_attempts)
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         print(self.login_attempts)

# def get_runnerup(arr):
#     output = []
#     for item in range(len(arr)):
#         if item in output:
#             continue
#         else:
#             output.append(item)
#     output.sort(reverse=True)
#     print(output[1])
#
#
# get_runnerup([2, 3, 6, 6, 5]) //5

# out_arr = []
# score_arr = []
# for count in range(5):
#     in_arr = []
#     name = input('provide a name: ').title()
#     in_arr.append(name)
#     score = float(input('provide a score: '))
#     in_arr.append(score)
#     out_arr.append(in_arr)
#
# for item in out_arr:
#     score_arr.append(item[1])
#
# output = []
# for item in range(len(score_arr)):
#     if item in output:
#         continue
#     else:
#         output.append(score_arr[item])
# output.sort(reverse=True)
# print(output)
#
# for item in out_arr:
#     if item[1] == output[len(output) - 2]:
#         print(item[0])
#     else:
#         continue


