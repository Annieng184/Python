#Viết biểu thức để kiểm tra xem số year phải là năm nhuận ko?

a = eval(input('Nhập số năm:'))
if a%400 == 0 or (a%4 == 0 and a%100 != 0):
	print('Là năm nhuận')
else:
	print('Không là năm nhuận')
