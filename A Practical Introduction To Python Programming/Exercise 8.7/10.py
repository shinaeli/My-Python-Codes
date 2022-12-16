# Write a censoring program. Allow the user to enter some text and your program should print
# out the text with all the curse words starred out. The number of stars should match the length
# of the curse word. For the purposes of this program, just use the“curse” words darn, dang,
# freakin, heck, and shoot. Sample output is below:
# Enter some text: Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freakin try.
# Oh *****, I thought I had the **** problem figured out.
# **** it. Oh well, it was a **** of a ****** try.

curse_words = ['darn', 'dang', 'freakin', 'heck', 'shoot']

user_input = input('Provide some sentences with curse words like "darn", "dang", "freakin", "shoot", "heck": ')
splitted_str = user_input.split()
# print(splitted_str)
output_list = []

for item in splitted_str:
    if ',' in item:
        get_first_letters = item[0:(item.lower().index(','))]
        get_stars = '*' * len(get_first_letters)
        new_output = get_stars + ','
        output_list.append(new_output)
    elif '.' in item:
        get_first_letters = item[0:(item.lower().index('.'))]
        get_stars = '*' * len(get_first_letters)
        new_output = get_stars + '.'
        output_list.append(new_output)
    elif '!' in item:
        get_first_letters = item[0:(item.lower().index('!'))]
        get_stars = '*' * len(get_first_letters)
        new_output = get_stars + '!'
        output_list.append(new_output)
    elif item.lower() in curse_words:
        get_star = '*' * len(item)
        output_list.append(get_star)
    else:
        output_list.append(item)

print(' '.join(output_list))

# Provide some sentences with curse words like "darn", "dang", "freakin", "shoot", "heck": Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freakin try.
# Oh *****, I thought I had the **** problem figured ***. **** **. Oh ****, it was a **** of a ******* ***.
# Provide some sentences with curse words like "darn", "dang", "freakin", "shoot", "heck": Just shoot the freakin heck.
# Just ***** the ******* ****.
# Provide some sentences with curse words like "darn", "dang", "freakin", "shoot", "heck": Just shoot the freakin heck!
# Just ***** the ******* ****!