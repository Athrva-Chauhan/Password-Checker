
import re

#re stands for 'regular experissons' , it is a expression that helps you match or find other strings or sets of strings,

paswd=input("Enter Your Password: ")
if not re.search('[a-z]',paswd):
    print("Your Password Does not contain lowercase !!!")

if not re.search('[A-Z]',paswd):
    print("Your Password Does not contain Uppercase !!!")

if not re.search('[0-9]',paswd):
    print("Your Password Does not contain Numbers !!!")

if not re.search('[!$&*£@#^%&+-/]',paswd):
    print("Your Password Does not contain any Special Character !!!")

if len(paswd)<9:
    print("Your Password is too short !!!")

else:
    print("Yor Password is Perfect :-) ")
