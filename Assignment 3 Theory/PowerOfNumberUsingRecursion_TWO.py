def power(Number, Power):
    if Power == 0:
        return 1
    elif Power == 1:
        return Number
    else:
        return (Number * power(Number, Power - 1))

Number = int(input("Enter Number\n"))
Power = int(input("Enter Power\n"))

print(power(Number, Power))