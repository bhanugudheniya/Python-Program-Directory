c=0
n=int(input("Enter Number Of Students: "))
d={}
for i in range(n):
	admno=int(input("Enter Admission No."))
	roll_no=int(input("Enter Roll no: "))
	name=input("Enter Name: ")
	marks=int(input("Enter Marks: "))
	d[admno]=[name,roll_no,marks]
print(d)
adm=int(input("Enter The Admission No. Of The Student You Want To Search?"))
for key in d:
	if adm==key:
		print(f"Student's Name: {d[key][0]}")
		print(f"Student's Roll No.: {d[key][1]}")
		print(f"Student's Marks:{d[key][2]}")
		c=1
	else:
		pass
if c==0:
	print("Invalid Admission No.")
