# Desired output of waiting_list is:
# 1.Ben
# 2.John
# 3.Sen

waiting_list = ["sen", "ben", "john"]
waiting_list.sort()     # Lists are mutable, so the method returns nothing but updates the string
# waiting_list.sort(reverse=True) will reverse sort the list

for index, item in enumerate(waiting_list):
    row = f"{index + 1}-{item.capitalize()}"
    print(row)