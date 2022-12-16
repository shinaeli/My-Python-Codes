# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
# occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase
# and lowercase) and numeric digits.

def duplicate_count(text):
    text = text.lower()
    count = {i: text.count(i) for i in set(text)}
    count = sorted(count.values())
    result = 0
    for i in count:
        if i > 1:
            result += 1
    return result

# def counter(word):
#   word = list(word.lower())
#   for i in word:
#     if (i.isalpha()) or (i.isdigit()):
#       count = word.count(i)
#         if (count > 1):
#           print "{} ={}" %(i,count)
#         while(word.count(i) > 1):
#           word.remove(i)


print(duplicate_count('aabBcde'))
