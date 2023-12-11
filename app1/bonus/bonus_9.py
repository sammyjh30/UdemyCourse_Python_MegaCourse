
password = input("Enter new password: ")
result = []

if len(password) >= 0:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

if digit:
    result.append(True)
else:
    result.append(False)