#Introduction to Programming, Task 12
#Kerusha Govender, (2019.04.11)
#[Program that generates a random two digit number between 10 - 99, and then asks user to guess a number, and compares the two numbers, generating certain statements
#if a number of conditions are met]
import sys
from random import *
lottery_num = randint(10, 99)
#In case the user's input is not a two digit I wanted to put some conditions but it got really complicated so I found the exit function online
#I got this from another site, it was hard to find how to perform this, because import random wasn't working
#In case the user does not follow instructions I check that it is a two digit number by using len, and a condition
user_guess = int(input("Enter any two-digit number between 10 and 99: "))
user_guess_str = str(user_guess)
userlen = len(user_guess_str)
if userlen!=2:
    sys.exit(print("You did not enter a two-digit number, game over."))
user_guess1 = user_guess_str[0]
user_guess2 = user_guess_str[1]
lottery_str = str(lottery_num)
lotterynum1 = lottery_str[0]
lotterynum2 = lottery_str[1]
reverseguess = user_guess_str[::-1]
reverse_guess = int(reverseguess)
print("The lottery number is " + str(lottery_num))
if (lottery_num == user_guess):
    print("Congratulations you have an exact match, you win R10 000.00.")
elif (lottery_num == reverse_guess):
    print("Congratulations you have all digits, you win R5000.00.")
elif (lotterynum1 == user_guess1) or (lotterynum2 == user_guess2) or (lotterynum2 == user_guess1) or (lotterynum1 == user_guess2):
    print("Congratulations you have one correct digit, you win R1000.00.")
else:
    print("Sorry no match.")

#I pulled the user's input and the generated number apart by casting them as string and using index, storing the individual pieces in variables for conditions
#I know it's a two digit number, so I can call out the precise index
#The easiest way to check if both numbers match but not in the order is to reverse it as a string

#try to put in a loop

        
