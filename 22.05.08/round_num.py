#Làm tròn số thập phân A đến B chữ số sau dấu phẩy (có xử lý)- dùng hàm format
#format(value[, format_spec])????

try:

	num1 = float(input('Nhập số đầu tiên: '))
	num2 = int(input('Nhập số thứ hai: '))

	print(format(round(num1, num2)))

except:
	print('Định dạng đầu vào không hợp lệ')


