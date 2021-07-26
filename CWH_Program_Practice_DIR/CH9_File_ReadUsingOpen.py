file = open("File1", 'r')   # by default the mode is r || file is a object which contain File1
# print(file)     # <_io.TextIOWrapper name='File1' mode='r' encoding='cp1252'>
data = file.read()  # data is a variable which contain file in readable format
print(data)     # print data
file.close()    # close file after use

# ****
# data = file.read(5) --> read first five character from the file