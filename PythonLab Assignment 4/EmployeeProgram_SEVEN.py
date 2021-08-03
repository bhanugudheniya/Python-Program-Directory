import pandas as pd
employees = pd.read_csv(r"E:\Bhanu's Folder 4\Programming Folder\Python\PythonLab Assignment 4\csv_SEVEN\EMPLOYEES.csv")
departments = pd.read_csv(r"E:\Bhanu's Folder 4\Programming Folder\Python\PythonLab Assignment 4\csv_SEVEN\DEPARTMENTS.csv")
job_history = pd.read_csv(r"E:\Bhanu's Folder 4\Programming Folder\Python\PythonLab Assignment 4\csv_SEVEN\JOB_HISTORY.csv")
jobs = pd.read_csv(r"E:\Bhanu's Folder 4\Programming Folder\Python\PythonLab Assignment 4\csv_SEVEN\JOBS.csv")
countries = pd.read_csv(r"E:\Bhanu's Folder 4\Programming Folder\Python\PythonLab Assignment 4\csv_SEVEN\COUNTRIES.csv")
regions = pd.read_csv(r"E:\Bhanu's Folder 4\Programming Folder\Python\PythonLab Assignment 4\csv_SEVEN\REGIONS.csv")
locations = pd.read_csv(r"E:\Bhanu's Folder 4\Programming Folder\Python\PythonLab Assignment 4\csv_SEVEN\LOCATIONS.csv")
print("First name       Last name      Salary    Department ID")
result = employees[employees['first_name'].str[-1]=='m']
for index, row in result.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])
