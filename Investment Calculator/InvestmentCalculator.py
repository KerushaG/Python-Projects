#Introduction to Programming, Task 12
#Kerusha Govender, (2019.05.06)
#[This program asks the user a series of questions, stores and calculates them to then display to the user their expected total income based from the choice of interest that
#they made.]

import math

currency = input("Enter the type of currency you're using: ")
P = float(input("Enter the amount that you are depositing, without the monetary symbol: "))
i = input("Enter the interest rate: ")
i_num = float(i.strip("%"))
rate = i_num / 100

roundsimple = 0
round_compound = 0
A = 0
interest = ' '

t = float(input("Enter the number of years the investment will accumulate interest for: "))
while interest != 'simple' or interest != 'compound': #I put a loop in case the user does not right the valid option
    interest = input("Enter which type of interest you want: 'simple' or 'compound' interest:")
    
    if interest == "simple":
        simple = P*(1+rate*t)
        roundsimple = round(simple,2)
        print("After " + str(t) + " years, you will get " + str(currency) + str(roundsimple) + " " + "at the interest rate of " + i + " percent.")
        break #as soon as they pick this or the one below, the loop breaks

    elif interest == "compound":
        A = P* math.pow((1+rate),t)
        round_compound = round(A,2)
        print("After " + str(t) + " years, you will get " + str(currency) + str(round_compound) + " " + "at the interest rate of " + i + " percent.")
        break

    else:
        print("You can only choose 'simple' or 'compound', try again.")

###########################################################################

#NOTES:
        
##import math
##
##r = 0
##percent_strip = 0
##rate = 0
##search = 0
##
##currency = input("Enter the type of currency you're using: ")
##P = float(input("Enter the amount that you are depositing, without the monetary symbol: "))
##
##i = input("Enter the interest rate: ")
###I am adding an if statement in case they enter the %, so I will search it to check if there is a percent, and if there is I will then strip it, cast it and
###divide it by 100 to get it ready for the calculation
###When the user enters a percentage symbol and a number, what does python register that as? A string or a number?
###In an if statement, if the user enters 67%, why can't I just say if i == '%':? or if the user enters "Yes I can and bla bla", can I say if i == "Yes", can't it just
###find the particular conditional value
###I am casting the input of i as a string seperately, so that it can be searched
##search = str(i)
##search_i = search.find('%')
##if search_i != -1:
##    percent_strip = search.strip("%")
##    rate = float(percent_strip)
##    #print(percent_strip)
##    r = rate / 100
##    #print(r)
###I had to store the stripped %number in its own variable called rate so that at the end when I print it doesn't say 6%percent.
##else:
##    rate = float(i)
##    r = rate / 100
##    #print(r)
##
##roundsimple = 0
##round_compound = 0
##A = 0
##
##t = float(input("Enter the number of years the investment will accumulate interest for: "))   
##interest = input("Enter which type of interest you want: 'simple' or 'compound' interest:")
##if interest == "simple":
##    A = P*(1+r*t)
##    #print(A)
##    roundsimple = round(A,2)
##    print("After " + str(t) + " years, you will get " + str(currency) + str(roundsimple) + " " + "at the interest rate of " + str(rate) + " percent.")
##
##elif interest == "compound":
##    A = P* math.pow((1+r),t)
##    round_compound = round(A,2)
##    print("After " + str(t) + " years, you will get " + str(currency) + str(round_compound) + " " + "at the interest rate of " + str(rate) + " percent.")
##
##else:
##    print("You can only choose 'simple' or 'compound', try again. \n")
##    interest = input("Enter if you would like 'simple' or 'compound' interest:")




 
    
    



    


  

    

    

