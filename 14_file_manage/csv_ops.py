# Working with CSV Files 

import csv

# Read Data From CSV File 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)

print("=" * 50)
        
# Assume we have 100k Student Records In CSV File (as of now only 100 records)
# Customer Requirement: Fetch me all the students from Hyderabad
# Observation to be made: What format the data is in ?? List 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row) # all entires
        # print(row[-1]) # only Address entires
        if row[-1] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Assume we have 100k Student Records In CSV File (as of now only 100 records)
# Customer Requirement: Fetch me all the students from tcs 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[1])
        if row[1].endswith("@tcs.com"):
            print(row)
            
print("=" * 50)

# Assume we have 100k Student Records In CSV File (as of now only 100 records)
# Customer Requirement: Fetch me all the students from Hyderabad
# Observation to be made: What format the data is in ?? List 

# with open("14_file_manage/sample.csv","r") as file_data:
#     csv_reader = csv.reader(file_data)
#     for row in csv_reader:
#         # print(row) # all entires
#         # print(row[-1]) # only Address entires
#         if row[-1] == "Hyderabad":
#             print(row)
            
# print("=" * 50)

# Using DictReader
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        print(row) 
        
print("=" * 50)

# Assume we have 100k Student Records In CSV File (as of now only 100 records)
# Customer Requirement: Fetch me all the students from Hyderabad
# Observation to be made: What format the data is in ?? List 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row['address']) # only Address entires
        if row['address'] == "Hyderabad":
            print(row)
            
print("=" * 50)

with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row['address']) # only Address entires
        if row['address'] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Writing Data with Writer
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerows([
        ['Mahesh', 'mahesh583@yahoo.com', '9262564200', 'Ahmedabad'],
        ['Manoj', 'manoj459@yahoo.com', '9999057949', 'Delhi'],
        ['Balu', 'balu754@hotmail.com', '9812454047', 'Coimbatore']
    ])
    
# Writing Data with DictWriter
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/demo.csv","w") as file_data:
    csv_writer = csv.DictWriter(file_data,fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'Mahesh', 'mobile': '9969450859', 'address': 'Hyderabad', 'email': 'mahesh381@outlook.com'})
    csv_writer.writerows([
        {'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'},
{'name': 'Santosh', 'email': 'santosh579@outlook.com', 'mobile': '9718726887', 'address': 'Hyderabad'},
{'name': 'Naveen', 'email': 'naveen409@tcs.com', 'mobile': '9806720153', 'address': 'Hyderabad'}
    ])
    
    