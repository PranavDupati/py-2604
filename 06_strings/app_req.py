# Enhanced Student Grade Tracker

print("=" * 50) 
print("         Enhanced Student Grade Tracker")
print("=" * 50)

# Validate Student ID: accept only numbers (non-zero and non-negative numbers)  

student_id_valid = False 

while not student_id_valid:
    student_id = input("Enter ID: ")
    
    # validate student_id is numeric only 
    # student_id = input("Enter ID: ")
    # print(student_id.isdigit())
    if student_id.isdigit():
        # if student_id > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True 
        else:
            print("Invalid ID - Zero Value Not Allowed")
    else:
        print("Invalid ID - Non Numerics Not Allowed")

print(f"Student ID {student_id}")

# EDIFY-LEARNER-101
institute_pattern = "EDIFY-LEARNER-"
# print(f"System Generated ID: "+institute_pattern+student_id) # TypeError: can only concatenate str (not "int") to str
print(f"System Generated ID: "+institute_pattern+str(student_id))