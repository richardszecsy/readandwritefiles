import csv

sales_report = open("sales.csv", "r")
sales = csv.reader(sales_report, delimiter = ",")
outfile = open("salesreport.csv", "w")
next(sales)
new = []
prev_id = None
running_total = 0
for Cid in sales:
    cust_id = int(Cid[0])
    sub_total = float(Cid[3])
    sales_tax = float(Cid[4])
    freight = float(Cid[5])
    total = sub_total + sales_tax + freight
    
    if prev_id != cust_id:
        if prev_id is not None:
            new.append([cust_id, round(total, 2)])
        prev_id = cust_id
        sales_total = sub_total + sales_tax + freight
    else:
        sales_total = sub_total + sales_tax + freight
    outfile.write( "Customer ID:" + "Total Pay\n")

for row in new:
    outfile.write(str(row[0]) + " " + str(row[1]))
    outfile.write("\n")

outfile.close()



