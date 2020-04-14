import sys

def convertion_miles(miles):
    km = miles * 1.6
    return km

def convertion_km(km):
    miles = km / 1.6
    return miles

if sys.argv[1] == "miles":
    print("miles | kilometers")
    for i in range(100):
        print(str(i) + " miles are " + str(convertion_miles(i)) + " kilometers")
elif sys.argv[1] == "kilometers":
    print("miles | kilometers")
    for i in range(100):
        print(str(i) + " kilometers are " + str(convertion_km(i)) + " miles")
else:
    print("enter a valid option!")