#Endrit Ngjelina
#SPC ID#2436798
#COP1000
#Worked alone
#This program calculates the regular pay, overtime pay and total pay of an employee.
#User inputs their hourly pay rate.
#User inputs hours worked.
#Program calculates and displays pay. 

#User inputs pay rate
hourly_pay = float(input('Enter your hourly pay rate: '))

#User inputs hours worked
hours_worked = float(input('Enter your hours worked last week: '))

#Constant for regular hours
REGULAR_HOURS = 40
#Constant for overtime
OVERTIME = 1.5

#Program calculates if there is overitme pay
#If not, it continues calculatoins normally
if hours_worked > REGULAR_HOURS:
    regular_pay = REGULAR_HOURS * hourly_pay
    overtime_hours = hours_worked - REGULAR_HOURS
    overtime_pay = overtime_hours * (hourly_pay * OVERTIME)
    total_pay = (REGULAR_HOURS * hourly_pay) + overtime_pay
    taxes = total_pay * 0.07
    total = total_pay - taxes
else:
    total = hours_worked * hourly_pay
    taxes = total * 0.07
    regular_pay = total
    overtime_pay=0


print(f'Regular pay: ${regular_pay:,.2f}.')
print(f'Overtime pay: ${overtime_pay:,.2f}.')
print(f'Taxes: ${taxes:,.2f}.')
print(f'Total pay: ${total:,.2f}.')

