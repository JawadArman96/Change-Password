#!/usr/bin/env python3
import re
from Levenshtein import distance
# import sys


def change_password(old_password, new_password):
    special_chars = ['!', '@', '#', '$', '&', '*']
    # define regex (in total length of the password should be 20)
    reg_ex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$&*])[A-Za-z0-9!@#$&*]{20,}$"
    # compiling regex
    pattern = re.compile(reg_ex)
    # searching regex
    match = re.search(pattern, new_password)
    # validating conditions
    if not match:            # checking alphanumeric,digits,
        return False         # special characters and length
    if new_password == old_password:  # checking if password
        return False
    # checking repetition
    numeric_count = 0
    for i in range(0, 26):
        char_val = chr(ord('a') + i)
        count_val = new_password.count(char_val)      # repeating alphabet
        if count_val > 4:
            return False
        if i < 10:
            char_val = chr(ord('0') + i)
            count_val = new_password.count(char_val)  # repeating numeric
            numeric_count += count_val
            if count_val > 4:
                return False

    # checking extra special characters
    count_val = 0
    for char_val in special_chars:
        count_val += new_password.count(char_val)
    if count_val > 4:
        return False
    # checking if 50% is a number
    percentage = (numeric_count / len(new_password)) * 100
    if percentage >= 50:
        return False
    # checking if 80% match with previous
    dist = distance(old_password, new_password)
    max_len = max(len(old_password), len(new_password))
    percentage = (1 - (dist/max_len)) * 100
    if percentage >= 80:
        return False
    return True


if __name__ == "__main__":
    saved_old_password = "abcdefghijABChgjgjh35!@#EFGHIJ"
    # test_password = sys.argv[1]
    test_password = "abcdefghijABCD12335!@#EFGHIJ"
    print(change_password(saved_old_password, test_password))
