rows = int(input("Enter Row nos. : "))

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print('* ', end='')
        else:
            print('$ ', end='')
    print()

# i == 0 : means first row
# i == rows - 1 : means first element in blank row
# j == 0 :  means first column
# j == rows - 1 : means first element in blank column
