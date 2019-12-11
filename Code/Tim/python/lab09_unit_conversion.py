import os

os.system('cls')

unit_in = input("What is the unit of measurement you want to convert from? \n(ft) feet (mi) miles (me) meters (km)\n> ")
measurement_in = float(input("What is the measurement? \n> "))
unit_out = input("What unit of measurement would you like to convert that to?\n(ft) feet (mi) miles (me) meters (km)\n> ")

if unit_in == "ft":
    measurement_in = measurement_in * 0.3048
elif unit_in == "mi":
    measurement_in = measurement_in * 1609.34
elif unit_in == "km":
    measurement_in = measurement_in * 1000

if unit_out == "ft":
    measurement_in =  measurement_in / 0.3048
if unit_out == "mi":
    measurement_in = measurement_in / 1609.34
if unit_out == "km":
    measurement_in = measurement_in / 1000

print(f"%%%%%%%%%%\n{measurement_in}\n%%%%%%%%%%\n> ")
