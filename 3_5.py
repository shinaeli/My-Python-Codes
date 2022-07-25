guest_list = ['Nas', 'Jay-Z', 'Dangote']

print(f"Hey {guest_list[0]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[1]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[2]}. I'm inviting you to a dinner hosted by me.")

missing_guest = guest_list[1]

print(f"{missing_guest} won't be making it to the dinner.")

guest_list[1] = 'Otedola'

print(f"Hey {guest_list[0]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[1]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[2]}. I'm inviting you to a dinner hosted by me.")