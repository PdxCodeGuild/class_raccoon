overflow = 1
while overflow >= 0:
    output=overflow
    overflow *= 2
    if overflow%1024 == 0:
        print(overflow)
print(output)
