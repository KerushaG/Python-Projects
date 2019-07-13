
total = 0

import sys
package = float(input("Enter the price of the package that you would like to purchase:"))
if package <= 0:
    sys.exit(print("You did not enter a valid amount."))
total += package
#make condition for package needing to be more than zero
distance = float(input("Enter the total distance of delivery in kilometers:"))
urgency = input("Is this an urgent delivery? (Yes or No): ")
method = input("Would you like a delivery by air fare? (Yes or No):")
insure = input("Do you want insurance? (Yes or No)")
if insure == "Yes":
    full = input("Do you want full insurance? If you answer no, we will default to limited insurance. (Yes or No)")
    if full == "Yes":
        total += 50.00
    else:
        total += 25.00
    
Gift = input("Do you want a gift? (Yes or No):")

if urgency == "Yes":
    total += 100.00
  
else:
    total += 20.00
  
if method == "Yes":
    total += (distance * 0.36)

else:
    total += (distance * 0.25)

if Gift == "Yes":
    total += 15.00

Total = round(total, 2)
print("The total cost is R" + str(Total) + ".")


#This did not work because the total value could be 1000s or more, so how do I present the total in Rands rounded up to two degits after the decimal? use the round function

    
