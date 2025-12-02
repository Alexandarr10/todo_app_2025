name = input("Enter your name:")
names = []

while name != "Exit":
    name = input("Enter name")
    if name != "Exit":
        names.append(name.capitalize())
    print(names)


print("Correct!")
