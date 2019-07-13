#Introduction to Programming, Task 20
#Kerusha Govender, 06.05.2019
#[A program that reads one text file, makes a calculation on them and writes the results of the lines into a new text file.]


file_input = open('input.txt', 'r+', encoding='utf-8-sig')
file_output = open('output.txt', 'w', encoding='utf-8-sig')

def convert_line(): #This is the main function that I call; it goes through every line in the file
    for line in file_input:
        line_word = line.split(":") #splits the word from the numbers
        num_set = line_word[-1].strip() #strips the spaces from the end of the line
        num_list = num_set.split(",") #makes the numbers into its own list
        int_numbers = [int(element) for element in num_list] #casts list into one of numbers so I can use list methods on it
        calculated_result = line_check(line_word, int_numbers) #this function takes the variables and passes it to a function that checks which calculation needs to be performed
        output(line_word, num_set, calculated_result) #the result of the above function is stored in the variable, and used to call a function which puts the string
        #together and writes the line to the new file

def line_check(line_word, int_numbers): #This function makes sure the right calculation is performed on the list of numbers for every line with the relevant word
    if "min" == line_word[0]:
        minimum = extract_min(int_numbers)
        return minimum
    elif "max" == line_word[0]:
        maximum = extract_max(int_numbers)
        return maximum
    elif "avg" == line_word[0]:
        average = extract_avg(int_numbers)
        return average

def output(line_word, num_set, calculated_result): #This function just takes chunks of the line and concatanates them in a string to be written to the new file
    new_file = ("The " + (line_word[0]) + " of " + "[" + num_set + "]" + " is " + str(calculated_result) + "\n")
    file_output.write(new_file)   
#these are the calculation functions
def extract_min(int_numbers):
    result = min(int_numbers)
    return result

def extract_max(int_numbers):
    result = max(int_numbers)
    return result

def extract_avg(int_numbers):
    len_numbers = len(int_numbers)
    sumof = sum(int_numbers)
    result = round((sumof / len_numbers), 2)
    return result
#this is the only function I call:    
convert_line()

file_input.close()
file_output.close()

###########################################################
#Version1
#I opened the 'input' text file in read and write mode using the encoding as well
#Then I opened 'output' text file in write mode
#I created one function for each operation and in each one I:
#First split the line into two items, one with the word and the other with the set of numbers. I had to clear the '\n' from the numbers item, and split them by "," 
#to get them as individual items in a list.
#The I used list comprehension to cast each item as an int, so that I could use the min, max, sum list methods.
#I also created a function to calculate the average for 'avg', so once I got the total and using len, the amount of numbers, I just called the function, in the
#extractAvg function.
#I also created a function to return string input which contains the result to be written into the new file
#After creating functions I:
#Used the for loop to read the lines in 'input', and used if statements, so that the conditions would ensure the right statements are executed for the right lines,
#regardless whether 'min' is on line one or line four.
#I called the function in each if statement and stored it in a variable.
#I used the file write function in each if statement, because if there were more than one line with min, max, or avg it would capture all those lines in the new file
#not just the last one it read and I used \n to ensure each is written on a new line

##file1 = open('input.txt', 'r+', encoding='utf-8-sig')
##file2 = open('output.txt', 'w', encoding='utf-8-sig')
####numSet > num_set
####numSet1 > num_set1
####numSet1_List > num_set1_list
####IntNumbers > int_numbers
####output > output_string
##
##
##def convert_line(line):
##    line_min = line.split(":")
##    numSet1 = line_min[-1].strip()
##    numSet1_List = numSet1.split(",")
##    IntNumbers = [int(element) for element in numSet1_List]
##    
##
##def output(line_word, index, numSet, answer):
##    return("The " + (line_word[index]) + " of " + "[" + numSet + "]" + " is " + str(answer))
##
##def extractMin(line):
##    line_min = line.split(":")
##    numSet1 = line_min[-1].strip()
##    numSet1_List = numSet1.split(",")
##    IntNumbers = [int(element) for element in numSet1_List]
##    minimum = min(IntNumbers)
##    output1 = output(line_min, 0, numSet1, minimum)
##    return output1
##
##def extractMax(line):
##    line_max = line.split(":")
##    numSet2 = line_max[-1].strip()
##    numSet2_List = numSet2.split(",")
##    IntNumbers = [int(element) for element in numSet2_List]
##    maximum = max(IntNumbers)
##    output2 = output(line_max, 0, numSet2, maximum)
##    return output2
##
##def average(total = 0, num = 0):
##    AvCalc =(round((total / num), 2))
##    return AvCalc
##
##def extractAvg (line):
##    line_avg = line.split(":")
##    numSet3 = line_avg[-1].strip()
##    numSet3_List = numSet3.split(",")
##    IntNumbers = [int(element) for element in numSet3_List]
##    total = sum(IntNumbers)
##    num = len(numSet3_List)
##    avg = average(total, num)
##    output3 = output(line_avg, 0, numSet3, avg)
##    return output3
##
##
##for line in file1:
##    if "min" in line:
##        output1 = extractMin(line) + "\n"
##        file2.write(output1)
##    elif "max" in line:
##        output2 = extractMax(line) + "\n"
##        file2.write(output2)
##    elif "avg" in line:
##        output3 = extractAvg(line) + "\n"
##        file2.write(output3)
##    
##
##file1.close()
##file2.close()

