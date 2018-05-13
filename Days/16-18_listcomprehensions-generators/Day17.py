NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

# Use list comprehension to make the first letter of each word capitalized

names_titled = [name.title() for name in NAMES]
#print(names_titled)

# Reverse the order of names


def reverse_name(name):
    first, last = name.split()
    return f"{last} {first}"

names_reversed = [reverse_name(name).title() for name in NAMES]
#print(names_reversed)


