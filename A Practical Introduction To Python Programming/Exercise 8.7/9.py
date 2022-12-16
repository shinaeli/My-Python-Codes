# Write a simple quiz game that has a list of ten questions and a list of answers to those questions.
# The game should give the player four randomly selected questions to answer.
# It should ask the questions one-by-one, and tell the player whether they got the question right or
# wrong. At the end it should print out how many out of four they got right.

from random import sample

questions = ['Which year did Nigeria gain independence?',
             'What is the capital of the United States of America?',
             'Who is the president of Nigeria?',
             "What is the title of Nas' debut rap album?",
             'What is the capital of New York?',
             'What is the capital of California?',
             'In which year was Gen. Muritala Mohammed assassinated?',
             'Who was the first Head of State in Nigeria?',
             "Who was Nigeria's Head of State during the Biafran Civil War?",
             'The leader of the Ogoni group that were executed by hanging was?'
             ]

answers = [
    '1960',
    'Washington D.C.',
    'Retired Major General Muhamadu Buhari',
    'Illmatic',
    'Albany',
    'Sacramento',
    '1976',
    'Major General Aguiyi Ironsi',
    'Major General Yakubu Gowon',
    'Ken Saro Wiwa'
]

picked_questions = sample(questions, 4)
score = 0
for item in picked_questions:
    print(item)
    user_answer = input('Your answer: ').title()
    get_index = questions.index(item)
    # print(get_index)
    if user_answer == answers[get_index]:
        print("You are correct.")
        score += 1
    else:
        print("You are wrong.")
        score += 0

print(f'You scored {score} out of {len(picked_questions)}.')


# What is the capital of New York?
# Your answer: osogbo
# You are wrong.
# The leader of the Ogoni group that were executed by hanging was?
# Your answer: olamide baddo
# You are wrong.
# Who is the president of Nigeria?
# Your answer: Retired Major General Muhamadu Buhari
# You are correct.
# What is the capital of California?
# Your answer: SacraMenTO
# You are correct.
# You scored 2 out of 4.

