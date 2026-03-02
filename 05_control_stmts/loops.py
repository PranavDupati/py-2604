# Looping Structures / Statements (Iteration Statements)

# While Loop
# while True:
#     print("This Line Always Executes - Forms Infinite Loop")
    # To Terminate the loops use control + c on keyboard
    
while False:
    print("This Line Always Executes - Forms Infinite Loop")
    
# While Loop
# Counters
count = 1
while count <= 5 :
    print("Count: ", count)
    count += 1
    
# You found a lost phone, trying to break passcode 
# At which attempt the phone will be unlocked ?
actual_passcode = "1234"
user_given_passcode = ""

while user_given_passcode != actual_passcode:
    user_given_passcode = input("Enter Passcode: ")
    
print("Phone Unlocked")
