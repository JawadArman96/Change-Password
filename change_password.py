#!/usr/bin/env python3
import re
from Levenshtein import distance
# import sys


def change_password(old_password, new_password):
    special_chars = ['!', '@', '#', '$', '&', '*']
    # define regex (in total min length of the password should be 19)
    reg_ex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$&*])[A-Za-z0-9!@#$&*]{19,}$"
    # compiling regex
    pattern = re.compile(reg_ex)
    # searching regex
    match = re.search(pattern, new_password)
    # validating conditions
    if not match:            # checking alphanumeric,digits,
        print("should be 18 alphanumeric characters, atleast 1 uppercase,"
              "atleast 1 lowercase, 1 special characters")
        return False         # special characters and length
    if new_password == old_password:  # checking if password
        print("Password matched with the old one")  # is equal
        return False
    # checking repetition
    numeric_count = 0
    for i in range(0, 26):                            # repeating alphabet
        char_val = chr(ord('a') + i)                  # checking lowercase repeat
        count_val = new_password.count(char_val)
        if count_val > 4:
            print("Repeated lowercase 4 times")
            return False
        char_val = chr(ord('A') + i)
        count_val = new_password.count(char_val)     # checking uppercase repeat
        if count_val > 4:
            print("Repeated uppercase 4 times")
            return False
        if i < 10:
            char_val = chr(ord('0') + i)
            count_val = new_password.count(char_val)  # repeating numeric
            numeric_count += count_val
            if count_val > 4:
                print("Repeated numbers 4 times")
                return False

    # checking extra special characters
    count_val = 0
    for char_val in special_chars:
        count_val += new_password.count(char_val)
    if count_val > 4:
        print("More than 4 special characters")
        return False
    # checking if 50% is a number
    percentage = (numeric_count / len(new_password)) * 100
    if percentage >= 50:
        print("50% of the password should not be number")
        return False
    # checking if 80% match with previous
    dist = distance(old_password, new_password)
    max_len = max(len(old_password), len(new_password))
    percentage = (1 - (dist/max_len)) * 100
    # print(str(dist) + " " + str(max_len) + " " + str(percentage))
    if percentage >= 80:
        print("password matches 80% with the old one")
        return False
    return True


if __name__ == "__main__":
    saved_old_password = "*34ABCbo7i89CDEFu&PSQ012"
    # test_password = sys.argv[1]
    test_password = "*34aBCbo7i89CdEGu&PSQ0"
    print(change_password(saved_old_password, test_password))
