import string
excl=string.ascii_lowercase+string.whitespace
#unit names that occur inside of other unit names must be added after the larger named unit (kilometer must be before meter)
multiplier={"kilometer":1000, "meter":1, "feet":0.3048, "foot":0.3048, "mile":1609.34, "yard":0.9144, "inch":0.0254}
while True:
    usin=input("Please input measurement and units(meters, kilometers, inches, feet, yards, miles)(example: 4 miles): ").lower()
    try:
        usnumb=float("".join(char for char in usin if char not in excl))
    except ValueError:
        input("Please enter a valid number and unit of measurement.")
        continue
    usmeters=0
    for unit in multiplier:
        if usin.find(unit) != -1:
            usmeters=usnumb*multiplier[unit]
            break
    if usmeters == 0 and usmeters != usnumb:
        input("Please enter a valid number and unit of measurement.")
        continue
    while True:
        out_unit=input("please choose an output unit: ").lower()
        clean_unit="".join(char for char in out_unit if char not in "s")
        if clean_unit in multiplier or clean_unit+"e" in multiplier:
            break
        print("Please enter a valid unit of measurement.")
    if clean_unit == "inche":
        if usmeters/multiplier["inch"] == 1:
            print("1 inch")
            break
        print(str(usmeters/multiplier["inch"])+" inches")
        break
    elif clean_unit == "feet" or clean_unit == "foot":
        if usmeters/multiplier["feet"] == 1:
            print("1 foot")
            break
        print(str(usmeters/multiplier["feet"])+" feet")
        break
    else:
        if usmeters/multiplier[clean_unit] == 1:
            print("1 "+clean_unit)
            break
        print(str(usmeters/multiplier[clean_unit])+" "+clean_unit+"s")
        break
