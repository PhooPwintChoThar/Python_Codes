name=input("Enter employee's Name : ")
hours_worked=float(input("Enter number of hours worked in a week : "))
pay_rate=float(input("Enter hourly pay rate : "))
federal_tax_rate=float(input("Enter federal tax withholding rate : "))
state_tax_rate=float(input("Enter state tax withholding rate : "))

print("\n")
print("Employee Name : ",name)
print("Hours Worked : ", hours_worked)
print("Pay Rate : $"+str(pay_rate))

gross_pay=hours_worked * pay_rate
print("Gross Pay : $" +str(round(gross_pay,2)))

federal_tax=gross_pay * federal_tax_rate
state_tax=gross_pay * state_tax_rate
total_deduction=federal_tax + state_tax
print("Deductions:")
print(f"\tFederal Withholding({format(federal_tax_rate, "5.2%")}) : $" + str(round(federal_tax,2)))
print(f"\tState Withholding ({format(state_tax_rate, "5.2%")}) : $" + str(round(state_tax,2)))
print(f"\tTotal Deduction : $" + str(round(total_deduction,2)))

net_pay=gross_pay - total_deduction
print("Net Pay : $" + str(round(net_pay,2)))


