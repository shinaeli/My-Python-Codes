# Write a program that repeatedly asks the user to enter a football score in the format winning
# score-losing score (like 27-13 or 21-3). The user indicates they are done entering scores by
# entering done. The program should then output the highest score and the lowest score out of
# all the scores entered.

score_list = []
while True:
    user_input = input('provide scores("winning - losing") and enter "done" to quit: ')
    if user_input == 'done':
        break
    else:
        get_index = user_input.index('-')
        first_score = user_input[0:get_index]
        second_score = user_input[get_index + 1:]
        score_list.append(int(first_score))
        score_list.append(int(second_score))


print(f'The highest score is {max(score_list)} while the lowest score is {min(score_list)}.')

# provide scores("winning - losing") and enter "done" to quit: 8-2
# provide scores("winning - losing") and enter "done" to quit: 5-1
# provide scores("winning - losing") and enter "done" to quit: 4-1
# provide scores("winning - losing") and enter "done" to quit: 4-0
# provide scores("winning - losing") and enter "done" to quit: 3-2
# provide scores("winning - losing") and enter "done" to quit: 7-2
# provide scores("winning - losing") and enter "done" to quit: 6-3
# provide scores("winning - losing") and enter "done" to quit: done
# The highest score is 8 while the lowest score is 0.
