
# This is a pretty horrible way of doing things
def get_workout(day):
    if day == 'Monday':
        return 'Chest+biceps'
    elif day == 'Tuesday':
        return 'Back+triceps'
    elif day == 'Wednesday':
        return 'Core'
    elif day == 'Thursday':
        return 'Legs'
    elif day == 'Friday':
        return 'Shoulders'
    elif day in ('Saturday', 'Sunday'):
        return 'Rest'
    raise ValueError('Not a day')

'''Not only is it ugly, it does not scale! What if we need to add Thursday 
every 2nd week or swap out a workout routine? Much better to separate 
the logic from the data. A mapping / dictionary works really well here:'''

workouts = {
    'Monday': 'Chest+biceps',
    'Tuesday': 'Back+triceps',
    'Wednesday': 'Core',
    'Thursday': 'Legs',
    'Friday': 'Shoulders',
    'Saturday': 'Rest',
    'Sunday': 'Rest',
}

# Pro tip: another nice way to define a dictionary is to zip two lists:
days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders Rest Rest'.split()

workouts2 = dict(zip(days, routines))


# Same function as the first, but shorter, readable and extensible
def get_workout_2(day):
    routine = workouts.get(day)
    if routine is None:
        raise ValueError('Not a day')
    return routine


# --- Counting inside a loop ---


days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()

# This is one way of keeping track of keys
i = 0
for day in days:
    i += 1
    print(f'{i}. {day}')

# This is using enumerate
for i, day in enumerate(days):
    print(f'{i + 1}. {day}')

# You can give a starting point using enumerate
for i, day in enumerate(days, 1):
    print(f'{i + 1}. {day}')


# --- Using the "with" statement ---


# Normal way to open/close files
f = open('text', 'w')
f.write('hello\n')
f.close()

# If you get an exception between open and close, the file won't be closed
f = open('text', 'w')
f.write('hello\n')
raise Exception
f.close()

# The exception crashed the program and the file handle was left open, not good.
# To prevent this you could use a try and finally, latter will always hit.
try:
    f = open('text', 'w')
    f.write('hello\n')
    1/0 # to get a zero division error
except ZeroDivisionError:
    print('exception raised: cannot divide by 0')
finally:
    print('but I will always close my file handle!')
    f.close()

# There is an even better way to do it, when you go out of the block, it
# auto closes the file
with open("text", "w") as f:
    f.write("hello\n")
    raise Exception # to see if the file is really closed


# --- Use built-ins/standard library


# Get a range of numbers
numbers = range(1, 11)
list(numbers)

# To sum these numbers
total = 0
for num in numbers:
    total += num

# You can just use sum()
sum(numbers)

# Exemple for using max() and min()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders'.split()
timings = '45 45 30 55 45'.split()

workout_times = dict(zip(routines, timings))

# Typical way
max_routine = None
max_timing = 0
for routine, timing in workout_times.items():
    timing = int(timing)
    if timing > max_timing:
        max_routine = routine
        max_timing = timing

# Using the max() and min() built-in
max(workout_times.items(), key=lambda x: x[1])
min(workout_times.items(), key=lambda x: x[1])


# --- Leverage tuple unpacking and namedtuples ---


# Need to swap a variable
a, b = 1, 2

# Typical way
temp = a
a = b
b = temp

# Pythonic way, no temporary variable needed
a, b = b, a

# Unpacking a tuple
routine, minutes = max(workout_times.items(), key=lambda x: x[1])

# Named tuple
# Typical way
workout = ('Chest+biceps', 'Monday', 45)
print(f'On {workout[1]} I train {workout[0]} during {workout[2]}')

# Using namedtuple
from collections import namedtuple

Workout = namedtuple('Workout', 'routine day duration') # using cap since it's a class (with no behavior)
workout = Workout(routine='Chest+biceps', day='Monday', duration=45)
print(f'On {workout.day} I train {workout.routine} during {workout.duration}')


# --- List comprehension and generators ---


days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()

# To get all days starting with T, typical way
def get_t_days(days=days):
    t_days = []
    for day in days:
        if day[0].lower() == 't':
            t_days.append(day)
    return t_days

# Using list comprehension
def get_t_days(days=days):
    return [day for day in days if day[0].lower() == 't']

# Using a generator
def get_t_days_gen(days=days):
    for day in days:
        if day[0].lower() == 't':
            yield day

from random import choice

def get_random_day(days=days):
    i = 0
    while True:
        i += 1
        yield i, choice(days)

days_gen = get_random_day() # initiate generator
next(days_gen)

from itertools import islice
slice_ = islice(days_gen, 100, 105)
list(slice_)


# --- String formatting and concatenation ---


lst = ['hello world,', 'today I am happy,', 'because I am writing Python code!']
' '.join(lst)


