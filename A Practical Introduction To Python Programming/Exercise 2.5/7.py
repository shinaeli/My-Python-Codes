# Write a program that uses exactly four for loops to print the sequence of letters below.
# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

output = ''

for item in range(10):
    output += 'A'
for item in range(7):
    output += 'B'
for item in range(4):
    output += 'CD'
output += 'E'
for item in range(6):
    output += 'F'
output += 'G'

print(output)

# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
