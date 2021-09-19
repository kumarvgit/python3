import blackjack

# print(__name__)
# Access to protected member
# blackjack._deal_card()
# blackjack.play()

g = sorted(globals())
for x in g:
    print(x)
