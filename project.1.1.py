# Project 1.1    -   Luca Daloia
# Determine the smallest conduit that can hold a certain amount of cables
# July 2023
# 22+ total hours
# Absolute Address: C:/Users/Luca/Desktop/Project1/project.1.1.py


# predefine certain variables to be used:
pi = 3.1415926535897932384626433832795
import math
import os
import time
# defining formula to find needed information of CAT6 cable:
def CAT6():
    x = float(input("Nominal Diameter of the CAT6 cable: "))
    y = x/2
    z = pow(y, 2) * pi
    return z

#
class Cable:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.num_cables = None

# predefine function 0:
def func0():
    #is that all?
    in2 = input("                                                                           Is that all? ")
    valid_in = ["y", "n"]
    while in2 not in valid_in:
        print("\n                                                                    ----- Invalid input! -----")
        in2 = input("\n                                                                           Is that all? ")
    
    if in2 == "y":
            time.sleep(0.4)
            os.system('cls')
            print("\n\n                                                                              Goodbye!!!")
            time.sleep(1.5)
            os.system('cls')
    elif in2 == "n":
            os.system('cls')
            func3()
            func0()
            

#predefine function 3:
def func3():

    # Get the desired number of objects from the user
    num_objects = int(input("Enter the number of different types of cables that will be used: "))
        
    # Create the specified number of objects
    objects = []
    for i in range(num_objects):
        name = input("\nEnter the type of cable {}: ".format(i + 1)) #getting name for object
        obj = Cable(name)
        print("\nWhat is the diameter in inches of the", name, sep = " ", end = " ") #get diam of cable

        cable_diam = float(input("cable? "))
        cable_radius = cable_diam/2

        print("\nHow many", name, sep = " ", end = " ")

        num_cables = int(input( "cables will be used? ")) # get num of cables
        cable_area = pow(cable_radius, 2) * pi 
        cabletot_area = num_cables * cable_area
        obj.area = cabletot_area
        obj.num_cables = int(num_cables)
        objects.append(obj)

    os.system('cls')

    total_cable_area = 0 #predefining object (idk why)
    for obj in objects:
        print("\nThe total area of", obj.name, "cables is: ", round(obj.area, 4), "squared in" ,sep = " ", end = "")
    for obj in objects:
        total_cable_area += obj.area
    print("\nThe total area of all the cables is:", round(total_cable_area, 4), "squared in")
    total_num_cables = 0
    for obj in objects:
        total_num_cables += obj.num_cables
        if total_num_cables == int(1):
            percentage = 0.53
            percent = str("53%")
        elif total_num_cables == int(2):
            percentage = 0.31
            percent = str("31%")
        else:
            percentage = 0.4 
            percent = str("40%")
        
    in5 = input("\n\nPress Enter to continue.")
    while in5 != "":
        nothing = 0
    if in5 == "":
        os.system('cls')

    # DATA ON CONDUITS
    # data for conduit 3/4 (0.75)
    cond_075 = 0.836
    cond_area_075 = pow(cond_075/2, 2)*pi
    cond_area_percent_075 = cond_area_075 * float(percentage)

    # data for conduit 1 
    cond_1 = 1.063
    cond_area_1 = pow(cond_1/2, 2)*pi
    cond_area_percent_1 = cond_area_1 * float(percentage)

    # data for conduit 1 1/2 (1.5)
    cond_15 = 1.624
    cond_area_15 = pow(cond_15/2, 2)*pi
    cond_area_percent_15 = cond_area_15 * float(percentage)

    # data for conduit 1 1/2 (1.5)
    cond_2 = 2.083
    cond_area_2 = pow(cond_2/2, 2)*pi
    cond_area_percent_2 = cond_area_2 * float(percentage)


    if total_cable_area <= cond_area_percent_075:
        smallest = str("3/4 (0.75)")
    elif total_cable_area <= cond_area_percent_1:
        smallest = str("1")
    elif total_cable_area <= cond_area_percent_15:
        smallest = str("1 1/2 (1.5)")
    elif total_cable_area <= cond_area_percent_2:
        smallest = str("2")

    os.system('cls')
    print("                                                  The smallest conduit that can be used is: ", smallest, sep = "" )
    #
    #Press enter to continue:

    in4 = input("                                                               Press Enter to continue.")
    if in4 == "":
        os.system('cls')
    elif in4 != "":
        nothing = 0
    # generate response:

###################################################################################
#               BEGINNING:

os.system('cls')
print("                                                                             HELLO! \n")

print("\n              This Program determines the smallest conduit that can support/hold a certain amount of cables (according to regulations - NAME).")
in3 = input("\n                                                                    Press Enter to begin")

#  Press Enter to begin

if in3 == "":
    os.system('cls')
    func3()
    func0()
while in3 != "":
    nothing = 0
























