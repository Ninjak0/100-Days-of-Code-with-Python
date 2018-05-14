import itertools
import time
import sys

symbols = itertools.cycle("-\|/")

# while True:
#     sys.stdout.write("\r" + next(symbols))
#     sys.stdout.flush()
#     time.sleep(0.25)

# for letter in itertools.product("julian", repeat=2):
#     print(letter)

friends = "mike bob julian".split()

# combinations doesn't care about the order
print(list(itertools.combinations(friends, 2)))

# permutations gives you in every order possible
print(list(itertools.permutations(friends, 2)))
