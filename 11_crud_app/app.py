# Student Management System

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

# Build Menu System For Operations 
while True:
    print("Choose An Option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
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
            
    
    elif choice == "2":
        print("=" * 30)
        print("Updating Student")
        print("=" * 30)
        student_id = input("Enter ID To Update: ")
        if student_id in students:
            new_name = input("Enter New Name: ")
            students[student_id]['name'] = new_name
            print("=" * 30)
            print("Updated Student")
            print("=" * 30)
        else:
            print("Student ID Doesn't Exist")
        
        print(students) # Confirmation         
    
    elif choice == "3":
        print("=" * 30)
        print("Deleting Student")
        student_id = input("Enter ID To Delete: ")
        if student_id in students:
            students.pop(student_id)
            print("=" * 30)
            print("Deleted Student")
            print("=" * 30)
        else:
            print("Student ID Doesn't Exist")
        
        print(students) # Confirmation  
            
        
    elif choice == "4":
        print("=" * 30)
        print("Reading Student")
        print("=" * 30)
        # {'101': {'name': 'Ravi', 'scores': [80, 90, 80], 'skills': {'git', 'python'}}}
        # items(): used to get both keys & values 
        for sid, data in students.items():
            name = data['name']
            scores = data['scores']
            skills = data['skills']
            
            # Average Score 
            total_score = 0
            count_scores = 0 
            
            for score in scores:
                total_score += score
                count_scores += 1
            
            avg_score = total_score / count_scores
            
            # Highest Score 
            high_score = scores[0]
            
            for score in scores:
                if score > high_score:
                   high_score = score
                   
            # Lowest Score 
            low_score = scores[0] 
            
            for score in scores:
                if score < low_score:
                    low_score = score 
                    
            # Skills Count 
            skills_count = 0
            
            for skill in skills:
                skills_count += 1
                
        print(f"Student ID: {sid}")
        print(f"Student Name: {name}")
        print(f"All Scores: {scores}")
        print(f"Average Score: {avg_score}")
        print(f"Highest Score: {high_score}")
        print(f"Lowest Score: {low_score}")
        print(f"All Skills: {skills}")
        print(f"All Skills Count: {skills_count}")
            
    elif choice == "5":
        print("=" * 30)
        print("Exit Application")
        print("=" * 30)
        # Displaying Admin Info At End
        print("=" * 50)
        print(f"Admin Phone Number: {ADMIN_INFO[0]}")
        print(f"Admin Email Address: {ADMIN_INFO[1]}")
        print("=" * 50)
        break
    
    else:
        print("=" * 30)
        print("Invalid Option, Only use (1-5)")
        print("=" * 30)
        
    