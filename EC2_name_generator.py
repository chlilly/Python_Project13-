import time 
import random
import string


#Random name generator function
def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

department = input("Enter the department name Accounting, FinOps, or Marketing.\n").upper()  
    
for _ in department:
    
    if department == "Marketing" or department.lower() == "marketing":
        print("Verfication in process, one moment please...")
        time.sleep(6)
        break
    
    elif department == "FinOps" or department.lower() == "finops":
        print("Verification in process, one moment please...")
        time.sleep(6)
        break
    
    elif department == "Accounting" or department.lower() == "accounting":
        print("Processing, one moment please...")
        time.sleep(6)
        break
    
    else:
        print("Error : Department not verified. Enter the correct Department to gain access.")
        raise TimeOut
        time.sleep(6)  

        
number = int(input("Input the number of EC2 instances that require names: "))
    
if number < 0:
    print("Please enter at least one number: ")
elif number > 0:
    print("Input accepted")
    
#Results should be printed
print("\n...Generating Results...\n")
time.sleep(10)
print("Here are your results!!")

for _ in range(1, number + 1):
    EC2_name = department
    unique_name = EC2_name + "-" + string_generator()
    print("Your New EC2 Instance Name : ", unique_name)
    
print("Complete! Thank you for using the name generator!!")

