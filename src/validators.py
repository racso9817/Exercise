"""
    Convert time to 24:00 if it is 00:00.
    @param time: The time to be converted.
    @return: The converted time.
"""
def convertTo24(time):
    if time == '00:00':
        time = '24:00'
    return time


"""
    Convert the time in string format into a time difference in hours considering the minutes.
    @param time1: The first time.
    @param time2: The second time.
    @return: The time difference in hours.
"""
def converToHours(time1, time2):
    hour1 = int(time1.split(':')[0]) + (float(time1.split(':')[1]) / 60)
    hour2 = int(time2.split(':')[0]) + (float(time2.split(':')[1]) / 60)
    differenceHour = hour2 - hour1
    if differenceHour == 0:
        differenceHour = 1/60
    return differenceHour