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
    Read the dictionary from previous function and checks for time rates.
    @param dict: The dictionary to check.
    @param namesList: The list of names to check.
    @return: The dictionary with the updated information of the employees and the updated counter.
"""
def checkTimeRates(dict, namesList):
    counter = 0
    newDict = {}
    for i in range(len(namesList)):
        emptyList = []
        info = dict[namesList[i]]
        newDict[namesList[i]] = {}
        for j in range(len(info)):
            # print(len(info), 'longitud de info')
            if j % 2 == 0:
                time1 = info[j+1].split("-")[0]
                time2 = info[j+1].split("-")[1]
                val.convertTo24(time2) #convert 00:00 to 24:00
                for k in range(len(var.time_rate)):
                    if time1 >= var.time_rate[k][0] and time1 <= var.time_rate[k][1]:
                        if time2 <= var.time_rate[k][1]:
                            emptyList.append(info[j])
                            emptyList.append(info[j+1])
                        else:
                            counter += 1
                            emptyList.append(info[j])
                            emptyList.append(time1 + "-" + var.time_rate[k][1])
                            emptyList.append(info[j])
                            emptyList.append(var.time_rate[k+1][0] + "-" + time2)
        newDict[namesList[i]] = emptyList
                            # print(namesList[i],info[j], time1, var.time_rate[k][0], var.time_rate[k][1])
    return newDict, counter
    

"""
    Calculate the amount to pay to employees.
    @param dict: The dictionary with the information of the employees.
    @param: the name of the employee.
    @return: The amount to pay to employees.
"""
def validateTimeRate(dict, name):
    list = dict[name]
    for i in range(len(list)):
        if i % 2 == 0:
            time1 = list[i+1].split("-")[0]
            time2 = list[i+1].split("-")[1]
            if list[i] == 'MO' or list[i] == 'TU' or list[i] == 'WE' or list[i] == 'TH' or list[i] == 'FR':
                for j in range(len(var.time_rate)):
                    if time1 >= var.time_rate[j][0] and time2 <= var.time_rate[j][1]:
                        var.employee_payment += var.payment[j][0] * val.converToHours(time1, time2)
                        # print(list[i], var.employee_payment, var.payment[j][0], converToHours(time1, time2)) #debugging
            elif list[i] == 'SA' or list[i] == 'SU':
                for j in range(len(var.time_rate)):
                    if time1 >= var.time_rate[j][0] and time2 <= var.time_rate[j][1]:
                        var.employee_payment += var.payment[j][1] * val.converToHours(time1, time2)
                        # print(list[i], var.employee_payment, var.payment[j][1], converToHours(time1, time2)) #debug