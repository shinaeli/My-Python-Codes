current_users = ['Jaiye', 'Admin', 'Timothy', 'Kehinde', 'Jamal', 'James', 'Frida', 'Seyi', 'Tolu']
current_users_upper = ['JAIYE', 'ADMIN', 'TIMOTHY', 'KEHINDE', 'JAMAL', 'JAMES', 'FRIDA', 'SEYI', 'TOLU']
new_users = ['Joy', 'TIMOTHY', 'Joshua', 'Goke', 'Jamal', 'KATE', 'Laura', 'TOLU', 'HARRIS']

for user in new_users:
    if user in current_users or user.upper() in current_users_upper:
        print('Please, you need to enter a new username.')
    else:
        print(f"Congrats. The username '{user}' is available.")


