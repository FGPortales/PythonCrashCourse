current_users = ['Álvarez', 'Antúnez', 'Benítez', 'Chávez', 'Díaz',
                 'Hernández', 'García', 'Rodríguez']
current_users.append('John')
new_users = ['Portales', 'Armas', 'Guevara', 'Chávez', 'Espinoza', 'Díaz']
new_users.append('JOHN')
current_users_copy = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print("You need to enter with other user")
        print(new_user)
    else:
        print("Username Available!")

print(current_users)
print(current_users_copy)
print(new_users)
