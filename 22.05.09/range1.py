#Viết p trình tìm tất cả các số chia hết cho 7 nhưng ko phải bội số của 5, nằm trong đoạn 2000 và 3200,. Các số thu dc in thành chuỗi trên 1 dòng, cách nhau dấu phẩy

file = []
for q in range(2000,3200):
	if (q%7 == 0) and (q%5 != 0):
		file.append(str(q))

print(','.join(file))

