# Using a nested loop to create co-ordinates
for x in range(3):
    # The outer 'x' loop runs once the inner 'y' loop runs completely
    for y in range(1, 5):
        # For each iteration in the inner 'y' loop, 'x' and 'y' gets printed
        print(f'({x}, {y})')