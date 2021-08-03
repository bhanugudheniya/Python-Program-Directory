import pandas as pd
df = pd.DataFrame({
    'school_code': ['s01','s02','s03','s01','s02','s04'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Bhanu Gudheniya','Shobit Khatri','Ashish Sharma', 'Naveen', 'Rohit', 'Nitish'],
    'date_Of_Birth': ['16/05/1998','03/08/1999','22/07/1999','06/01/1998','11/05/1998','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
print("Default Index:")
print(df.head(10))
print("\nschool_code as new Index:")
df1 = df.set_index('school_code')
print(df1)
print("\nt_id as new Index:")
df2 = df.set_index('t_id')
print(df2)
