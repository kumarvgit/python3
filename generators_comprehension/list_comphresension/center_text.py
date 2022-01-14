def centre_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + "-"
    # using join
    # text = "-".join(args)  # error can not join strings and int
    # use list comphrension instead
    text = "-".join([str(arg) for arg in args])  # using comp in join
    # text = "-".join(str(arg) for arg in args)  # removing [] converts it to generator expression
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)  # Error can not join strings and int
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")  # Error can not join strings and int
