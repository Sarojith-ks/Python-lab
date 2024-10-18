n=int(input("enter the lowest range value :"))
m=int(input("enter the upper range value :"))
print("the prime number in range are :")
for number in range(n,m+1):
	if number>1:
		for i in range(2,number):
			if(number%i)==0:
				break
		else:
			print(number)
