a=int(input("entera number:"))
sum=0
for i in range(1,a):
	if a%i==0:
		sum=sum+i
if sum==a:
	print("the number is a perfect number")
else:
	print("the number is not aperfect number")
