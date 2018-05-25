import re

# ---When not to use Regex---

text = 'Awesome, I am doing the #100DaysOfCode challenge'

text.startswith('Awesome')
text.endswith('challenge')
print('100daysofcode' in text.lower())

new_text = text.replace('100', '200')


# ---Now using Regex---

re.search(r"I am", text)
re.match(r"I am", text) # does not work, because "I am" is not the full string
re.match(r"Awesome.*challenge", text) # this works, because it's the whole string

hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'

m = re.search(r"(#\d+DaysOfCode)", hundred)
print(m.groups())
m = re.search(r"(#\d+DaysOfCode)", two_hundred)
print(m.groups()[0])

text = '''
$ python module_index.py |grep ^re
re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095
'''

print(re.findall(r'\d+', text))

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum"""

print(re.findall(r"\w+", text))
print(text.split()[:5])

print(re.findall(r"[A-Z][a-z0-9]+", text))

from collections import Counter

cnt = Counter(re.findall(r"[A-Z][a-z0-9]+", text))
print(cnt)
print(cnt.most_common(5))

movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')

pat = re.compile(r'''
                  ^             # start of string
                  \d+           # one or more digits
                  \.            # a literal dot
                  \s+           # one or more spaces
                  (?:           # non-capturing parenthesis, so I don't want store this match in groups()
                  [A-Za-z']+\s  # character class (note inclusion of ' for "Schindler's"), followed by a space
                  )             # closing of non-capturing parenthesis
                  {2}           # exactly 2 of the previously grouped subpattern
                  \(            # literal opening parenthesis
                  \d{4}         # exactly 4 digits (year)
                  \)            # literal closing parenthesis
                  $             # end of string
                  ''', re.VERBOSE)

for movie in movies:
    print(movie, pat.match(movie))

text = '''Awesome, I am doing #100DaysOfCode, #200DaysOfDjango and of course #365DaysOfPyBites'''

new_text = re.sub(r'\d+', '100', text)
print(new_text)

new_text2 = re.sub(r"(#\d+DaysOf)\w+", r"\1Python", text)
print(new_text2)