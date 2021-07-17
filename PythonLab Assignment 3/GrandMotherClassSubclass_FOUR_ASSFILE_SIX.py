class grandmother:
    def __init__(self):
        self.str1=" "
    def main(self):
        self.str1="I am the grandmother"
        print(self.str1)
class mother(grandmother):
    def __init__(self):
        self.str2=" "
    def mot(self):
        self.str2="I am the mother"
        print(self.str2)
class daughter(mother):
    def __init__(self):
        self.str3=" "
    def d(self):
        self.str3="i am daughter"
        print(self.str3)
obj = daughter()
obj.main()
obj.mot()
obj.d()
