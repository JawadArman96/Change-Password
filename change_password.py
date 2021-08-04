#!/usr/bin/env python3
import re
# import sys


def change_password(old_password, new_password):
    # define regex (in total length of the password should be 20)
    reg_ex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$&*])[A-Za-z0-9!@#$&*]{20,}$"
    # compiling regex
    pattern = re.compile(reg_ex)
    # searching regex
    match = re.search(pattern, new_password)
    # validating conditions
    if not match:
        return False
    if new_password == old_password:
        return False
    return True


if __name__ == "__main__":
    saved_old_password = "old_password"
    # test_password = sys.argv[1]
    test_password = "ashdsdhf*Zgsdhfhsdfgsdfghdg3fhsgdf"
    print(change_password(saved_old_password, test_password))
