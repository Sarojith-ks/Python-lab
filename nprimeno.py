num = int(input("Enter a number: "))
count = 0
n = 2

print("First", num, "prime numbers are:")

while count < num:
#define a flag variable.
    primeflag = True
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            primeflag = False
            break
            
    if primeflag:
        print(n, end=" ")
        count += 1
        n += 1
