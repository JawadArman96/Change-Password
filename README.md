# usage
```
# run the change_password.py with password as
# parameter to execute change_password() function
$python3 change_password.py password
# to test the funtion, first it is
# needed to create virtual environment
# and then from terminal run
$pytest testing.py
```
# sample data input file
```
# test_data.csv [new test case can be 
# added to this file for testing purpose
# it is used to test check_password()  
# and change_password()
# function]
# following is the sample

,abcdefABCDEF012345*,TRUE
abcdef012345ABCDEF*,TRUE
ABCDEFabcdef012345*,TRUE
ABCDEF012345abcdef*,TRUE
012345ABCDEFabcdef*,TRUE
012345abcdefABCDEF*,TRUE
... ... 

# test_data_old_pw.csv [new test case can be 
# added to this file for testing purpose
# it is used to test change_password() 
# function]
# following is the sample

,abcdefgABCDEFG012345*,abcdefgABCDEFG01234*,FALSE
abcdefgABCDEFG012345*,abcdefgABCDEFG0123*,FALSE
abcdefgABCDEFG012345*,abcdefGABCDEFG0123*,FALSE
abcdefgABCDEFG012345*,abcdefGPBCDEFG0123*,FALSE
abcdefgABCDEFG012345*,abcdefGPQCDEFG0123*,TRUE
... ... ...
```