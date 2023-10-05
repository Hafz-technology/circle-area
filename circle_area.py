w = input("calculate circal area by radius or diameter (for radius enter r for diameter enter d): ")
pi = 3.14
if w == "r" :
    r = int(input("enter the radius: "))
    area = pi * r *r
    print(area)
else:
    d = int(input("enter the diameter: "))
    area = (pi * d *d )/4
    print(area)

