f = open('File1', 'r')
data = f.readline()
print(data)

data = f.readline()
print(data)

f.close()

# readline use for read single line at a time, if we write it again so it will print next line.