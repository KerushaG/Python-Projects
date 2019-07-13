#Introduction to Programming, Task 24.2
#Kerusha Govender, 2019.05.13
#A program that asks the user for the amount of nights they wish to stay at a hotel, the amount of days they would like to rent a car for and the flight that they want
#to take.
#-----------------------
#improved variable names
def hotel_cost(nights):
    hotel_price = nights * 688
    return hotel_price

def car_rental(days):
    car_price = days * 480.5
    return car_price

def location_menu():
    location = 0
    cities = ['Port Elizabeth', 'Durban', 'Cape Town', 'Bloemfontein', 'Johannesburg']
    for index, item in enumerate (cities, 1):
        print("{0}.{1}".format(index, item))
    print('6. I changed my mind, I want to exit this program.')
    while location < 1 or location > 6:
        location = int(input("From which city will you be taking a flight? Type in a number(1-6): "))
        if location >= 1 and location <= 5:
            your_options(location)
        elif location == 6:
            break
    
def your_options(location):
    cities = ['Port Elizabeth', 'Durban', 'Cape Town', 'Bloemfontein', 'Johannesburg']
    num = (int(location) - 1)
    city = cities[num]
    choice = 0
    cities.pop(num)
    for index, item in enumerate (cities, 1):
        print("{0}.{1}".format(index, item))
    print('5. Take me back to the previous menu.')
    print('6. I changed my mind, I want to exit this program.')
    while choice < 1 or choice > 6:
        choice = int(input("Which city would you like to fly to? Type in a number (1-6): "))
        if choice == 6:
            break
        elif choice == 5:
            location_menu()
        elif choice >= 1 and choice <= 4:
            flight = cities[choice-1]
            price_loop(city, flight)
        
def price_loop(city, flight):
    if city == 'Port Elizabeth':
        pe_prices(flight)
    elif city == 'Durban':
        durb_prices(flight)
    elif city == 'Cape Town':
        ct_prices(flight)
    elif city == 'Bloemfontein':
        bloem_prices(flight)
    elif city == 'Johannesburg':
        joburg_prices(flight)
            
def pe_prices(flight):
    dict_pe = {'Durban': '750',
              'Cape Town': '500',
              'Bloemfontein': '880',
              'Johannesburg':'1500'
              }
    value = dict_pe[flight]
    num_value = int(value)
    global travel_cost
    travel_cost += num_value  

def durb_prices(flight):
    dict_durb = {'Port Elizabeth': '780',
                'Cape Town': '2100',
                'Bloemfontein': '800',
                'Johannesburg':'1999'
                }
    value = dict_durb[flight]
    num_value = int(value)
    global travel_cost
    travel_cost += num_value
           
def ct_prices(flight):
    dict_ct = {'Port Elizabeth': '999',
              'Bloemfontein': '889',
              'Durban': '2500',
              'Johannesburg':'2354'
              }
    value = dict_ct[flight]
    num_value = int(value)
    global travel_cost
    travel_cost += num_value
    
def bloem_prices(flight):
    dict_bloem = {'Port Elizabeth': '600',
                 'Durban': '500',
                 'Cape Town': '879',
                 'Johannesburg':'998'
                 }
    value = dict_bloem[flight]
    num_value = int(value)
    global travel_cost
    travel_cost += num_value
    
travel_cost = 0

def joburg_prices(flight):
    dict_joburg = {'Port Elizabeth': '1000',
                  'Bloemfontein': '970',
                  'Cape Town': '1880',
                  'Durban':'2120'
                  }
    value = dict_joburg[flight]
    num_value = int(value)
    global travel_cost
    travel_cost += num_value
    
def costs(nights, days):#improvement made here
    location_menu()
    total = hotel_cost(nights) + car_rental(days) + travel_cost
    print("The total cost of your holiday is R" + str(total))
    

########################################################################

nights = int(input("How many nights will you spend at the hotel? "))
days = int(input("For how many days will you hire the car? "))
costs(nights, days) #improvement made here 

###############################################################
#ORIGINAL VERSION
#I made standard functions for the hotel and the car rental costs. When it came to the flights, I wanted to introduce choices, based on where the user would be flying
#from which would also affect the cost of where they choose to fly too. So I made a sort of menu with options for them to choose where they would be flying from and
#another menu that would show them the options they would have to fly too based on their choice of location. I also used while loops and if statements to ensure
#the user can go back and forth between the menus, exit when they want, and get asked the question again if they type in an invalid number. Once they've chosen their
#destination, I made a price loop definition, which directs their choices to the relevant dictionary functions. These dictionaries are based on the location choice. So
#for example, if I am from PE then where can I go and how much will it cost. These dictionary functions using user's choice of destination, then accesses the value
# or price of that destination and prints a statement out for the user. At the end of each of the dictionary functions, I used a global variable to send the cost of
#the flight to another function that calculates the sum of everything all together.
#After all the functions are created I ask the user questions about the rental and accommodation and store their answers in variables. To display the flight menus, I just
#call one function - location_menu. Then to get the entire calculation I call the costs function and add the variables of the rental and accommodation as its arguments.

