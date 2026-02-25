# Operators 

# Arithmetic Operators
num1 = 10
num2 = 5 

print("Sum Of Numbers: ", num1 + num2)
print("Difference Of Numbers: ", num1 - num2)
print("Product Of Numbers: ", num1 * num2)
print("Division Of Numbers: ", num1 / num2)
print("Modulus Of Numbers: ", num1 % num2)

print("Floor Division Of Numbers: ", num1 // num2)

print("Normal Division Of Numbers: ", 3/2)
print("Floor Division Of Numbers: ", 3//2)

print("Exponentiation Of Numbers: ", 3 ** 2) # 3 ^ 2

# Compound Assignment Operators  
num = 10 
num = num + 5 
print(num)

num = 10
num += 5 
print(num)

num = 10
num *= 5 
print(num)

# Increment: increase a value, used in loops in future sessions 
count = 1
print(count)
# count++ # SyntaxError: invalid syntax
count += 1
print(count)
count += 1
print(count)
count += 1
print(count)

# Decrement: decrease a value, used in loops in future sessions 
count = 10
print(count)
count -= 1
print(count)
count -= 1
print(count)
count -= 1
print(count)

# Comparison Operators
num1 = 3
num2 = 2

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)

print("================")

# Logical Operators
num1 = 4
num2 = 3
num3 = 2
num4 = 1

print(num1 > num2 and num3 > num4) # True and True -> True
print(num1 > num2 and num3 < num4) # True and False -> False

print(num1 > num2 or num3 < num4) # True or False -> True
print(num1 < num2 or num3 < num4) # False or False -> False

print(num1 > num2) # True
print(not num1 > num2) # False

print("================")

# Membership Operators
data = "python is programming language"
find_word = "java"
status = find_word in data 
print(status)

data = "python is programming language"
find_word = "python"
status = find_word in data 
print(status)

data = "python is programming language"
find_word = "java"
status = find_word not in data 
print(status)

list_employees_ids = ["101","102","106","108"]
find_emp_id = "104"
status = find_emp_id in list_employees_ids
print(status)

# Scenario with numerics
data = 123456789
find_four = 4 
# status = find_four in data # TypeError: argument of type 'int' is not iterable
print(status)

print(type(data))
print(dir(data))

data = "python is programming language"
print(type(data))
print(dir(data))

data = ["101","102","106","108"]
print(type(data))
print(dir(data))