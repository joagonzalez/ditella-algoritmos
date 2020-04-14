def despedir(x):
	x.append('chau')
	print(len(x))

a = ['hola', 'mundo']
despedir(a)
print(a)
despedir(list(a))
print(a)