class getString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())
print("Enter String")
str1 = getString()
str1.get_String()
str1.print_String()
