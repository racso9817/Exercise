from datetime import datetime
import variables as var

"""
    Validate input from the user.
    @param input: The input from the user.
    @param list: The list of valid inputs.
    @return: True if the input is valid, False otherwise.
"""
def validateInput(input, list):
    if input in list:
        return True
    else:
        return False


"""
    Search for what time rate the employee is working.
    @param timeRate: Time rate working hours.
    @param employeeTimeRate: The employee's time rate.
    @return: True if the time rate is valid, False otherwise.
"""
def validateTimeRate(timeRate, employeeTimeRate):
    timesList = []
    employeeTimesList = []
    print(timeRate)
    print(employeeTimeRate)
    employeeTimeRatelist = employeeTimeRate.split('-')
    timeRatelist = timeRate.split('-')
    print(timeRatelist)
    print(employeeTimeRatelist)
    timeRatelist[0] = datetime.strptime(timeRatelist[0], '%H:%M')
    timeRatelist[1] = datetime.strptime(timeRatelist[1], '%H:%M')
    timesList.append(timeRatelist[0].time())
    timesList.append(timeRatelist[1].time())
    print(timesList)
    employeeTimeRatelist[0] = datetime.strptime(employeeTimeRatelist[0], '%H:%M')
    employeeTimeRatelist[1] = datetime.strptime(employeeTimeRatelist[1], '%H:%M')
    employeeTimesList.append(employeeTimeRatelist[0].time())
    employeeTimesList.append(employeeTimeRatelist[1].time())
    print(employeeTimesList)
    if timeRatelist[0] >= employeeTimeRatelist[0] and timeRatelist[1] <= employeeTimeRatelist[1]:
        return True
    else:
        return False