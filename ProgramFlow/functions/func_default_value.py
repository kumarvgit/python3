#  Added default value without having a space between var=val
def banner_text(text=" ", screen_width: int = 80) -> None:
    """
    Formats the given line with specified screen_width
    :param text: the text to display
    :param screen_width: the width of the screen
    :raises ValueError: if the text is not going to fit in screen
    :return: None
    """
    # screen_width = 50
    if len(text) > screen_width - 4:
        raise ValueError("String {1} is larger than specified width {0}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)

result = banner_text("Nothing is returned", 60)
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())
