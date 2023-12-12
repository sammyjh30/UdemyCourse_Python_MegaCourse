
password = input("Enter new password: ")
#  Dictionaries have a key-value pair e.g.{"key1":"value1", "key2":"value2"}
# Fetch the value using the key e.g dict["key1"]
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
uppercase = False
for i in password:
    if i.isdigit():
        digit = True
    elif i.isupper():
        uppercase = True

result["digit"] = digit
result["uppercase"] = uppercase

if all(result.values()):    # unless you specify values, all() checks the keys and will give True even if a Value is false
    print("Strong Password")
else:
    print("Weak Password")

print(result)
