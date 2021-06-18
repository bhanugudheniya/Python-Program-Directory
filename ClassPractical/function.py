def chk(n):
    print("MCA")
    return n

print(12 and chk(23))
print("******************")
print(chk(12) and 10)
print("******************")
print(11 or chk(34))
print("******************")
print(0 and chk(12))
print("******************")
print(chk(12) and 0)
print("******************")
print(0 or chk(12))
print("******************")
print(chk(12) or 0)



"""
and CASE :---> x and y (if x is false then x, else y)

or CASE :--->  x or y (if x is true then x, else y)
"""