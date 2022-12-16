#  At a certain school, student email addresses end with @student.college.edu, while professor email addresses end with @prof.college.edu. Write a program that first asks the
# user how many email addresses they will be entering, and then has the user enter those addresses. After all the email addresses are entered, the program should print out a message
# indicating either that all the addresses are student addresses or that there were some professor addresses entered.

student_mail_ender, prof_mail_ender = '@student.college.edu', '@prof.college.edu'

number_of_inputs = int(input('Provide the number of mails to be entered: '))

count = 1
students_recorder, profs_recorder = 0, 0

while count <= number_of_inputs:
    user_input = input('Provide an email: ')
    if user_input.endswith(student_mail_ender):
        students_recorder += 1
    elif user_input.endswith(prof_mail_ender):
        profs_recorder += 1
    count += 1

if students_recorder == number_of_inputs:
    print('All the mails provided belongs to students.')
else:
    print('Some of the mails provided belongs to professors.')

