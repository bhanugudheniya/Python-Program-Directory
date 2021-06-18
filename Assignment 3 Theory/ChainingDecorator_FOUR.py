def star(functionStar):
    def innerStar(*argumentStar, **countStar):
        print("*" * 30)
        functionStar(*argumentStar, **countStar)
        print("*" * 30)
    return innerStar

def hash(functionHash):
    def innerHash(*argumentHash, **countHash):
        print("#" * 30)
        functionHash(*argumentHash, **countHash)
        print("#" * 30)
    return innerHash

@star
@hash
def Message():
    stringValue = input()
    return stringValue

Message()

# msg = input("Enter a String")