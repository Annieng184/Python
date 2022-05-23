#Nhập và tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng (có xử lý)???


try:
	num = int(input())
	list_num = num.split()
	list_sum = sum(list.num)
	print(list_sum)

except:
	print('Định dạng đầu vào không hợp lệ!')


