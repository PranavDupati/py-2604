# Indentation 

print("Hello")
print("Python")
#  print("Ravi") # IndentationError: unexpected indent
print("Ravi")

# if condition - Incorrect Indentation
# if True: # IndentationError: expected an indented block after 'if' statement on line 9
# print("Statement 1")
# print("Statement 2")
# print("Statement 3")
# print("Statement N")

# if condition - Correct Indentation
if True: 
 print("Statement 1")
 print("Statement 2")
 print("Statement 3")
 print("Statement N")
 
if True: 
  print("Statement 1")
  print("Statement 2") # IndentationError: unexpected indent
  print("Statement 3")
  print("Statement N")
  
if True: 
    print("Statement 1")
    print("Statement 2") # IndentationError: unexpected indent
    print("Statement 3")
    print("Statement N")
    
# if condition
if 5 > 2: # True
    print("yes 5 > 2 is correct")
    
if 5 < 2: # False 
    print("yes 5 < 2 is correct")
    
num = 10 
if num > 0:
    print("given num is positive")
if num < 0:
    print("given num is negative")
    

num = -10 
if num > 0:
    print("given num is positive")
if num < 0:
    print("given num is negative")
    
    
# if else condition 
num = 10 
if num > 0:
    print("given num is positive")
else:
    print("given num is negative")
    
# if else condition using input() -> dynamic 
name = input("Enter Name: ")
print(name)
print("Hello " +name)
print("Hello " ,name)
print("Hello {name}")
print(f"Hello {name}")

username = input("Enter Username: ")
course = input("Enter Course Name: ")
print(f"Hello {username}, Welcome To {course}")

# if else condition using input() -> dynamic 
num = input("Enter Number: ") 
num = int(num)
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"given {num} is positive")
else:
    print(f"given {num} is negative")
    
# if else condition using input() -> dynamic 
num = int(input("Enter Number: "))
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"given number {num} is positive")
else:
    print(f"given number {num} is negative")
    
# Voting App
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You Can Vote")
else:
 print(f"You Cannot Vote You are Still {age}")
    # print("Not Executed")
 print("Now Executed")
 
print('==================')

# Conditional Expression
# value_if_true if condition else value_if_false     
age = int(input("Enter Your Age: "))
status = "You Can Vote" if age >= 18 else "You Cannot Vote"     
print(status)

print('==================')

# elif ladder 
# Check For Grades
marks = int(input("Enter Marks: "))
if marks >=90:
    print("A Grade")
elif marks >=75:
    print("B Grade")
elif marks >=60:
    print("C Grade")
elif marks >=50:
    print("D Grade")
elif marks >=35:
    print("E Grade")
else:
    print("FAIL")
    
# match/case statement
error_code = int(input("Enter Error Code - What You are Seeing: "))
match error_code:
    case 403:
        print("It's Forbidden Error")
    case 404:
        print("It's Not Found Error")
    case 200:
        print("It's No Error - It's Success")
    case 502:
        print("It's Internal Server Error")
    case _:
        print("It's Invalid Error Code")
