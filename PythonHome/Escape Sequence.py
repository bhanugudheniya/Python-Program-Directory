txt1 = 'It\'s alright.'
print(txt1)

txt2 = "This will insert one \\ (backslash)."
print(txt2)

txt3 = "\nHello\nWorld!\n"
print(txt3)

txt4 = "Hello\rWorld!"
print(txt4)

txt5 = "Hello\tWorld!"
print(txt5)

#This example erases one character (backspace):
txt6 = "Hello \bWorld!"
print(txt6)

#A backslash followed by three integers will result in a octal value:
txt7 = "\110\145\154\154\157"
print(txt7)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt8 = "\x48\x65\x6c\x6c\x6f"
print(txt8)
