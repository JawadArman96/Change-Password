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

# requirement
```
pip==21.2.2
flask==2.0.1
levenshtein==0.12.0
```
# used library's brief
```
In order to check similarity between old and 
new password I used levenshtein library which
use levensthein distance algorithm.
# Defination
The Levenshtein distance between two 
strings a,b (of length |a| and |b| respectively)
is given by  lev (a,b) where

lev(a,b) = {
 Case 1:    |a|  , if |b| ==0
 Case 2:    |b|  , if |a| ==0
 Case 3:    lev(tail(a), tail(b)), if a[0] == b[0]
 Case 4:    1 + min (lev(tail(a), b), 
                     lev(a, tail(b)), 
                     lev(tail(a), tail(b)))
                     , otherwise   
 }
 
The algorithm considers 3 types of operation to
a string insertions, deletions or substitutions
each step is consdered with cost of 1. The distance 
between two string a, b is the minimum number
of operations needed to generate one string from a to b
This is implemented using dynamic programming
techniquie
 
For example we can consider to strings a = "benyam" and 
b = "ephrem" the minimum distance between these two string 
is 5 . For DP approach the dp array is calculated 
in following way

        1   2   3   4   5   6   7  
        ""  b   e   n   y   a   m
1   ""  0   1   2   3   4   5   6
2   e   1   1   1   2   3   4   5
3   p   2   2   2   2   3   4   5
4   h   3   3   3   3   3   4   5
5   r   4   4   4   4   4   4   5
6   e   5   5   4   5   5   5   5
7   m   6   6   5   5   6   6   5
    
we can create this array in O(|a| * |b|) time.
The result distance of these two string is 
array[|a|][|b|] = 5
so distance = 5
for matching similarity in percentage I used following
equation

percentage = (1 - distance/ max(|a|, |b|))%100
so the similarity between these two string is 
calculated would be 
percentage = (1 - 5/6)* 100 %
=16.66%

```