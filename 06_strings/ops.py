# String Methods / Operations 

# Simulate Gmail Functionality
# RaVI2KRIshNA -> ravi2krishna@gmail.com 

email = input("Enter Email ID: ")
print("Original Email: "+email)
print(type(email))
# Transform Email to Lower Case 
format_email = email.capitalize()
print("Transformed Email: "+format_email)

format_email = email.lower()
print("Transformed Email: "+format_email)

# Attach @gmail.com
format_email = email.lower() + "@gmail.com"
print("Transformed Email: "+format_email)

#         RaVI2KRIshNA 
# Remove Spaces 
format_email = format_email.strip()
print("Transformed Email: "+format_email)

# Simulate PAN Functionality
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm

pan = input("Enter PAN ID: ")
print("Original PAN: "+pan) # $jkop7712q
print(pan.isalnum())

if pan.isalnum() and len(pan) == 10: 
    print("Original PAN: "+pan)
    print("Formatted PAN: "+pan.upper())
else:
    print(f"Given {pan} PAN is Invalid")
    
# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
# https://www.businessbloomer.com/wp-content/uploads/2014/11/woocommerce-add-coupon-automatically-to-cart-if-product.png

phone_number = input("Enter Phone Number With ISD Code: ")
print(phone_number.startswith("+91"))

if phone_number.startswith("+91"):
    print("Calling Indian Number - Charged In Rupees")
    
elif phone_number.startswith("+33"):
    print("Calling France Number - Charged In Euros")
    
elif phone_number.startswith("+1"):
    print("Calling USA Number - Charged In Dollars")

else:
    print("Invalid Number - Calling Is Supported Only For India, France and USA")
    
    
# Simulate Email Synchronization w.r.t gmail
source_email = input("Enter Source Email ID: ")
destination_email = input("Enter Destination Email ID: ")

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Backup Process Started")
else:
    print("Email Backup Process Failed - Source and Destination Didn't Match")
    
# Simulate Data Operations Work: CSV Data from a file and perform some operations 
# Name, Email, Age, City, Job_Role
# emp_data = "John,john@gmail.com,35,Hyderabad,Developer"
emp_data = "Jennifer,Jennifer@gmail.com,35,Hyderabad,Developer"

# Requirement: Display Employee Name & Job Role
emp_name = emp_data[0:4]
emp_email = emp_data

print("Employee Name: "+emp_name)
print("Employee Email: "+emp_email)

# Above is Hardcoded logic, it's not Dynamic 

emp_data = "Jennifer,Jennifer@gmail.com,35,Hyderabad,Developer"
# Requirement: Display Employee Name & Job Role
emp_data_test = "Jennifer Jennifer@gmail.com 35 Hyderabad Developer"
emp_data_test_extraction = emp_data_test.split()
print(emp_data_test_extraction)
print("Employee Name: "+emp_data_test_extraction[0])
print("Employee Role: "+emp_data_test_extraction[-1])

emp_data_extraction = emp_data.split(",")
print("Employee Name: "+emp_data_extraction[0])
print("Employee Role: "+emp_data_extraction[-1])