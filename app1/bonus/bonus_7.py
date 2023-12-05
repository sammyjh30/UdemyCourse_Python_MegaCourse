filenames = ["1.doc", "1.report", "1.presentation"]

# transform this list using a list comprehension
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)
