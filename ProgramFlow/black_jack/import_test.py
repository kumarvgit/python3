import blackjack

# print(__name__)
# Access to protected member
# blackjack._deal_card()
# blackjack.play()

g = sorted(globals())
for x in g:
    print(x)

person_details = ('Tim', 23, 'Aussie')

# Here _ is a throw away variable
name, _, _ = person_details
print(name)
print(_)

