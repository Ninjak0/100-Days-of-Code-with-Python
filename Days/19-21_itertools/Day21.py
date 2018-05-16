import itertools

# ---Bite 64. Fix a truncating zip function---

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in itertools.zip_longest(names, locations, confirmed, fillvalue="-"):
        print(participant)


if __name__ == '__main__':
    get_attendees()



# ---Bite 17. Form teams from a group of friends---
'''
Write a function called friends_teams that takes a list of friends,
a team_size (type int, default=2)
and order_does_matter (type bool, default False).

Return all possible teams. Hint: if order matters (order_does_matter=True),
the number of teams would be greater.
'''

friends = 'Bob Dante Julian Martin'.split()

def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter == False:
        return list(itertools.combinations(friends, team_size))
    elif order_does_matter == True:
        return list(itertools.permutations(friends, team_size))


# ---Bite 65. Get all valid dictionary words for a draw of letters---
'''
Complete get_possible_dict_words and _get_permutations_draw to get 
all valid dictionary words for a random draw of 7 letters.

For example a draw of letters G, A, R, Y, T, E, V would give highest 
valued word GARVEY (13 points).
'''

# TODO: Come back to this problem some other time

import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    pass

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    pass
