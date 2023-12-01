filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"../files/day6/{filename}", 'r')
    content = file.read()
    print(content)
    file.close()
