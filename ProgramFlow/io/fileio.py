"""
Conventional way where we need to close up the file after opening it.
"""
# jabber = open('sample.txt', mode='r')
#
# for line in jabber:
#     print(line)
# jabber.close()

"""
This is going to close the resources once the job is done
"""
with open('sample.txt', mode='r') as jabber:
    for line in jabber:
        print(line, end='')

"""
Using the readline each line
"""
with open('sample.txt', mode='r') as jabber:
    line = jabber.readline()
    while line:
        print(line)
        line = jabber.readline()

"""
Read all of them together
"""
with open('sample.txt', mode='r') as jabber:
    lines = jabber.readlines()
print(lines)
