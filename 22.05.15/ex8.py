#Tính tổng các số <n và là số lẻ, tích các số <n và là số chẵn


n = int(input())
tong = 0
tich = 0

for i in range(1, n):
	if i%2 == 0:
