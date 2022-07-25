from random import choice

items = [2, 15, 4, 8, 11, 3, 37, 27, 39, 10, 'k', 'h', 'g', 'm', 'f']
print(f"Any ticket matching these four letters or numbers'{choice(items)} {choice(items)} "
      f"{choice(items)} {choice(items)}' wins a prize.")


