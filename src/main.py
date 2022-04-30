import variables as var #import variables.py file
import functions as func #import functions.py file
import validators as val #import validators.py file

var.lista = func.readFile("src/info.txt")
func.employeeDict(var.lista, var.info_dict)
timeCounter = 1
while timeCounter != 0:
    tuple1 = func.checkTimeRates(var.info_dict, var.employee_names)
    timeCounter = tuple1[1]
    var.info_dict = {}
    var.info_dict = tuple1[0]
# print(var.info_dict) #debugging
# print(var.employee_names) #debugging

#main program
# while True:
    #creating a menu for the user of the program
    # print("\nEnter the name of the employee you want to calculate the amount of pay for \n")
    # print("You can choose between the following names: ", var.employee_names, '\n')    
    # name = input("Enter the name of the employee: ").upper()
    # if(val.validateInput(name, var.employee_names)): #if the name is valid
        #\033[1;31m is the color code for red
        #\033[1;32m is the color code for green
        #\033[1;39m is the color code for default
        #\033[1;42m is the color code for green background
        #\033[1;49m is the color code for default background
        # print("\n \033[1;32m {name} exists\n \033[1;39m".format(name=name))
for i in var.employee_names:
    func.validateTimeRate(var.info_dict, i)
    print("\n \033[1;42m The amount to pay {name} is:".format(name=i),"{:.2f} USD.\033[1;49m".format(var.employee_payment))
    var.employee_payment = 0 #resets the amount of pay for the next employee

    # else:
    #     print(("\n \033[1;31m {name} is an invalid name. Please try again.\n \033[1;39m".format(name=name)))