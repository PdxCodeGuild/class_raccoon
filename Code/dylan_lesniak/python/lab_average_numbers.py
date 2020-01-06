'''
Filename: lab_average_numbers.py
Author: Dylan
Purpose: Create average, median, and mode for a given list of inputs. 
'''

import helper 
.
def get_list(): #going to take the user's numbers and return them into a list which will be returned.
    done = "no" #This list will then be passed into other functions as necessary. 
    current_nums = []
    while done != "done":
        print("Please enter a number to be placed into the list. ")
        print("Or enter 'done' if you would like to move on.")
        num = input("> ")
        try: #this part to avoid errors while checking for text and digits
            num.lower()
            if num.lower() == "done":
                break
        except:
            pass
            
        num = int(helper.digit_checker(num))
        current_nums.append(num)
        print(f"The current number list is: {current_nums}.\n")
    return current_nums

def ave(current_nums):
    sumation = 0
    for num in current_nums:
        sumation += num
    average = sumation / len(current_nums)
    print(f"The average of the list is: {average}") #a basic formula to get the sum without using the sum function, divided by num elements. 

def median(current_nums):
    current_nums.sort()
    if len(current_nums) % 2 == 0:
        median_idx = len(current_nums) // 2
        median_list = [current_nums[median_idx],current_nums[median_idx + 1]] #the middlemost two values
        print(median_list)



if __name__ == "__main__":
    user_list = get_list()
    ave(user_list)
    median(user_list)
    #mode(user_list)