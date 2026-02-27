# Data Types 

# Numeric Types 

data = 10 
print(type(data))

data = -10 
print(type(data))

data = 10.5 
print(type(data))

data = -10.5 
print(type(data))

# data = 3 + i5
# print(type(data))

data = 3 + 5j
print(type(data))

# Boolean Type
data = True
print(type(data))

data = False 
print(type(data))

# None Type
data = None 
print(type(data))

# String Type
data = "python"
print(type(data))

# List 
data = [10,20,30,40,50]
print(type(data))

# Tuple
data = (10,20,30,40,50)
print(type(data))

# Set
data = {10,20,30,40,50}
print(type(data))


# Frozenset
data = frozenset({10,20,30,40,50})
print(type(data))

# Dictionary
data = {"course":"python","time":12,"duration":60}
print(type(data))
 
# Custom Datatype
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_gpa = 9.5 
    student_enrolled_courses = ["python","cloud","devops"]

data = Student()
print(type(data))
print(data.student_id)
print(data.student_name)

# Type Conversion / Implicit Conversion [Automatic]
n1 = 10 # int 
n2 = 5.5 # float 
sum = n1 + n2 
print(sum) 
print(type(sum))

# Type Casting / Explicit Conversion [ Manual ]
price = 1120.85
print(price)
print(type(price))

round_off_price = price
print(round_off_price)
print(type(round_off_price))

# data_type(value)
round_off_price = int(price)
print(round_off_price)
print(type(round_off_price))

# Some user in a web page was filling some form(text boxes), 
# which has some rating (Strings)

rating = "5"
print(type(rating))
rating = int(rating)
if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
    print("Positive Feedback")
else:
    print("Negative Feedback")