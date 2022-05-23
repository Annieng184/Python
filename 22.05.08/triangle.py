#Nhập 3 số a,b,c có là cạnh của một tam giác không? (có xử lý)

try:

	a = float(input())
	b = float(input())
	c = float(input())

	if a+b>c and a+c>b and b+c>a:
		print('Là tam giác')
	else:
		print('Không phải là tam giác')

except:
