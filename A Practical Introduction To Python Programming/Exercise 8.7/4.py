# (a) Write a program that asks the user to enter a sentence and then randomly rearranges the
# words of the sentence. Don’t worry about getting punctuation or capitalization correct.
# (b) Do the above problem, but now make sure that the sentence starts with a capital, that
# the original first word is not capitalized if it comes in the middle of the sentence, and
# that the period is in the right place.

from random import shuffle

# user_str = input('Provide a sentence: ')
# splitted_str = user_str.split(' ')
# shuffle(splitted_str)
# print(' '.join(splitted_str))


# Provide a sentence: Tade runs very fast.
# very Tade runs fast.
# Provide a sentence: Tade runs very fast.
# runs fast. Tade very

user_str = input('Provide a sentence: ')
splitted_str = user_str.split(' ')
lowercased_str = [x.lower() for x in splitted_str]
shuffle(lowercased_str)
lowercased_str[0] = lowercased_str[0].title()
print(' '.join(lowercased_str))
