from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests


# --- LIST COMPREHENSIONS ---

names = "pybites mike bob julian tim sara guido".split()

# for name in names:
#     print(name.title())

first_half_alphabet = list(string.ascii_lowercase)[:13]


# -- This is the simple way to doing it
new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())


# -- This is the same thing using list comprehension
new_names_2 = [name.title() for name in names if name[0] in first_half_alphabet]

resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
#print(words[:5])

cnt = Counter(words)
#print(cnt.most_common(5))

#print("-" in words)
words = [re.sub(r"\W+", r"", word) for word in words]
#print("-" in words)


resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
#print(len(stopwords))

words = [word for word in words if word.strip() and word not in stopwords]
#print("the" in words)

cnt = Counter(words)
#print(cnt.most_common(5))


# --- GENERATORS ---

def num_gen():
    for i in range(5):
        yield i

gen = num_gen()

print(next(gen))

#notice that this iteration starts at 1 since the 0 was already returned
for i in gen:
    print(i)

# This returns an error since we finished the iteration
#print(next(gen))

options = "red yellow blue white black green purple".split()


# -- Normal way
def create_select_options(options=options):
    select_list = []

    for option in options:
        select_list.append(f"<option value={option}>{option.title()}</option>")

    return select_list

from pprint import pprint as pp
print(pp(create_select_options()))


# -- Using generator
def create_select_options_gen(options=options):
    for option in options:
        yield f"<option value={option}>{option.title()}</option>"

print(list(create_select_options_gen()))


# -- IMPORTANT: List generators are faster than iterating over a list normally
