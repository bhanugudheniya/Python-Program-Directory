d={1:"a",2:"b",3:"c",4:"d",5:"e"}
print("Dictionary before deleting is")
print(d)
ch=int(input("Enter the key you want to delete:"))
del d[ch]
print("Dictionary after deleting is")
print(d)
