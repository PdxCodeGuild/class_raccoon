# #Converting units to other units
# #functions
# units = {
# "ft": .3048,
# "mi": 1609.34,
# "m": 1,
# "km": 1000,
# "yd": .9144,
# "in": .0254
# }

# def meter_converter(user_input, user_unit):
#     return user_input * units[user_unit]

# #logic
# user_unit = input("What kind of unit would you like to convert? (ft, mi, km, m, yd, in)  ").lower()
# user_input = int(input("How many would you like to convert? "))
# result = meter_converter(user_input, user_unit)
# print(f"That equals {result} meters.")


#Converting units to other units
#functions
units = {
"ft": .3048,
"mi": 1609.34,
"m": 1,
"km": 1000,
"yd": .9144,
"in": .0254
}

def meter_converter(user_input, user_unit):
    return user_input * units[user_unit] 

#logic
user_unit = input("What kind of unit would you like to convert? (ft, mi, km, m, yd, in)  ").lower()
user_input = int(input("How many would you like to convert? "))
user_change = input("What would you like to converti them to?").lower()
result = meter_converter(user_input, user_unit) / units[user_change]
print(f"{user_input}{user_unit} is {result} {user_change}")