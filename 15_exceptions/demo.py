# Exception Handling

# When No Errors -> Nothing To Handle
print("Program Execution Started")
num1 = 10
num2 = 5
print("Result: ",num1/num2)
print("Program Execution Completed")

print("=" * 50)

# When Errors -> Program abruptly "STOPS"
# print("Program Execution Started")
# num1 = 10
# num2 = "five"
# print("Result: ",num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
# print("Program Execution Completed")

# When Errors -> Handle Exceptions Using try & except
print("Program Execution Started")
num1 = 10
num2 = "five"
try:
    print("Result: ",num1/num2)
except:
    print("Don't Divide Numerics and Strings!!!!")    
print("Program Execution Completed")

print("=" * 50)

# When No Errors -> Nothing To Handle
print("Program Execution Started")
num1 = 10
num2 = 5
print("Result: ",num1/num2)
print("Program Execution Completed")
print("=" * 50)

# When No Errors -> Nothing To Handle
# print("Program Execution Started")
# num1 = 10
# num2 = 0
# print("Result: ",num1/num2) # ZeroDivisionError: division by zero
# print("Program Execution Completed")

print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!! We Got Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")
print("=" * 50)

# When We Come Across Multiple Errors
print("Program Execution Started")
# data = [1,2,'python',0,5]
# data = [1,2,0,5]
data = [1,2,5]
for num in data:
    print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
print("Program Execution Completed")
print("=" * 50)

# When We Come Across Multiple Errors
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except:
        (print("OOPS!!!! Something Went Wrong"))
print("Program Execution Completed")
print("=" * 50)

# When We Come Across Multiple Errors
# Specific Exception Message 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except TypeError:
        print("OOPS!!!! Don't Divide Numerics and Strings!!!!")
    except ZeroDivisionError:
        print("OOPS!! We Got Error - Check Below Link")
        print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")
print("=" * 50)

# else in exceptions 
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!! We Got Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful")
print("Program Execution Completed")
print("=" * 50)


# finally -> run code for sure 
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!! We Got Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful")
finally:
    print("Closing All Opened Connections Like File & Database Connections")
    print("Program Execution Completed")
print("=" * 50)

# Custom Exceptions
class MyCustomError(Exception):
    pass 

# Voting App with Custom Exceptions
age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")

# Custom Age Exception    
class AgeError(Exception):
    pass 

# age = int(input("Enter Age: "))
# if age < 18:
#     raise AgeError
# else:
#     print("You Can Vote")

# age = int(input("Enter Age: "))
# if age < 18:
#     raise AgeError("under age error")
# else:
#     print("You Can Vote")
    
age = int(input("Enter Age: "))
try:
    if age < 18:
        raise AgeError("under age error")
except:
    print("You are not 18 yet")
else:
    print("You Can Vote")
    
class IDError(Exception):
    pass

age = int(input("Enter Age: "))
try:
    if age < 18:
        raise AgeError("under age error")
    else:
        has_id = input("Do you have ID ? (yes/no)")
        if has_id != "yes":
            raise IDError("no valid id error ")
except AgeError:
    print("You are not 18 yet")
except IDError:
    print("You are not having valid ID")    
else:
    print("You Can Vote")