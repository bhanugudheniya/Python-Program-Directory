class parent:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def print(self):
        print(self.name)
        print(self.age)
class child(parent):
    def __init__(self,age,name):
        super().__init__(age,name)
ch= child(23,"Bhanu Gudheniya")
ch.print()
