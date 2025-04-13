num1=int(input("\nEnter the first number:"))
num2=int(input("\nEnter the second number:"))
choice=int(input("\n Select the number for the operation: \n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division \n 5. Floor division \n 6. Modulus Division \n 7. Exponent power\n \nEnter the value here:"))

if choice==1:
    print("\nAddition of ", num1 , "and" , num2 , "is :" , num1+num2)
elif choice==2:
    print("\nSubstraction of ", num1 , "and" , num2 , "is :" , num1-num2)
elif choice==3:
    print("\nMultiplication of ", num1 , "and" , num2 , "is :" , num1*num2)
elif choice==4:
    print("\nDivision of ", num1 , "and" , num2 , "is :" , num1/num2)
elif choice==5:
    print("\nFloor Division of ", num1 , "and" , num2 , "is :" , num1//num2)
elif choice==6:
    print("\nModulus Division of ", num1 , "and" , num2 , "is :" , num1%num2)
elif choice==7:
    print("\n", num1 , "raised to power of" , num2 , "is :" , num1**num2)
else:
    print("\nenter valide numbers from the options")