


def combine(keys, values):
    d = {}
    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        d[key] = value
    return d
    
def average(d):
    avg = 0
    for key in d:
        avg += d[key]
    return avg/len(d)
    
    # return sum(d.values())/len(d)


fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
fruit_dict = combine(fruits, prices) # {'apple':1.2, 'banana':3.3, 'pear':2.1}
print(fruit_dict)
print(average(fruit_dict)) # 2.2






def average_letters(d):
    
    # {'a': [5, 2, 3], 'b': [10, 1, 1], 'c': [4, 5, 6]}
    letter_list_dict = {}
    for key in d:
        letter = key[0]
        value = d[key]
        # check if letter is in letter_list_dict
        if letter in letter_list_dict:
            # append the value to the list for that key (letter)
            letter_list_dict[letter].append(value)
        else:
            # if not, add a new list with the value as the only element
            letter_list_dict[letter] = [value]
    # print(letter_list_dict)
    for key in letter_list_dict:
        letter_list_dict[key] = sum(letter_list_dict[key])/len(letter_list_dict[key])
    return letter_list_dict
    
    
    # totals = {}
    # counts = {}
    # for key in d:
    #     letter = key[0]
    #     value = d[key]
    #     if letter in totals:
    #         totals[letter] += value
    #         counts[letter] += 1
    #     else:
    #         totals[letter] = value
    #         counts[letter] = 1
    # for letter in totals:
    #     totals[letter] /= counts[letter]
    # return totals
    
        
        
            
# round(2.333333, 2) # 2.33
        

d = {'a1':5, 'a2':2, 'a3':2, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
print(average_letters(d)) # {'a':3, 'b':4, 'c':5}

