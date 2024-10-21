string =input("enter a string :")
count = 0
for i in range(len(string)):
    if string[i] != ' ':  
        count += 1 
print("Total number of characters in the string: " + str(count))

