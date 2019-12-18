'''
Filename: lab17_number_to_phrase.py
Author: Dylan
Purpose: Take input and convert int to phrase. Assume 0-999
'''
import helper

def choose_method():
    acceptable_inputs = ["Roman", "Time", "Number"]
    print("Would you like to get Roman Numerals / Time / Number Text? (Roman/Time/Number)")
    method = helper.text_checker(input("> ").capitalize(),acceptable_inputs)
    if method == "Roman":
        print("Please enter a number to convert to Roman Numerals. (Hail Kaiser)")
        number = helper.digit_checker(input("> "),3)
        print(roman_convert(number))
    elif method == "Number":
        print("Please enter number to convert to text: ")
        number = helper.digit_checker(input("> "),3)
        print(convert(number))
    elif method == "Time":
        time_convert()
    else:
        print("You entered an invalid input but somehow got through my checks... NOW WE BOTH HAVE TO QUIT. \nHOPE YOU'RE HAPPY.")
        exit()

def convert(num):
    if num == "0":
        return "zero"
    singles_dict = {"0":"","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
    num_list = list(num)
    num_str = ""
    while len(num_list) > 0:
        if len(num_list) == 3:
            num_str += singles_dict[num_list[0]] + " Hundred "
            num_list = num_list[1:]
        elif 20 <= int("".join(num_list)) <= 99:
            num_str += tens(num_list)
            num_list = num_list[1:]
        elif 10 <= int("".join(num_list)) <= 19:
            num_str += teens(num_list)
            return num_str
        else:
            num_str += singles_dict[num_list[-1]] #this avoids errors if number left over is like, 09. 
            return num_str
    
def tens(num_list):
    tens_dict = {"2":"Twenty ", "3":"Thirty ","4":"Forty ","5":"Fifty ","6":"Sixty ","7":"Seventy ","8":"Eighty ","9":"Ninety "}
    return tens_dict[num_list[0]] 
    

def teens(num_list):
    num = "".join(num_list)
    teens_dict = {"10":"Ten", "11":"Eleven", "12":"Twelve", "13":"Thirteen", "14":"Fourteen", "15":"Fifteen","16":"Sixteen","17":"Seventeen","18":"Eighteen","19":"Nineteen"}
    return teens_dict[num]

def roman_convert(num):
    if num == "0":
        return "Zero"
    num_list = list(num)
    num_str = ""
    while len(num_list) > 0:
        if len(num_list) == 3:
            num_str += roman_hundreds(num_list)
            num_list = num_list[1:]
        elif 1 < len(num_list) <= 2:
            num_str += roman_tens(num_list)
            num_list = num_list[1:]
        else:
            num_str += roman_singles(num_list) #this avoids errors if number left over is like, 09. 
            return num_str

def roman_hundreds(num_list):
    hundreds = {"0":"","1":"C","2":"CC","3":"CCC","4":"CD","5":"D","6":"DC","7":"DCC","8":"DCCC","9":"CM"}
    return hundreds[num_list[0]]
   
def roman_tens(num_list):
    tens_dict = {"1":"X","2":"XX ", "3":"XXX ","4":"XL ","5":"L ","6":"LX ","7":"LXX ","8":"LXXX ","9":"XC"}
    return tens_dict[num_list[0]] 

def roman_singles(num_list):
    singles_dict = {"0":"","1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"IIX","9":"IX"}
    return singles_dict[num_list[0]]

def time_convert():
    print("Please enter a time in this format EXACTLY: 00:00")
    time_halves = helper.time_checker(input("> "))
    first_half = "".join(time_halves[0])
    second_half = "".join(time_halves[1])
    print(convert(first_half), end = " ")
    print(convert(second_half))

    

if __name__ == "__main__":
    cont = 'y'
    while cont == 'y':
        choose_method()
        print("Would you like to start over? (y/n)")
        cont = input("> ").lower()
