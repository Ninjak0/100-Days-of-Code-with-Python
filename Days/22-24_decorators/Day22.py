from functools import wraps
import time

def my_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # do something before the original function is called
        # call the passer in fuction
        result = function(*args, **kwargs)
        # do something after the original function call
        return result
    # return wrapper = decorated function
    return wrapper


# decorator syntax
@my_decorator
def my_function(args):
    pass

# different syntax
def my_function2(args):
    pass
my_function = my_decorator(my_function)

def get_profile0(name, active=True, *sports, **awards):
    print('Positional arguments (required): ', name)
    print('Keyword arguments (not required, default values): ', active)
    print('Arbitrary argument list (sports): ', sports)
    print('Arbitrary keyword argument dictionary (awards): ', awards)

# print(get_profile("julian", False, "basketball", "soccer",
#                   pythonista="special honor of the community",
#                   topcoder="2017 code camp"))

def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('hi from decorator - args:')
        print(args)
        result = function(*args, **kwargs)
        print('hi again from decorator - kwargs:')
        print(kwargs)
        return result
    # return wrapper as a decorated function
    return wrapper

@show_args
def get_profile(name, active=True, *sports, **awards):
    print('\n\thi from the get_profile function\n')

# print(get_profile("bob", True, "basketball", "soccer",
#                   pythonista="special honor of the community",
#                   topcoder="2017 code camp"))


#  ---Decorator used to indicate the elapsed time for a function call---

def timeit(func):
    '''Decorator to time a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        # before calling the decorated function
        print('== starting timer')
        start = time.time()

        # call the decorated function
        func(*args, **kwargs)

        # after calling the decorated function
        end = time.time()
        print(f'== {func.__name__} took {int(end-start)} seconds to complete')

    return wrapper

@timeit
def  generate_report2():
    '''Function to generate revenue report'''
    time.sleep(2)
    print('(actual function) Done, report links ...')

# print(generate_report())


def print_args(func):
    '''Decorator to print function arguments'''

    @wraps(func)
    def wrapper(*args, **kwargs):

        # before
        print()
        print('*** args:')
        for arg in args:
            print(f'- {arg}')

        print('**** kwargs:')
        for k, v in kwargs.items():
            print(f'- {k}: {v}')
        print()

        # call func
        func(*args, **kwargs)

    return wrapper


@timeit
@print_args
def generate_report(*months, **parameters):
    time.sleep(2)
    print('(actual function) Done, report links ...')


parameters = dict(split_geos=True, include_suborgs=False, tax_rate=33)
generate_report('October', 'November', 'December', **parameters)