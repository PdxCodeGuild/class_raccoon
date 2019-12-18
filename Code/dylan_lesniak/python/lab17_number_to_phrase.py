'''
Filename: lab17_number_to_phrase.py
Author: Dylan
Purpose: Take input and convert int to phrase. Assume 0-999
'''
import helper

def convert(num):
    if num == "0":
        return "zero"
    singles_dict = {"0":"","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    num_list = list(num)
    num_str = ""
    while len(num_list) > 0:
        if len(num_list) == 3:
            num_str += singles_dict[num_list[0]] + " hundred "
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
    tens_dict = {"2":"twenty ", "3":"thirty ","4":"forty ","5":"fifty ","6":"sixty ","7":"seventy ","8":"eighty ","9":"ninety "}
    return tens_dict[num_list[0]] 
    

def teens(num_list):
    num = "".join(num_list)
    teens_dict = {"10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", "15":"fifteen","16":"sixteen","17":"seventeen","18":"eighteen","19":"nineteen"}
    return teens_dict[num]
    
    

if __name__ == "__main__":
    cont = 'y'
    while cont == 'y':
        print("Please enter number to convert to text: ")
        number = helper.digit_checker(input("> "),3)
        print(convert(number))