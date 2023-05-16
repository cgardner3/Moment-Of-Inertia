'''
Write a program that will use functions that will be made for each of
the different structures. In each of the different functions, the user will
be asked to be inputted all of the dimensions for that beam. The program will then
calculate the moment of inertia and print the details in the main method.
The program will continue to loop and start over as long as that user wants to
continue again.

Author: Cheryl Gardner
Course: ITM 313
'''

#Declare the greeting function that will welcome the user to the calculator
def greeting():
    print("Welcome to the Moment of Intertia Calculator")

#Define the iBeam function 
def iBeam():
    #Ask the user for the four dimensions needed to calculate the moment of inertia
    B = eval(input("Enter the value of the base, B "))
    H = eval(input("Enter the value of the height, H "))
    b = eval(input("Enter the value of the little base, b/2 "))
    h = eval(input("Enter the value of the little height, h "))
    #Print the space buffer between input and output
    print("")
    #Calculate the inertia and return it back to the main function
    inertia = ((B*H*H*H)-(2*b*h*h*h))/12
    return inertia

#Define the rectangularBeam function
def rectangularBeam():
    #Ask the user for the two dimensions needed to calculate the moment of inertia
    b = eval(input("Enter the value of the base, b "))
    h = eval(input("Enter the value of the height, h "))
    #print a space buffer
    print("")
    #Calculate the moment of inertia and return it to the main function
    inertia = (b*h*h*h)/12
    return inertia

#Define the cylindricalBeam function
def cylindricalBeam():
    #Ask the user for the redius of the cylinder
    r = eval(input("Enter the value of the radius, r "))
    #Print a space buffer
    print("")
    #Calculate the moment of inertia and return it to the main function
    inertia = (3.14*r*r*r*r)/4
    return inertia

#Define the main function   
def main():
    #Ask the user what type of beam they want to be calculated
    selection = input("What type of beam do you want to be calculated, A for I-Beam, B for Rectangular Beam or C for Cylindrical Beam: ")
    #Declare choice variable to y so that it enters the loop
    choice = 'y'

    #Start the while loop
    while (choice == 'y'):
        #If the user selected a, then do this
        if (selection == 'a' or selection == 'A'):
            #Display the moment of inertia and then print a space buffer
            print("The value of the moment of inertia for the given shape is %.4f" % iBeam())
            print("")

        #If the user selected b, then do this
        if (selection == 'b' or selection == 'B'):
            #Display the moment of inertia and then print a space buffer
            print("The value of the moment of inertia for the given shape is %.4f" % rectangularBeam())
            print("")

        #If the user selected c, then do this             
        if (selection == 'c' or selection == 'C'):
            #Display the moment of inertia and then print a space buffer
            print("The value of the moment of inertia for the given shape is %.4f" % cylindricalBeam())
            print("")

        #Ask the user if they want to continue
        choice = input("Do you want to do the calculation for another shape? Enter y or n ")

        #If the user says yes, then ask what type of beam they want to calculate
        if(choice == 'y'):

            selection = input("What type of beam do you want to be calculated, A for I-Beam, B for Rectangular Beam or C for Cylindrical Beam: ")

#Declare the closing function
def closing():
    #print a space buffer and thank the user for using the calculator
    print("")
    print("Thank you for using our calculator! Come again soon!")

#Call the greeting function
greeting()
#Call the main function
main()
#Call the closing function
closing()
