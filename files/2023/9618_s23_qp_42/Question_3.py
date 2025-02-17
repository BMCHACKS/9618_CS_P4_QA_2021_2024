

class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay = HourlyPay # DECLARE PRIVATE Hourlypay : REAL
        self.__EmployeeNumber = EmployeeNumber # DECLARE PRIVATE EmployeeNumber : STRING
        self.__JobTitle = JobTitle # DECLARE PRIVATE JobTitle : STRING
        self.___PayYear2022 = [0.0 for _ in range(52)] # DECLARE PRIVATE PayYear2022 : ARRAY[0:51] OF REAL

    def GetEmployeeNumber(self): return self.__EmployeeNumber
    def SetPay(self, week_number, hours_worked):
        pay = hours_worked * self.__HourlyPay
        self.___PayYear2022[week_number] = pay
    
    def GetTotalPay(self): 
        total = 0
        for pay in self.___PayYear2022: total += pay
        return total


class Manager(Employee):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue = BonusValue # DECLARE PRIVATE BonusValue : REAL

    def SetPay(self, week_number, hours_worked):
        new_hours_worked = hours_worked + (hours_worked * (self.__BonusValue/100))
        super().SetPay(week_number, new_hours_worked)


def EnterHours():
    try:
        file = open("HoursWeek1.txt", 'r')
        for line in file:
            employee_id = line.rstrip()
            hours_worked = float(file.readline().rstrip())
            for x in range(len(EmployeeArray)):
                if EmployeeArray[x].GetEmployeeNumber() == employee_id:
                    EmployeeArray[x].SetPay(1, hours_worked)
                    break
    except IOError:
        print("[ERROR] File Not Found")

# main


EmployeeArray = []

temp_array = []
try:
    file =  open("Employees.txt", 'r')
    for line in file: temp_array.append(line.rstrip())
except IOError:
    print("[ERROR] File Not Found")


counter = 0
for x in range(len(temp_array)):
    counter += 1
    if counter == 3:   
        if temp_array[x][0] not in '123456789': 
            EmployeeArray.append(Employee(float(temp_array[x-2]), temp_array[x-1], temp_array[x]))
            counter = 0
        else:
            EmployeeArray.append(Manager(float(temp_array[x-2]), temp_array[x-1], temp_array[x+1], float(temp_array[x])))
            counter = -1
    

EnterHours()
for employee in EmployeeArray: print(f"{employee.GetEmployeeNumber()} {employee.GetTotalPay()}")
