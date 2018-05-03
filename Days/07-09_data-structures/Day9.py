from data import *


# Note : us_state_abbrev == dict
#        states_list == list


# 1) Print out the 10th item in each.
def tenth_item_in_each():
    print("The 10th item in the list is", states_list[9])

    list_us_state_abbrev = list(us_state_abbrev.keys())
    item_10 = list_us_state_abbrev[9]
    print("The 10th item in the dictionary is", item_10, ":",us_state_abbrev[item_10])


# 2) Print out the 45th key in the dictionary.
def key_45_in_dict():
    list_us_state_abbrev = list(us_state_abbrev.keys())
    print("The 45th item in the dictionary is", list_us_state_abbrev[44])


# 3) Print out the 27th value in the dictionary.
def value_27_in_dict():
    list_us_state_abbrev = list(us_state_abbrev.values())
    print("The 27th value in the dictionary is", list_us_state_abbrev[26])

tenth_item_in_each()
key_45_in_dict()
value_27_in_dict()