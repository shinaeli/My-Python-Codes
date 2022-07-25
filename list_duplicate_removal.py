# Using the mutator method or approach
ages = [12, 5, 8, 20, 5, 10, 12, 15, 11, 5, 7, 7, 14, 8, 10]
# Iterate through the 'ages' list
for age in ages:
    # For each iteration, check if the current item exists more tha once in the 'ages' list
    if ages.count(age) > 1:
        # If true, remove the item
        ages.remove(age)
# Print the mutated 'ages' list
print(ages) #[20, 12, 15, 11, 5, 7, 14, 8, 10]

# Using the second method which doesn't mutate the original 'ages' list
ages = [12, 5, 8, 20, 5, 10, 12, 15, 11, 5, 7, 7, 14, 8, 10]
# Create a empty list called 'outputList'
outputList = []
# Iterate through the 'ages' list
for age in ages:
    # For each iteration, check if the current item doesn't exist in 'outputList' list
    if age not in outputList:
        # If true, assign the item to 'outputList' list
        outputList.append(age)
# Print the fully-filled 'outputList' to the console
print(outputList) #[12, 5, 8, 20, 10, 15, 11, 7, 14]
# The 'ages' list still remains intact
print(ages) #[12, 5, 8, 20, 5, 10, 12, 15, 11, 5, 7, 7, 14, 8, 10]



