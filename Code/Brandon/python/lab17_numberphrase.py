#lab 17 number to phrase

ones_digit = {0: "", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",7:"seven", 8:"eight", 9:"nine"}
tens_digit = {0:"",1: "ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}



#Fuction for calculating hundreds if the value is 3 items in list.
def num_hundreds(user_input):
    new_phrase = ""
    hundreds = int(user_input[0])
    tens = int(user_input[1])
    ones = int(user_input[2])
    new_phrase += ones_digit[hundreds] + " "+ "hundred" +" " + tens_digit[tens] +" "+  ones_digit[ones]
    return(new_phrase)


#Function for calculating tens and ones if the value is 2.
def num_phrase(user_input):
    new_phrase = ""
    tens = int(user_input[0])
    ones = int(user_input[1])
    if tens == 0 and ones == 0:
        return("Zero")
    elif tens == 0:
        new_phrase += ones_digit[ones]
        return(new_phrase)        
    elif ones == 0:
        new_phrase += tens_digit[tens]
        return(new_phrase)
    elif tens == 1 and ones == 0:
        return("ten")
    else:
        new_phrase += tens_digit[tens] +" " +ones_digit[ones]
        return(new_phrase)

#Function for teens if the tens value is 1
def num_teen(user_input):
    tens = int(user_input[0])
    ones = int(user_input[1])

    
    if tens == 1 and ones == 2:
        return("twelve")
    elif tens == 1 and ones == 3:
        return("thirteen")
    elif tens == 1 and ones == 4:
        return("fourteen")
    elif tens == 1 and ones == 5:
        return("fifteen")
    elif tens == 1 and ones == 6:
        return("sixteen")
    elif tens == 1 and ones == 7:
        return("seventeen")
    elif tens == 1 and ones == 8:
        return("eighteen")
    elif tens == 1 and ones == 9:
        return("nineteen")

def check_num(value,user_input):
    tens = int(user_input[0])
    ones = int(user_input[1])
    

    # if value == 2 and tens + ones <= 9:
    #     print(num_phrase(user_input))
    if value == 2:
        if tens == 1:
            print(num_teen(user_input))
        elif tens >= 2:
            print(num_phrase(user_input))
        elif value == 2: 
            print(num_phrase(user_input))
    elif value == 3:
        hundreds = int(user_input[2])
        print(num_hundreds(user_input))
    


 

        
user_input = list(input("Enter a number in the range of 0-99. ie 09,11,46\n:"))
value = int(len(user_input))
# print(value)
check_num(value,user_input)

