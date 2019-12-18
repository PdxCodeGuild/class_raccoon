#lab 17 number to phrase

ones_digit = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",7:"seven", 8:"eight", 9:"nine"}
tens_digit = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

def num_phrase(user_input):
    new_phrase = ""
    tens = int(user_input[0])
    ones = int(user_input[1])
    if tens >= 2:
        if ones == 0:
            new_phrase += tens_digit[tens]
            return(new_phrase)
        else:
            new_phrase += tens_digit[tens] +" " +ones_digit[ones]
            return(new_phrase)
    
    elif tens == 1 and ones == 1:
        return("eleven")
    elif tens == 1 and ones == 2:
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

        

user_input = list(input("Enter a number in the range of 0-99. ie 09,11,46\n:"))
print(num_phrase(user_input))