information_user_0 = {
    'first_name': 'Carlos',
    'last_name': 'Pérez',
    'age': '24',
    'city': 'city'
}
information_user_1 = {
    'first_name': 'Ruben',
    'last_name': 'Ramirez',
    'age': '21',
    'city': 'Lima'
}
information_user_2 = {
    'first_name': 'Rosa',
    'last_name': 'Guzmán',
    'age': '23',
    'city': 'Loreto'
}

people = [information_user_0, information_user_1, information_user_2]

for user in people:
    print(f"Name: {user['first_name']} {user['last_name']}")
    print(f"Age: {user['age']} años")
    print(f"City: {user['city']}\n")
