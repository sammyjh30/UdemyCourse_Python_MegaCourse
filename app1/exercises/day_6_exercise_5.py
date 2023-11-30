new_member = input("Add a new member: ")

file = open('../files/members.txt', 'r')
members = file.readlines()
file.close()

members.append(new_member + '\n')

file = open('../files/members.txt', 'w')
file.writelines(members)
file.close()
