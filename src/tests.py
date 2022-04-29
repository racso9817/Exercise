from datetime import datetime
import validators as val

time1 = datetime.strptime('00:20', '%H:%M').time()
time2 = datetime.strptime('09:30', '%H:%M').time()

#convert minutes into hours
def convertMinutesToHours(minutes):
    return minutes / 60

minutes1 = convertMinutesToHours(time1.minute)
minutes2 = convertMinutesToHours(time2.minute)

#print((time2.hour - time1.hour) + minutes2 - minutes1)

print(val.validateTimeRate("MO", "19:00-20:00"))

# if datetime.strptime('21:00', '%H:%M').time() < datetime.strptime('00:00', '%H:%M').time():
#     print("true")
# else:
#     print("false")