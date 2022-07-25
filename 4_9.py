output_list = []

for num in range(1, 11):
    cubed = num ** 3
    output_list.append(cubed)

print(output_list) #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# OR Using List Comprehension
cubed = [num ** 3 for num in range(1, 11)]
print(cubed) #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]