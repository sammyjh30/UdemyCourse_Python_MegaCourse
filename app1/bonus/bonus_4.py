# Lists [] are mutable => they can be changed e.g. replacing a value
# Tuple () is an immutable List
# Strings are immutable => they cannot be changed. So how do we change a character in a str?
# => .replace('original char', 'new char') => creates a NEW string, does not update the existing one unless explicit
#  string = string.replace(). if you .replace(char1, char2, int no. of occurrences from beginning of string)

filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

