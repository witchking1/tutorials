#!/usr/bin/python3 

import random 

computer_number = random.randint(1,100)
tries = 0
print("i am thinking of a number between 1 and 100 what's the number")
while True:
  user_number = int(input())
  
  if user_number < computer_number:
    print("number is greater than {}".format(user_number))
    tries+=1
  elif user_number > computer_number:
    print("number is less than {}".format(user_number))
    tries+=1
  else:
    print("Success!...you had {} tries".format(tries))
    break 
  