# created a custom exception class called 'AssignmentException'
class AssignmentException(Exception):
    pass


while True:
    try:
        student_name = input('Provide your full name: ')
        assignment_score_1 = input('Provide score obtained from the first assignment: ')
        assignment_score_2 = input('Provide score obtained from the second assignment: ')
        exam_score = input('Provide your examination score: ')

        if float(assignment_score_1) > 50:
            # if the condition above is true
            # an instance of 'AssignmentException' is raised(called) by passing an error message to it as an argument
            raise AssignmentException('Assignment1 score cannot be greater than 50')
        elif float(assignment_score_2) > 50:
            # if the condition above is true
            # an instance of 'AssignmentException' is raised(called) by passing an error message to it as an argument
            raise AssignmentException('Assignment2 score cannot be greater than 50')

        final_score = 0.25 * (float(assignment_score_1) + float(assignment_score_2)) + 0.75 * float(exam_score)

        # if the condition below is false, an assertion error is displayed
        # it will use the string beside it as its message
        assert float(exam_score) <= 100, 'Final exam score cannot be greater than 100.'

        print(f'{student_name.title()} scored {final_score} over 100.')

        grade = ''
        if final_score > 90:
            grade += 'A+(Outstanding)'
        elif (final_score > 80) and (final_score <= 90):
            grade += 'A(Very Good)'
        elif (final_score > 70) and (final_score <= 80):
            grade += 'B(Good)'
        elif final_score <= 70:
            grade += 'Fail'

        create_file = f'Report Cards/{student_name.title()}.txt'
        with open(create_file, 'w') as score_object:
            score_object.write(f'''
    {'*' * 3}Report Card{'*' * 3}
    {'*' * 3}Course name: Python for Beginners{'*' * 3}
    {'=' * 40}
    Student Name: {student_name.title()}
    Assignment-1 score: {assignment_score_1}
    Assignment-2 score: {assignment_score_2}
    Exam score: {exam_score}
    Final score: {round(final_score, 4)}
    Grade: {grade}
            ''')
    except AssignmentException as e:
        print(f'''
        Error: {e}.
        Provide the correct input next time!
        ''')
    except AssertionError as e:
        print(f'''
        Error: {e}.
        Provide the correct input next time!
        ''')
    except ValueError as e:
        print(f'''
        Error: {e}.
        Provide the correct input next time!
        ''')
        break



