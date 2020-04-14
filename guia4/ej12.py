txt = 'este es un texto muy corto de prueba'

a = [x*10 for x in range(0, 10) if (x == 1 or x == 5 or x == 9)]
b = [('par' if x % 2==0 else 'non') for x in range(0, 10)]
c = ''.join([(x if x not in 'aeiou' else '_') for x in txt])
d = [y+x for x in '123' for y in 'ab']

print(a)
print(b)
print(c)
print(d)