import csv


infile = open("EmployeePay.csv", "r")

employee_file = csv.reader(infile, delimiter = ",")
next(employee_file)

for record in employee_file:
    pay = float(record[3])
    bonus = float(record[4])* float(record[3])
    total = pay * bonus
    print("First name:", record[1])
    print("Last name:", record[2])
    print("Pay:", pay)
    print("Bonus:", bonus)
    print("Total Pay:", total)
