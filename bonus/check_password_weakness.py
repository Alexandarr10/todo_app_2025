password = input("Enter your password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False

for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

upper = False

for j in password:
    if j.isupper():
        upper = True

result.append(upper)

if not all(result):
    print("Your password is too weak! Try to add at least 8 characters, including digits and uppercase letters")
else:
    print("Your password is strong!")
