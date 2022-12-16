# Write a program that takes any two lists L and M of the same size and adds their elements
# together to form a new list N whose elements are sums of the corresponding elements in L
# and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].


L = eval(input('Provide a list of numbers: '))
M = eval(input('Provide a list of numbers of the same size as the first list: '))
N = []

for num in range(len(L)):
    N.append(L[num] + M[num])

print(N)

# Provide a list of numbers: [3,1,4]
# Provide a list of numbers of the same size as the first list: [1,5,9]
# [4, 6, 13]