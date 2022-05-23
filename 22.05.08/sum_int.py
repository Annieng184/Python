#Tính tổng hai số nguyên bất kì có xử lí dữ liệu đầu vào (dùng hàm try và except)

try:
	num1 = int(input())
	num2 = int(input())

	print('Tổng hai số là: ', num1+num2)
except:
	print('Định dạng đầu vài không hợp lệ')
