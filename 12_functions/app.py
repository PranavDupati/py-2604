# Student Management System -> Using Functional Style 

# Menu Based System -> In Future once you learn full stack, replace with UI Elements like Buttons 

# System Setup -> System Info - READ ONLY (Tuple)
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1")

# Admin Info - READ ONLY (Tuple)
ADMIN_INFO = ("9900998800","admin@edify.com")

# Displaying System Info On Start Up 
print("=" * 50)
print(f"Welcome To: {SYSTEM_INFO[0]}")
print(f"Software Name: {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Core Functionality (CRUD)
# Add Student -> id, name, scores, skills 
# Representing Students Data inside Dictionary 

# https://jsoneditoronline.org/images/news/smart_json_formatting.png

# Students Data inside Dictionary 
students = {}

# Adding Student Function
def add_student():
        print("=" * 30)
        print("Adding Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("OOPS!! Student Already Exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
            
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input)
            
            print("========== Student Added ==========")
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print(students)
            
# Updating Student Function
def update_student():
        print("=" * 30)
        print("Updating Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            new_name = input("Enter New Name: ")
            students[student_id]['name'] = new_name
            print("=" * 30)
            print("Student Updated")
            print("=" * 30)
        else:
            print("Student ID Doesn't Exist")
        
        print(students) # for confirmation
 
# Deleting Student Function    
def delete_student():
        print("=" * 30)
        print("Deleting Student")
        print("=" * 30)
        student_id = input("Enter ID: ")
        if student_id in students:
            students.pop(student_id)
            print("=" * 30)
            print("Student Deleted")
            print("=" * 30)
        else:
            print("Student ID Doesn't Exist")
        
        print(students) # for confirmation

# Reading Student Function    
def read_student():
        print("=" * 30)
        print("Reading Student")
        print("=" * 30)
        # {'101': {'name': 'Ravi', 'scores': [90, 80, 70, 60], 'skills': {'git', 'python', 'java'}}}
        # items(): used to get both keys & values 
        for sid, data in students.items():
            name = data['name']
            scores = data['scores']
            skills = data['skills']
            
            # Average Score 
            avg_score = sum(scores) / len(scores)

            # Highest Score 
            high_score = max(scores)
            
            # Lowest Score 
            low_score = min(scores)
                    
            # Skills Count  
            skills_count = len(skills)
                
        print(f"ID: {sid}")
        print(f"Name: {name}")
        print(f"All Scores: {scores}")
        print(f"Average Score: {avg_score}")
        print(f"Highest Score: {high_score}")
        print(f"Lowest Score: {low_score}")
        print(f"All Skills: {skills}")
        print(f"Skills Count: {skills_count}")    

# Search Student By Skill Function    
def search_student_skill():    
        print("=" * 30)
        print("Searching Student")
        print("=" * 30)
        skill_to_search = input("Enter Skill To Search: ")
        filtered_students = list(filter((lambda sid: skill_to_search in students[sid]['skills']),students))
        # print(filtered_students)
        if filtered_students:
            print("=" * 30)
            print(f"Students With Skills {skill_to_search}")
            print("=" * 30)
            for sid in filtered_students:
                print(f"ID: {sid} - Name: {students[sid]['name']}")
        else:
            print("=" * 30)
            print(f"No Students Found With Skill {skill_to_search}")
            print("=" * 30)
            
# Exit Application Function    
def exit_system():
        print("=" * 30)
        print("Exit Application")
        print("=" * 30)
        print(f"Admin Phone Number: {ADMIN_INFO[0]}")
        print(f"Admin Email Address: {ADMIN_INFO[1]}")
    
# Build Menu System For Operations 
while True:
    print("Choose An Option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Search Student By Skill")
    print("6 - Exit Student")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        add_student()
            
    elif choice == "2":
       update_student() 
    
    elif choice == "3":
        delete_student()
        
    elif choice == "4":
        read_student()
        
    elif choice == "5":
        search_student_skill()
         
    elif choice == "6":
        exit_system()
        break
    
    else:
        print("=" * 30)
        print("Invalid Option, Only use (1-6)")
        print("=" * 30)
        
    