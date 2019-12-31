'''
Filename: crime_data.py
Author: Dylan
Purpose: Analyze text list of crimes
'''

#mods

#variables & variable methods
with open('crimes.csv','r') as f:
    all_info = f.read()

lines = all_info.split('\n')
lines = [line for line in lines if line != ""]
lines = [line.strip(" ") for line in lines]
headers_list = lines[0].split(",")
lines = lines[1:]

#goals:
'''
    The specific most common crime type.
    The rarest crimes.
    The year with the most crime.
'''

def get_crime_stats(lines):
    crime_type_dict = dict_of_type(lines,"Offense Type")
    year_crime_count = dict_of_date(lines)

    max_crime_type = max_val_dict(crime_type_dict)
    max_crime_amt = crime_type_dict[max_crime_type]
    min_crime_type = min_val_dict(crime_type_dict)
    min_crime_amt = crime_type_dict[min_crime_type]

    max_crime_year = max_val_dict(year_crime_count)
    max_year_amt = year_crime_count[max_crime_year]
    print(f"The most commited crime is {max_crime_type} with a count of {max_crime_amt}.")
    print(f"The least commited crime is {min_crime_type} with a count of {min_crime_amt}.")
    print(f"The year with the most crimes was {max_crime_year} with a count of {max_year_amt} crimes.")

def dict_of_type(lines, data_type):
    type_dict = {}
    type_index = headers_list.index(data_type) 
    for line in lines: #populates the crime dict with counts for each crime
        element_list = line.split(",")
        offense_type = element_list[type_index]
        if offense_type in type_dict:
            type_dict[offense_type] += 1
        else:
            type_dict[offense_type] = 1
    return type_dict

#the date method is identical to the dict_of_type except that it needs an extra step to get just the years. 
def dict_of_date(lines):
    type_dict = {}
    type_index = headers_list.index("Occur Date") 
    for line in lines: #populates the crime dict with counts for each crime
        element_list = line.split(",")
        offense_date = element_list[type_index]
        offense_year = offense_date.split("/")[2]
        if offense_year in type_dict:
            type_dict[offense_year] += 1
        else:
            type_dict[offense_year] = 1
    return type_dict

def max_val_dict(crime_type_dict):
    v=list(crime_type_dict.values())
    k=list(crime_type_dict.keys())
    return k[v.index(max(v))]

def min_val_dict(crime_type_dict):
    v=list(crime_type_dict.values())
    k=list(crime_type_dict.keys())
    return k[v.index(min(v))]

if __name__ == "__main__":
    get_crime_stats(lines)



