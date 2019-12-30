#lab09_unitconv.py

#Version 1
feet = {
"meters": 0.3048
}

dist = ""
while isinstance(dist, float) == False:
    dist = input("Let's convert to meters. What is the distance in feet? ")
    try:
        dist = float(dist)
    except ValueError:
        print("Invalid entry!")

conv = round(dist*feet["meters"], 4)
print(f"{dist} feet = {conv} meters")

#Version 2
meters = {
"feet": 0.3048,
"miles": 1609.34,
"meters": 1,
"kilometers": 1000
}

unit = ""
while unit not in meters.keys():
    unit = input("Let's do more metric conversions. What unit are you using: feet, miles, meters, or kilometers? ").casefold()
dist = float(input(f"What is the distance in {unit}? "))

conv = round(dist*meters[unit], 4)
print(f"{dist} {unit} = {conv} meters.")

#Version 3 - Add yards and inches
meters["yards"] = 0.9144
meters["inches"] = 0.0254

unit = ""
while unit not in meters.keys():
    unit = input("Let's do more metric conversions. What unit are you using: feet, miles, meters, kilometers, yards, or inches? ").casefold()
dist = float(input(f"What is the distance in {unit}? "))

conv = round(dist*meters[unit], 4)
print(f"{dist} {unit} = {conv} meters.")

#Version 4 - Unit to unit conversions
unit = ""
while unit not in meters.keys():
    unit = input("Now let's convert between units. What unit are you using: feet, miles, meters, kilometers, yards, or inches? ").casefold()
dist = float(input(f"What is the distance in {unit}? "))

enunit = ""
while enunit not in meters.keys():
    enunit = input("And what unit would you like to convert to: feet, miles, meters, kilometers, yards, or inches? ").casefold()

conv = round(dist*meters[unit]*(1/meters[enunit]), 4)
print(f"{dist} {unit} = {conv} {enunit}.")
