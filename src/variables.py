#Days of the week
MO = "Monday"
TU = "Tuesday"
WE = "Wednesday"
TH = "Thursday"
FR = "Friday"
SA = "Saturday"
SU = "Sunday"

payment = 0 #payment variable for the employee

#list of tuples for payment rates
weekdays = [("00:01-09:00",25),("09:01-18:00",20),("18:01-00:00",15)] #MO-FR
weekends = [("00:01-09:00",30),("09:01-18:00",20),("18:01-00:00",25)] #SA-SU

info_dict = {} #empty dictionary for information gathered from the info.txt file
lista = [] #empty list for the lines of the info.txt file
employee_names = [] #empty list for the names of the employees