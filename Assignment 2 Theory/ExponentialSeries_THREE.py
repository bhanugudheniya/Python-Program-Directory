# Sum of the exponential series 1+x1/1!+x2/2!+……..xn/(n)! .
x = int(input("Enter the value of x : "))
n = int(input("Enter the number of terms : "))
ExponentialSum = 1

for i in range(1, n+1):
    ExponentialSum = ExponentialSum+((x**i)/i)      # ** -> Exponentiation
print("The Sum of Exponential Series is : ", ExponentialSum)