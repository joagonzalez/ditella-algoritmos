import sys
import json
import morecode
import vars

data = json.load(open(sys.argv[1], 'r'))

print("viene de vars.json")
for element in data:
    print('data: ' + str(element))

print("viene de morecode.py")
morecode.function1()
morecode.function2()

print("viene de vars.py")
print(vars.FORD)