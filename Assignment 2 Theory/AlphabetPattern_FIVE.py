# A
# B C
# DEF
# GHIJ
# ΚΙΜΝΟ

def alphaPattern(n):
    num = 65

    if n <= 7:
        for i in range(0, n):

            for j in range(0, i + 1):
                ch = chr(num)

                print(ch, end=" ")

                num = num + 1

            print("\r")
    else:
        print("Please Input Number in Range of 1 to 7 ")
alpha = int(input("Enter Row : "))
alphaPattern(alpha)
