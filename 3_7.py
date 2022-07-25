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

print('Hey! Everyone. I found a bigger dinner table.')

guest_list.insert(0, 'Mrs. M. B. Omotosho')
guest_list.insert(2, 'Eminem')
guest_list.append('The Game')

print(f"Hey {guest_list[0]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[1]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[2]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[3]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[4]}. I'm inviting you to a dinner hosted by me.")
print(f"Hey {guest_list[5]}. I'm inviting you to a dinner hosted by me.")

print(guest_list) #['Mrs. M. B. Omotosho', 'Nas', 'Eminem', 'Otedola', 'Dangote', 'The Game']

print("I'm sorry. I can only invite two guests to the dinner.")

print(f"{guest_list.pop(2)}. I'm sorry, I couldn't invite you to the dinner.")
print(f"{guest_list.pop(2)}. I'm sorry, I couldn't invite you to the dinner.")
print(f"{guest_list.pop(2)}. I'm sorry, I couldn't invite you to the dinner.")
print(f"{guest_list.pop()}. I'm sorry, I couldn't invite you to the dinner.")

print(guest_list) #['Mrs. M. B. Omotosho', 'Nas']

print(f"{guest_list[0]}, you're still invited to the dinner.")
print(f"{guest_list[1]}, you're still invited to the dinner.")

del guest_list[1]
print(guest_list) #['Mrs. M. B. Omotosho']
del guest_list[0]
print(guest_list) #[]