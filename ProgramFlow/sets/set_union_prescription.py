from prescription_data import adverse_interactions
meds_to_watch = set()

for interaction in adverse_interactions:
    # create a new set each time
    # meds_to_watch = meds_to_watch | interaction
    # meds_to_watch.update(interaction)
    meds_to_watch |= interaction
print(sorted(meds_to_watch))

print('-' * 80)

# add several sets to form unions
meds_to_watch.clear()
meds_to_watch.update(*adverse_interactions)
print(sorted(meds_to_watch))
print('-' * 80)
# to print each item in a separate line we can unpack it
print(*sorted(meds_to_watch), sep='\n')
