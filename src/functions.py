import variables as var
import validators as val

"""
    Reads a file and returns a list of lines.
    @param filename: The name of the file to read.
    @return: A list of lines on the txt file.
"""
def readFile(filename):
    with open(filename, 'r') as file:
        list = file.readlines() #readlines() returns a list of lines
    for i in range(len(list)): #for loop to remove the \n from each line
        list[i] = list[i].replace("\n", "")
    return list #returns the list of lines

"""
    Creates a dictionary with the information of the employees.
    @param list: The list of lines from the info.txt file.
    @param dict: The dictionary to add the information to.
    @return: The dictionary with the information of the employees.
"""

def employeeDict(list, dict):
    for i in range(len(list)):
        emptyList = []
        line = list[i].split("=") #splits the line into a list of 2 elements
        var.employee_names += [line[0]] #adds the name of the employee to the list of names
        line1Split = line[1].split(",") #splits the line into a list of 3 elements
        #print(line1Split) #debugging
        for j in range(len(line1Split)):
            string = line1Split[j]            
            emptyList.append(string[:2])
            emptyList.append(string[2:])
        #print(emptyList) #debugging
        dict[line[0]] = emptyList
    return dict #returns the dictionary

"""
    Retrieve information about payment
    @param dict: The dictionary with the information of the employees.
    @param name: The name of the employee.
    @return: The information of the payment of the employee.
"""
def retrievePaymentInfo(dict, name):
    employeeInfo = dict[name] #returns the information of the employee according to the name
    #print(employeeInfo)
    for i in range(len(employeeInfo)):
        if i % 2 == 0:
            if (employeeInfo[i] == "MO" or employeeInfo[i] == "TU" or employeeInfo[i] == "WE" or employeeInfo[i] == "TH" or employeeInfo[i] == "FR"):
                print('weekdays')
                print(employeeInfo[i], employeeInfo[i+1])
                print(val.validateTimeRate(employeeInfo[i],employeeInfo[i+1]))
                var.employee_payment += val.validateTimeRate(employeeInfo[i],employeeInfo[i+1])
            elif (employeeInfo[i] == "SA" or employeeInfo[i] == "SU"):
                print('weekends')
                print(employeeInfo[i], employeeInfo[i+1])
                print(val.validateTimeRate(employeeInfo[i],employeeInfo[i+1]))
                var.employee_payment += val.validateTimeRate(employeeInfo[i],employeeInfo[i+1])
    return var.employee_payment