##def HotelCost(nights):
##    y = nights * 688
##    return y
##
##def CarRental(days):
##    a = days * 480.5
##    return a
##
##def location_menu():
##    location = 0
##    cities = ['Port Elizabeth', 'Durban', 'Cape Town', 'Bloemfontein', 'Johannesburg']
##    for index, item in enumerate (cities, 1):
##        print("{0}.{1}".format(index, item))
##    print('6. I changed my mind, I want to exit this program.')
##    while location < 1 or location > 6:
##        location = int(input("From which city will you be taking a flight? Type in a number(1-6): "))
##        if location >= 1 and location <= 5:
##            YourOptions(location)
##        elif location == 6:
##            break
##    
##def YourOptions(location):
##    cities = ['Port Elizabeth', 'Durban', 'Cape Town', 'Bloemfontein', 'Johannesburg']
##    num = (int(location) - 1)
##    city = cities[num]
##    choice = 0
##    cities.pop(num)
##    for index, item in enumerate (cities, 1):
##        print("{0}.{1}".format(index, item))
##    print('5. Take me back to the previous menu.')
##    print('6. I changed my mind, I want to exit this program.')
##    while choice < 1 or choice > 6:
##        choice = int(input("Which city would you like to fly to? Type in a number (1-6): "))
##        if choice == 6:
##            break
##        elif choice == 5:
##            location_menu()
##        elif choice >= 1 and choice <= 4:
##            flight = cities[choice-1]
##            priceloop(city, flight)
##        
##def priceloop(city, flight):
##    if city == 'Port Elizabeth':
##        PEprices(flight)
##    elif city == 'Durban':
##        Durbprices(flight)
##    elif city == 'Cape Town':
##        CTprices(flight)
##    elif city == 'Bloemfontein':
##        Bloemprices(flight)
##    elif city == 'Johannesburg':
##        Joburgprices(flight)
##            
##def PEprices(flight):
##    dictPE = {'Durban': '750',
##              'Cape Town': '500',
##              'Bloemfontein': '880',
##              'Johannesburg':'1500'
##              }
##    value = dictPE[flight]
##    x = int(value)
##    global travelcost
##    travelcost += x
##    print("The cost of your flight is R" + str(travelcost))   
##
##def Durbprices(flight):
##    dictDurb = {'Port Elizabeth': '780',
##                'Cape Town': '2100',
##                'Bloemfontein': '800',
##                'Johannesburg':'1999'
##                }
##    value = dictDurb[flight]
##    x = int(value)
##    global travelcost
##    travelcost += x
##    print("The cost of your flight is R" + str(travelcost))
##           
##def CTprices(flight):
##    dictCT = {'Port Elizabeth': '999',
##              'Bloemfontein': '889',
##              'Durban': '2500',
##              'Johannesburg':'2354'
##              }
##    value = dictCT[flight]
##    x = int(value)
##    global travelcost
##    travelcost += x
##    print("The cost of your flight is R" + str(travelcost))
##    
##def Bloemprices(flight):
##    dictBloem = {'Port Elizabeth': '600',
##                 'Durban': '500',
##                 'Cape Town': '879',
##                 'Johannesburg':'998'
##                 }
##    value = dictBloem[flight]
##    x = int(value)
##    global travelcost
##    travelcost += x
##    print("The cost of your flight is R" + str(travelcost))
##    
##travelcost = 0
##
##def Joburgprices(flight):
##    dictJoburg = {'Port Elizabeth': '1000',
##                  'Bloemfontein': '970',
##                  'Cape Town': '1880',
##                  'Durban':'2120'
##                  }
##    value = dictJoburg[flight]
##    x = int(value)
##    global travelcost
##    travelcost += x
##    print("The cost of your flight is R" + str(travelcost))
##    
##
##def costs(carprice, hotelprice):
##    TOTAL = travelcost + carprice + hotelprice
##    print("The total cost of your holiday is R" + str(TOTAL))
##    return TOTAL
##
##########################################################################
##
##nights = int(input("How many nights will you spend at the hotel? "))
##hotelprice = HotelCost(nights)
##print("The cost of your accommodation is R" + str(hotelprice))
##days = int(input("For how many days will you hire the car? "))
##carprice = CarRental(days)
##print("The cost of your car rental is R" + str(carprice))
##location_menu()
##costs(carprice, hotelprice)


