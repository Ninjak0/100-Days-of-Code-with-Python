'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    search_results = re.search("(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)",
                               line)

    year    = int(search_results.group(1))
    month   = int(search_results.group(2))
    day     = int(search_results.group(3))
    hour    = int(search_results.group(4))
    minute  = int(search_results.group(5))
    second  = int(search_results.group(6))

    extracted_date = datetime(year, month, day, hour, minute, second)

    return extracted_date


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    min_time = datetime.max
    max_time = datetime.min
    for line in loglines:
        if "Shutdown initiated" in line:
            low_temp_initiated = convert_to_datetime(line)
            if low_temp_initiated < min_time:
                min_time = low_temp_initiated
        if "Shutdown complete" in line:
            high_temp_initiated = convert_to_datetime(line)
            if high_temp_initiated > max_time:
                max_time = high_temp_initiated

    return max_time - min_time

