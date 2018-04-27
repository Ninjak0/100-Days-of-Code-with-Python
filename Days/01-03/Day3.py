# Pomodoro Timer
# Here are the 5 steps :
# 1) Decide on a task to be done
# 2) Set the timer to 25 minutes
# 3) Work on the task until de the timer rings
# 4) Take a 5 minutes break
# 5) Repeat steps 1-4 four times
# 6) take a 15-30 minutes break
# 7) Repeat the cycle if the task is not accomplished

import winsound
import datetime
import time
import sys

# Define how long each period is and how long breaks are
work_time = 25
breather_time = 5


def time_over():
    '''
    Will play a beep sound 3 times
    '''
    frequency = 1000  # Set Frequency To 2500 Hertz
    duration = 700  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    time.sleep(0.2)
    winsound.Beep(frequency, duration)
    time.sleep(0.2)
    winsound.Beep(frequency, duration)

def timer(delay):
    '''
    delay: expects an int parameter
    Starts a timer that will print a countdown of n minutes in console
    A beep will sound when the countdown reaches 0:00:00
    '''
    zero_time = datetime.timedelta(seconds=-1)
    work_period = datetime.timedelta(minutes=delay)
    work_second = datetime.timedelta(seconds=1)

    while work_period != zero_time:
        sys.stdout.write('\r' + str(work_period))
        sys.stdout.flush()
        work_period -= work_second
        time.sleep(1)

    time_over()

def main_work():
    print("Work on '" + task + "' for " + str(work_time) + " minutes.")
    timer(work_time)

def break_time():
    print("Good Work! Take a " + str(breather_time) + " minutes break.")
    timer(breather_time)


# Start of the main program
print("     ---Welcome to the Pomodoro Timer---")
print()
task = input("Please enter the name or a description of a task that needs to "
             "be accomplished: ")
print()
print("Great! Here is your work plan:")
print("-Work on '" + task + "' for 25 minutes until you hear the bell.")
print("-Take a 5 minutes break.")
print("-Repeat 4 times.")
print("-Take a 15 minutes break after 4 times.")
print()
input("Press Enter to begin!")
print()


# Main block of the 4 period of the main cycle
def main_block():
    for x in range(4):
        print("Let's begin period " + str(x + 1) + " of 4!")
        main_work()
        print()
        print()
        if x == 3:
            pass
        else:
            break_time()
        print()
        print()


main_block()

# After the main cycle is done
print("Nice work! Please take a 15 minutes break.")
timer(15)
print()
print()

# Confirm the user if the user is done or not, repeat if not
print("Were you able to accomplish the task?")
done = input("Please enter Y if you are done or N if you need to start another"
             " cycle: ")

while done.upper() != "N" or "Y":
    if done.upper() == "N":
        print("Let's go again!")
        main_block()
        break
    elif done.upper() == "Y":
        print("Nicely done! Goodbye!")
        break
    else:
        print("Invalid choice!")
        print()
    done = input(
        "Please enter Y if you are done or N if you need to start another"
        " cycle: ")





