users = ['admin', 'john', 'mike', 'andrew', 'james']

if users:
    for user in users:
        if 'admin' == user:
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again")
else:
    print("We need to find some users!")