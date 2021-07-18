splitString = 'Hello\nWorld'
print(splitString)

# While writing """ or ''' python interpreter waits for next three " or ' to end vars
anotherSplitString = '''Multiline
in
Single
variable
and i don't need to escape single
or double " quote :)'''
print(anotherSplitString)

# Escaping \ from string
# escape \ with another \
print("c:\\User\\text\\notes.txt")
# use raw string, this is typically used in regular expression
print(r"c:\User\text\notes.txt")

