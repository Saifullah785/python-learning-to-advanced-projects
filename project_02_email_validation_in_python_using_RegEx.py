# a-z      
# 0-9
# . __time 1
# @ time 1
# - .2,3
# importing regex module



# in regex "^" is used for starting [a-z].

# in regex "+" is work for joining  +.

# in regex "\" is used for searching [\._].

# in regex "?" is used for 1 or 0 like Yes or No.
# [a-z 0-9]+[@]\w+[.]\w{2,3}

# in regex "$" is used for reverse search

# declear the variable

import re

email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

# variable for getting user input 

user_email=input("Enter your Email :")

#  

if re.search(email_condition,user_email):

    print("Sir,your Entered a Right Email ")
else:
    print("you entered a Wrong Email: ")    