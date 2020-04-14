import sys

farenheit = int(sys.argv[1])
celcius = (farenheit - 32) * (5/9.0)

print(str(farenheit) + " grados Farenheit equivalen a " + str(celcius) + " grados Celcius.")

# hacer unit test