import functools
from datetime import datetime
import time

def time_it(function):
    @functools.wraps(function)
    def original_function(*args, **kwargs):
        start_time = datetime.today()

        result = function(*args, **kwargs)

        end_time = datetime.today()
        delay = end_time - start_time
        print(delay.total_seconds())

        return result

    return original_function

@time_it
def delay_message():
    print("Let's kick it off!")
    time.sleep(2)
    print("The deed is done.")


print(delay_message())
