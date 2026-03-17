# Strings In Python 

# Single Line Strings

s1 = 'hello'
print(s1)

s2 = "hello"
print(s2)

s3 = """hello""" # not recommended for Single Line Strings
print(s3)

s4 = '''hello''' # not recommended for Single Line Strings
print(s3)

# Multi Line Strings

# define_python = "Python is a high-level, general-purpose programming language. 
#         Its design philosophy emphasizes code readability with the 
#         use of significant indentation. 
#         Python is dynamically type-checked and garbage-collected."

# print(define_python)

define_python = '''Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the 
        use of significant indentation. 
        Python is dynamically type-checked and garbage-collected.'''

print(define_python)

define_python = """Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the 
        use of significant indentation. 
        Python is dynamically type-checked and garbage-collected."""

print(define_python)

# Need Single Quote In a String 
question = "How are you ?"
# answer = 'i'm fine' # SyntaxError: unterminated string literal (detected at line 42)
answer = "i'm fine"
print(answer)

# Need Double Quote In a String
question = "How are you ?"
# answer = "i"m fine" # SyntaxError: unterminated string literal (detected at line 48)
answer = 'i"m fine'
print(answer)

# Need Single Quote & Double Quote In a String
question = "How are you ?"
# answer = "i'm fine i"m fine" # SyntaxError: unterminated string literal (detected at line 54)
answer = """i'm fine i"m fine"""
answer = '''i'm fine i"m fine'''
print(answer)

# Accessing Strings 
text = "python"
print(text)

# Accessing Characters 
print(text[0])
print(text[1])
# Above is positive indexing 

# Negative Indexing
print(text[-1])
print(text[-2])

# Beyond Index Range
# print(text[10]) # IndexError: string index out of range
# print(text[-10]) # IndexError: string index out of range

# Access all Characters 
text = "python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])

# Access all Characters 
text = "python"
for character in text:
    print(character)
    
# Slicing 
text = "python"
            #  0.  1.  2.   3.  4.  5.   (positive indexing) 
            #  p   y   t    h   o   n 
            # -6  -5  -4  -3  -2  -1 
            
print(text[::])           
print(text[0:3:1])  # pyt
print(text[0:3])    # pyt
print(text[1:3])    # yt
print(text[0:5:2])  # pto
print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # thn -> empty 
print(text[-4:-6:-1]) # ty 

# String Concatenation 
g = "good"
m = "morning"
print(g+m)

# Formatted String Literals (f-strings)
age = 30 
# print("My age is "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My age is {age}")

# String Repetition
laugh = "Haha"
print(laugh)

hard_laugh = laugh * 10
print(hard_laugh)

# String Immutability 
greet = "hello"
print(greet)
# Requirement is Hello
# greet[0] = 'H' # TypeError: 'str' object does not support item assignment
print(greet)

# List Objects are Mutable In Nature -> Can be Changed / Modified)
greet = ['h','e','l','l','o']
print(greet)
greet[0] = 'H'
print(greet)

