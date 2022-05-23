#Hiển thị các số chia hết cho 5 trong khoảng a, b (a <= b).

a = int(input('Nhập số đầu tiên: '))
b = int(input('Nhập số thứ hai: '))
q = []
for i in range(a,b+1):
	if i%5 == 0:
		q.append(i)

print(q)
