# Write a program that allows the user to enter any number of test scores. The user indicates
# they are done by entering in a negative number. Print how many of the scores are A’s (90 or
# above). Also print out the average.

score_list, count = [], 0
while True:
    user_score = int(input('Provide a score: '))
    if user_score >= 0:
        score_list.append(user_score)
    else:
        break

for item in score_list:
    if item >= 90:
        count += 1
print(f'{count} of the scores are As.')
print(f'The average of the scores is {sum(score_list) / len(score_list)}.')

# Provide a score: 75
# Provide a score: 88
# Provide a score: 90
# Provide a score: 94
# Provide a score: 71
# Provide a score: 35
# Provide a score: 48
# Provide a score: 91
# Provide a score: 85
# Provide a score: 62
# Provide a score: -99
# 3 of the scores are As.
# The average of the scores is 73.9.
