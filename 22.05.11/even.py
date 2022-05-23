#Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn. In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.

# values = ''
# for n in range(1000,2000+1):
# 	if n %2 == 0:
# 		values = str(values) + str(n) + ',' + ''
# print(values[:-1])

values = []
for n in range(1000, 2000+1):
	if n%2 ==0:
		values.append(n)

print(values)

# s1 = '1 2'
# s1 = s1 + ' ' + str(3)
# s1 = s1 + ' ' + str(4)
# for n in range (1, 1000):
# 	s1 = s1 + ',' + str(n)
# print(s1)


