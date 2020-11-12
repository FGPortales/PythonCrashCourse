# usernames = ['perez', 'rodriguez', 'ortega', 'león', 'admin']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello {}, would you like to see a status report?".format(
                username))
        else:
            print("Hello {}".format(username))
        print("Hello {}, thank you for logging again".format(username))
else:
    print("We need to find some users!!")
