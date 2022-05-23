#Nhập số giây, sau đó đổi số giây thành giờ và phút

ss = int(input('Enter the number of seconds: '))
h,d = divmod(ss,3600)
m,s = divmod(d,60)
print(ss,'seconds = ',h,'hour',m,'minute',s,'second')
