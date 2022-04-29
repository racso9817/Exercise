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
    Convert minutes into hours
"""
def convertMinutesToHours(minutes):
    return minutes / 60

"""
    Search for what time rate the employee is working.
    @param employeeTimeRate: The employee's time rate.
    @return: True if the time rate is valid, False otherwise.
"""
def validateTimeRate(day,employeeTimeRate):
    employeeTimeRate = employeeTimeRate.split("-")
    #convert string into time format
    time1 = datetime.strptime(employeeTimeRate[0], '%H:%M') #start time
    minute1 = convertMinutesToHours(time1.minute)
    time2 = datetime.strptime(employeeTimeRate[1], '%H:%M') #end time
    minute2 = convertMinutesToHours(time2.minute)
    #print(time1.time(), time2.time()) #debugging
    if day == "MO" or day == "TU" or day == "WE" or day == "TH" or day == "FR":
        if time1.time() < time2.time(): #validate if working time is correctly established
            if time1.time() >= datetime.strptime('00:01', '%H:%M').time() and time2.time() <= datetime.strptime('09:00', '%H:%M').time():
                return var.payment[0][0] * ((time2.hour - time1.hour) + minute2 - minute1)
            elif time1.time() >= datetime.strptime('09:01', '%H:%M').time() and time2.time() <= datetime.strptime('18:00', '%H:%M').time():
                return var.payment[1][0] * ((time2.hour - time1.hour) + minute2 - minute1)
            elif time1.time() >= datetime.strptime('18:01', '%H:%M').time() and time2.time() >= datetime.strptime('00:00', '%H:%M').time():
                return var.payment[2][0] * ((time2.hour - time1.hour) + minute2 - minute1)
    elif day == "SA" or day == "SU":
        if time1.time() < time2.time(): #validate if working time is correctly established
            if time1.time() >= datetime.strptime('00:01', '%H:%M').time() and time2.time() <= datetime.strptime('09:00', '%H:%M').time():
                return var.payment[0][1] * ((time2.hour - time1.hour) + minute2 - minute1)
            elif time1.time() >= datetime.strptime('09:01', '%H:%M').time() and time2.time() <= datetime.strptime('18:00', '%H:%M').time():
                return var.payment[1][1] * ((time2.hour - time1.hour) + minute2 - minute1)
            elif time1.time() >= datetime.strptime('18:01', '%H:%M').time() and time2.time() >= datetime.strptime('00:00', '%H:%M').time():
                return var.payment[2][1] * ((time2.hour - time1.hour) + minute2 - minute1)