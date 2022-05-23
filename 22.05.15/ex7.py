#Nhập số tự nhiên, in ra các ước số và đếm các ước số đó

n = int(input('Enter a number: '))
count = 0
for i in range(1,n+1):
	if n%i ==0:
		count = count+1

for i in range(1,n+1):
	if n%i ==0:
		print(i, end=' ')

print('Tổng ước số là:',count)





