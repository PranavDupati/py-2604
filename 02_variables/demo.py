# Variables 

# Store Data (Assign)
student_name = "Ravi" # String
student_age = 25 # int
student_gpa = 9.5 # float 
student_passed = True # bool
student_failed = False # bool
# student_aadhar =  # SyntaxError: invalid syntax
student_aadhar = None # Absence Of value i.e NoneType 

# Retrieve Data (Get)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(student_failed)
print(student_aadhar)

# # Retrieve Data (Get) With Concatenation
print("======== Student Info ========")
print("Student Name: " + student_name)
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: " , student_age)
# print("Student GPA: " + student_gpa) # TypeError: can only concatenate str (not "float") to str
print("Student GPA: " , student_gpa)

# print("Student Passed: " + student_passed) # TypeError: can only concatenate str (not "bool") to str

print("Student Passed: " , student_passed)
# print("Student Failed: " + student_failed) # TypeError: can only concatenate str (not "bool") to str
print("Student Failed: " , student_failed)

# print("Student Aadhar: " + student_aadhar) # TypeError: can only concatenate str (not "NoneType") to str

print("Student Aadhar: " , student_aadhar)

print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(student_failed))
print(type(student_aadhar))

# id() -> gives memory address 
id(student_name)
print(id(student_name))
print(id(student_age))
number = 25 
print(id(number))
