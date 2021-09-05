def banner_text(text, screen_width):
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


screen_wid = 66
banner_text("*", screen_wid)
banner_text("Always look on the bright side of life...", screen_wid)
banner_text("If life seems jolly rotten,", screen_wid)
banner_text("There's something you've forgotten!", screen_wid)
banner_text("And that's to laugh and smile and dance and sing,", screen_wid)
banner_text(" ", screen_wid)
banner_text("When you're feeling in the dumps,", screen_wid)
banner_text("Don't be silly chumps,", screen_wid)
banner_text("Just purse your lips and whistle - that's the thing!", screen_wid)
banner_text("And... always look on the bright side of life...", screen_wid)
banner_text("*", screen_wid)

result = banner_text("Nothing is returned", screen_wid)
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())
