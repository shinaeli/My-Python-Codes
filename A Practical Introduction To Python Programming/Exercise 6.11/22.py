# A simple way of encrypting a message is to rearrange its characters. One way to rearrange the
# characters is to pick out the characters at even indices, put them first in the encrypted string,
# and follow them by the odd characters. For example, the string message would be encrypted
# as msaeesg because the even characters are m, s, a, e (at indices 0, 2, 4, and 6) and the odd
# characters are e, s, g (at indices 1, 3, and 5).
# (a) Write a program that asks the user for a string and uses this method to encrypt the string.
# (b) Write a program that decrypts a string that was encrypted with this method.

user_input = input('Provide a word to be encrypted: ')
evens, odds = '', ''

for count in range(0, len(user_input)):
    if count % 2 == 0:
        evens += user_input[count]
    else:
        odds += user_input[count]

print(evens+odds)

# Provide a word to be encrypted: message
# msaeesg
