from collections import namedtuple, defaultdict, Counter, deque
import random

# --Practice using namedtuples--
User = namedtuple("User", "name role weapon")
bobby = User(name="Bobby", role="Rogue", weapon="Dirk")
# Using F-String (fun and easy to read!)
print(f"{bobby.name} is a {bobby.role} that uses a {bobby.weapon} to fight his enemies.")

# --Practice using defaultdict--
challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]

# This does not work, the key is not already added

# challenges = {}
# for name, challenge in challenges_done:
#     challenges[name].append(challenge)

# But this does

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
print(challenges.get("julian"))

# --Practice using Counter--
words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()

# Here is how you would get the most common 5 words normaly

common_words = {}

for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

# sort dict by values descending and slice first 5 to get most common
for k, v in sorted(common_words.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(k, v)

# Now compare this to using Counter and its most_common method

print(Counter(words).most_common(5))

# --Practice using deque--
lst = list(range(10000000))
deq = deque(range(10000000))

def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

# TODO: look into the %timeit ipython magic function

