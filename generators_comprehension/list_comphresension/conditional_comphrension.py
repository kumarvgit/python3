menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)


# comphrension equivalent of above code i.e. for loop
# adding condition in list comp, we can have x numbers of filters
#  here if is a filter hence it will add only if condition is true
meals = [meal for meal in menu if 'spam' not in meal]
print(meals)

# Filter chain
meals = [meal for meal in menu if 'spam' not in meal if "chicken" not in meal]
print(meals)

# using and in filter chain
meals = [meal for meal in menu if 'spam' not in meal and "chicken" not in meal]
print(meals)

# meals with spam or eggs but can not contain bacon and sausage together
fussy_meal = [meal for meal in menu
              if "spam" in meal
              or "eggs" in meal
              if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meal)
