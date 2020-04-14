def f(x,y):
    x = 2 * x + y
    return x

x = 3
y = 7

y = f(y,x)
x = f(y,x)

print(x,y) # 37 17