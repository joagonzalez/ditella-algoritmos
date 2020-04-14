# ej1
# a)
print(1+1)
print(str(type(1+1)))

# b)
print('ho' + "la")
print(str(type('ho' + "la")))

# c)
print((1>0) or (not ('a'<'b')))
print(str(type((1>0) or (not ('a'<'b')))))

# d)
print(len('hola') + 6)
print(str(type(len('hola') + 6)))

# e)
print((5.6 >2.0) and (len('hola')<2))
print(str(type((5.6 >2.0) and (len('hola')<2))))

# f)
print(1+1.0)
print(str(type(1+1.0)))

# g)
print(11/2)
print(str(type(11/2)))

# h)
print(11//2)
print(str(type(11//2)))

# i)
try:
    print(1/0)
    print(str(type(1/0)))
except:
    print('no pude dividir por cero')

# j)
try:
    print(123 + '123')
    print(str(type(123 + '123')))
except:
    print('no pude concatenar string e int')
# k)
print(1 + int('123'))
print(str(type(1 + int('123'))))

# l)
print(str(123) + '123')
print(str(type(str(123) + '123')))