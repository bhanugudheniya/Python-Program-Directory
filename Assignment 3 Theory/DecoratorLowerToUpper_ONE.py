def DecoratorOver(function):
    def DecoratorUnder():
        f = function()
        print(f.upper())
    return DecoratorUnder


@DecoratorOver # chk = DecoratorOver(chk)       #----------->----|
def chk():                                      #                |
    strValue = input("Enter a String\n")        #               \|/
    return strValue                             #               `|`
# chk = DecoratorOver(chk) <--------------<-------------<--------|
chk()