#Introduction to Programming, Task 25
#Kerusha Govender, 13 May 2019
#A program that reads a DNA sequence and returns the SLC code, another one that reads a text filewith a DNA sequence, finds a character and copiesthe content plus
#replacements of the character into two new files
#IMPORTANT QUESTION:
#I am not sure if I used stride parameter properly, because it didn't really work that simply in my code as opposed to i%3, please let me know if I misunderstood..

slcdict = {'ATT':'I', #made a global dictionary
           'ATC':'I',
           'ATA':'I',
           'CTT':'L',
           'CTC':'L',
           'CTA':'L',
           'CTG':'L',
           'TTA':'L',
           'TTG':'L',
           'GTT':'V',
           'GTC':'V',
           'GTA':'V',
           'GTG':'V',
           'TTT':'F',
           'TTC':'F',
           'ATG':'M'
           }

def translate(dna_input): #this is the main function
    dna_string = dna_input.upper() #incase of any discrepancies
    dna_length = len(dna_string)
    slc_code = get_codons(dna_length, dna_string)#calling the function below and carrying over info
    output =  print(slc_code, end= '')
    
def get_codons(dna_length, dna_string):#using a stride parameter which will ensure only every third character is iterated through
    slc_code = ''
    for i in range(0,dna_length+1,3): #however,I had to add +1, because in a sequence with perfect sets of 3, the iteration did not go to the last number, given that it starts iterating from zero
        if i != 0: #It starts iterating on zero and giving a default x Value
            codon = dna_string[i-3:i] #I kept this to check the sets of 3, and I said i-3 to create the range
            global slcdict
            if codon in slcdict:
                slc = slcdict[codon]
                slc_code += slc
            else:
                slc = 'X'
                slc_code += slc
    return slc_code
       
dna_input = input("Enter a DNA string: ")
translate(dna_input) #this is the only function I call

dna_file = open('DNA.txt', 'r', encoding='utf-8-sig').read() #does this mean it is not necessary to close the file, because when I did add close file at the end it errored and said this variable was a string
dna_string = (''.join(dna_file))

def mutate(): 
    global dna_string
    normal_file = open('normalDNA.txt', 'w', encoding='utf-8-sig')
    normal_replace = dna_string.replace('a', 'A')
    normal_file.write(normal_replace)
    normal_file.close()
    mutated_file = open('mutatedDNA.txt', 'w', encoding='utf-8-sig')
    mutated_replace = dna_string.replace('a', 'T')
    mutated_file.write(mutated_replace)
    mutated_file.close()

mutate() #thefunction called 
#dna_file.close() causes an error

#######################################################################################


###Original Version:
##def translate(dna_input): #this is the main function
##    dna_string = dna_input.upper() #incase of any discrepancies
##    dna_length = len(dna_string)
##    get_codons(dna_length, dna_string)#calling the function below and carrying over info
##    
##def get_codons(dna_length, dna_string):
##    for i in range(0,dna_length):
##        if i%3 == 0: #this is to break up the sequence into chunks of 3, if there is no chunk of 3 at the end, the program automatically calls it x
##            codon = dna_string[i: i + 3]
##            codon_check(codon) #takes this info to the function below
##
##slcdict = {'ATT':'I', #made a global dictionary
##           'ATC':'I',
##           'ATA':'I',
##           'CTT':'L',
##           'CTC':'L',
##           'CTA':'L',
##           'CTG':'L',
##           'TTA':'L',
##           'TTG':'L',
##           'GTT':'V',
##           'GTC':'V',
##           'GTA':'V',
##           'GTG':'V',
##           'TTT':'F',
##           'TTC':'F',
##           'ATG':'M'
##           }
##
##def codon_check(codon): #takes the chunks of 3, checks if it is in the dictionary and if it is stores the value in slc, otherwise it gets stored as X in else
##    global slcdict
##    if codon in slcdict:
##        slc = slcdict[codon]
##    else:
##        slc = 'X'
##    output(slc) #calling the function below, slc is carried over
##
##def output(slc):
##    y = '' #so that y can accumulate all the slc codes on one line
##    y += slc
##    print(y, end= '')
##    return y
############################################################
##
##dna_input = input("Enter a DNA string: ")
##translate(dna_input) #this is the only function I call
##
############################################################
##dna_file = open('DNA.txt', 'r', encoding='utf-8-sig')
##dna = dna_file.readlines() #this was in list
##dna_string = (''.join(dna)) #so I made it one big string
###I didn't put the above in the mutate function because I needed it later for the other executions outside the function
##def mutate(): #created the function and made dna_string global
##    global dna_string
##    search = dna_string.find('a')
##    print('\n',search) #for some reason it prints the index on the same line as the slc code, I added \n
##
##mutate() #thefunction called 
##dna_file.close()

############################################################
##ORIGINAL CODE
##normal_file = open('normalDNA.txt', 'w', encoding='utf-8-sig')
###I'm using the text string here 
##normal_replace = dna_string.replace('a', 'A')
##normal_file.write(normal_replace)
##
##normal_file.close()
##
############################################################
##
##mutated_file = open('mutatedDNA.txt', 'w', encoding='utf-8-sig')
###I'm using the text string here 
##mutated_replace = dna_string.replace('a', 'T')
##mutated_file.write(mutated_replace)
##
##mutated_file.close()
###########################################################




