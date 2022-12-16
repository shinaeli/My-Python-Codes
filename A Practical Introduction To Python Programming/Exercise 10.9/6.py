# Write a program that uses a boolean flag variable in determining whether two lists have any
# items in common.

arr1 = ['mary', 'joseph', 'cleo', 'moses', 'jonah']
arr2 = ['john', 'mary', 'silas', 'peter', 'jonah', 'timothy', 'philemon', 'saul']

output = ('timothy' in arr1) and ('timothy' in arr2)
output1 = ('mary' in arr1) and ('mary' in arr2)

print(output)
print(output1)

# False
# True