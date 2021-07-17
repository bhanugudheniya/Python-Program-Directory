class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=calculator(a,b)
choice=1
while choice!=0:
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Press 0 to exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",c.add())
    elif choice==2:
        print("Result: ",c.sub())
    elif choice==3:
        print("Result: ",c.mul())
    elif choice==4:
        print("Result: ",c.div())
    elif choice==0:
        print("Exiting!!!")
    else:
        print("Invalid choice!!")
