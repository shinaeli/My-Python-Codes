# Designing a multiple choice question

# Import modules 'question1', 'question2', 'question3' and 'marker' from 'sample_questions' folder.
from sample_questions import question1, question2, question3, marker

# Initialize three variables: 'start', 'updated_score', 'total_score' with respective default values.
start, updated_score, total_score = True, 0, 3

while start:
    # Call 'question_1' function and wrap its returned value in variable 'test1'.
    test1 = question1.question_1()
    # Call 'marker' function passing 'test1' as an argument to it.
    # The value returned updates 'updated_score' variable.
    updated_score += marker.marker(test1)

    # Call 'question_2' function and wrap its returned value in variable 'test2'.
    test2 = question2.question_2()
    # Call 'marker' function passing 'test2' as an argument to it.
    # The value returned updates 'updated_score' variable.
    updated_score += marker.marker(test2)

    # Call 'question_3' function and wrap its returned value in variable 'test3'.
    test3 = question3.question_3()
    # Call 'marker' function passing 'test3' as an argument to it.
    # The value returned updates 'updated_score' variable.
    updated_score += marker.marker(test3)

    # The total score attained by the user is displayed.
    print(f'Your Score: {updated_score} out of {total_score}.')
    # The 'while' loop terminates.
    start = False


