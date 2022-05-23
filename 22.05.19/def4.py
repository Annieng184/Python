#hàm nguyên tố(m) đơn giản sau sẽ trả lại 1 nếu m là nguyên tố, ngược lại sẽ trả về 0 nếu m là hợp số
def nguyento(n):
	s = 0
	for i in range(1, n):
		if n%i == 0:
			s = s+1
		if s ==1:
			return 1
		else:
			return 0

n = int(input('Nhập số tự nhiên m: '))
if nguyento(n) == 1:
	print(n, 'là số nguyên tố')
else:
	print(n, 'không là số nguyên tố')
