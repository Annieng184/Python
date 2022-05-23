#Nhập 3 số, kiểm tra xem có thể tạo thành 1 tam giác dc ko? Nếu có, thể hiện '3 số a,b,c tạo thành tam giác', nếu ko, '3 số a,b,c ko tạo thành tam giác'

a,b,c = eval(input('3 cạnh tam giác là:'))

if a+b>c and a+c>b and b+c>a:
	print('3 số a,b,c tạo thành tam giác')
else:
	print('3 số a,b,c  tạo thành tam giác')
