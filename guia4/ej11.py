txt = 'este es un texto muy corto de prueba'

[x for x in range(0, 10) if x %3==1]
a = [(x if x %2==0 else -111) for x in range(0, 10)]
[x for x in txt.split(' ') if len(x)>3]
' '.join([x+' '+x for x in txt.split()])
''.join([x for x in txt if x not in 'aeiou'])
a = [x+y for x in 'ab' for y in '123']

print(a)