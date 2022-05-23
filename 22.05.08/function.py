def calc(x, y, z):
	if z < 0 and y > 0:
		return 3*x - y + 2*z
	else:
		return 3*x + 5*y - z

x = 4
y = 3
z = 1
print(calc(x, y, z))

x = 5
y = 6
z = 0
print(calc(x, y, z))

x = 10
y = 20
z = -5
print(calc(x, y, z))

x =  100
y = 200
z = -10
print(calc(x, y, z))
