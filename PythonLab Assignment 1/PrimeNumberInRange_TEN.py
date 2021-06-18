numberInput = int(input("Enter any number : "))
temp = numberInput
print("All Prime Number in range till",numberInput  ,"are : ")
for i in range(2, numberInput+1):
    b = 0
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
