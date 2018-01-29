def make_great(names):
    cnt = 0
    while cnt < len(names):
        names[cnt] = "Great" + names[cnt]
        cnt = cnt + 1

def show_magicians(names):
    for name in names:
        print(name)

names_magicians = ["Mike", "Bobby", "John", "Wiliams", "Bill"]
copy_names_magicians = names_magicians[:]

make_great(names_magicians)
show_magicians(names_magicians)
show_magicians(copy_names_magicians)