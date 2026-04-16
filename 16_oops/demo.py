# OOP - Object Oriented Programming

# class -> Blue Print 
# Student -> Real World Entity 

class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies():
        print("Student Info - Student Studies")
        
    # Statements 
    print("Student Information System")
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
        
# Object Creation
student_object = Student()    
# student_studies()
# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

# Methods 
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        
    # Statements 
    print("Student Information System")
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
        
# Object Creation
student_object = Student() 
student_object.student_studies()

print("=" * 50)

# Referring With Objects
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        # print("Student Name: "+student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Name: "+self.student_name) # recommended (OOP)
        print("Student Email: "+student_object.student_email)
        
# Object Creation
student_object = Student() 
student_object.student_studies()


# Referring With self is # recommended (OOP)
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        # print("Student Name: "+student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Name: "+self.student_name) # recommended (OOP)
        print("Student Email: "+self.student_email) # recommended (OOP)
        
# Object Creation
student_object = Student() 
student_object.student_studies()

print("=" * 50)

# Without Constructors
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name) # recommended (OOP)
        print("Student Email: "+self.student_email) # recommended (OOP)
        
# Object Creation
student_ravi = Student() 
student_ravi.student_studies()

student_john = Student() 
student_john.student_studies()

student_mike = Student() 
student_mike.student_studies()

print("=" * 50)

# With Constructors
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor - to initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # this.student_name = student_name -> Valid in Java 
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name) # recommended (OOP)
        print("Student Email: "+self.student_email) # recommended (OOP)
        
# Object Creation
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)

# Instance Members 
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor - to initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # Below are instance variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    # Below is Instance Method
    def student_studies(self):
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name) # recommended (OOP)
        print("Student Email: "+self.student_email) # recommended (OOP)
        
# Object Creation
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("johnny","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)


# Class Variable 
class Student:
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Edify"
    
    # Constructor - to initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # Below are instance variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    # Below is Instance Method
    def student_studies(self):
        print("From Institute: "+Student.institute_name) # recommended (OOP)
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name) # recommended (OOP)
        print("Student Email: "+self.student_email) # recommended (OOP)
        print("From Institute: "+self.institute_name) # not recommended (OOP)
        
        
# Object Creation
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("johnny","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)


# Class Method 
class Student:
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Edify"
    
    # Constructor - to initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # Below are instance variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    # Below is Instance Method
    def student_studies(self):
        print("From Institute: "+Student.institute_name) # recommended (OOP)
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name) # recommended (OOP)
        print("Student Email: "+self.student_email) # recommended (OOP)
        print("From Institute: "+self.institute_name) # not recommended (OOP)
        
    # Class Method - operates on class variables 
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # Accessing instance data inside a class method gives error 
        # print(self.student_email) # NameError: name 'self' is not defined


# Object Creation
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("johnny","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

# Calling Class Method
Student.change_institute_name("Digital Edify")

student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("johnny","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)


# Class Method 
class Student:
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Edify"
    
    # Constructor - to initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # Below are instance variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    # Below is Instance Method
    def student_studies(self):
        print("From Institute: "+Student.institute_name) # recommended (OOP)
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name) # recommended (OOP)
        print("Student Email: "+self.student_email) # recommended (OOP)
        print("From Institute: "+self.institute_name) # not recommended (OOP)
        
    # Class Method - operates on class variables 
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # Accessing instance data inside a class method gives error 
        # print(self.student_email) # NameError: name 'self' is not defined
        
    # Static Method - does not depend/operate on instance variable or class variable 
    @staticmethod
    def something_random():
        return "I Do Something, that is not associated with Class Or Objects"

# Object Creation
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("johnny","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

# Calling Class Method
Student.change_institute_name("Digital Edify")

student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("johnny","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

# Calling Static Method
print(Student.something_random())

print("=" * 50)