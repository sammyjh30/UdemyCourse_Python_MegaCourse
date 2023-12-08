# with open("../files/docs.txt", "r") as file:   - This will fail because the file and path need to exist
with open("../files/doc.txt") as file:          # By default open() assumes "r" as the mode
        content = file.read()  # content can be used outside the with. Note, do not read file before assigning -> cursor

# file.read()     - file as a variable still exists, but it is now associated with a closed file
# and hence this line will fail
