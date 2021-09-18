def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def centre_text(text):
def centre_text(*text, sep=" ", end="\n", file=None, flush=False):
    # Convert to text
    # text = str(text)
    # convert to a single string
    combined_text = ''
    for txt in text:
        combined_text = combined_text + str(txt) + sep
    # left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text)
    left_margin = (80 - len(combined_text)) // 2
    print(" " * left_margin, combined_text, sep=sep, end=end, file=file, flush=flush)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")
centre_text("centre_text", "first", "second", 3, 4, "spam")
centre_text("centre_text_endl", "first", "second", 3, 4, "spam", sep='|', end='-')

print()
print("first", "second", 3, 4, "spam")


# Write to file
with open("centered", mode="w") as centered_file:
    # call the function
    centre_text("spam and eggs", file=centered_file)
    centre_text("spam, spam and eggs", file=centered_file)
    centre_text(12, file=centered_file)
    centre_text("spam, spam, spam and spam", file=centered_file)
    centre_text("centre_text", "first", "second", 3, 4, "spam", file=centered_file)
    centre_text("centre_text_endl", "first", "second", 3, 4, "spam", sep='|', end='-', file=centered_file)
