current_users = ['admin', 'john', 'mike', 'andrew', 'james']
new_users = ['eric', 'stiv', 'marty', 'john', 'bob']

for new_user in new_users:
    if new_user in current_users:
        print("Error! " + new_user.title() + "'s name is busy")
    else:
        print("Ok")