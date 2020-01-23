import string

multiplier={"kilometers":1000, "meters":1, "feet":0.3048, "miles":1609.34, "yards":0.9144, "inches":0.0254}
def convert(unitin, unitout, distance):
    try:
        midpoint = float(distance) * multiplier[unitin] # convert to meters
        outlong = str(midpoint / multiplier[unitout])
        splitdeclist = outlong.split(".")
        splitdec = splitdeclist.pop(1)
        rounded = splitdec.split("00", 1)
        splitdeclist.append(rounded[0])
        output = ".".join(splitdeclist)
        return output
    except ValueError:
        return None
