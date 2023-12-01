filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"../files/day6/{filename}", 'x')
    file.write("Hello")
    file.close()
