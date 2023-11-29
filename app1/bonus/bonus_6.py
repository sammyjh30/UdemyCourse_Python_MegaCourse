contents = ["All carrots are to be sliced "
            "longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

a = ("I am a string "
     "on my own")
b = "I am also a string " \
     "on my own"                # Note the different syntax between the 3 string splits

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# zip() works like enumerate -> list(tupled matching indexes)
for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)


