## Python code to detect the age and define the fair of the ticket to the customer:

age=int(input("\nEnter your age: \t")) # getting the age information
if age<5:
    print("You have a Free Ticket") 
else:
    is_student=input("\nAre you a student: \t").lower()  # incase of age more than 5 then checking if student or not to define the fair
    value="yes"
    if is_student==value:                                   # students have less fair
        if age<10:
            print("Ticket amount to be paid is: Rs.5/-")
        elif age<15:
            print("Ticket amount to be paid is: Rs.10/-")
        elif age<25:
            print("Ticket amount to be paid is: Rs.15/-")
        elif age<30:
            print("Ticket amount to be paid is: Rs.20/-")
    else:                                                    # non-students have high fair       
        if age<10:  
            print("Ticket amount to be paid is: Rs.25/-")
        elif age<15:
            print("Ticket amount to be paid is: Rs.30/-")
        elif age<25:
            print("Ticket amount to be paid is: Rs.35/-")
        elif age<30:
            print("Ticket amount to be paid is: Rs.40/-")
        
