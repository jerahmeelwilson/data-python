
import csv


invoices = open('CupcakeInvoices.csv')

for order in invoices:
    print(order)

with open("CupcakeInvoices.csv") as invoices:
    reader = csv.reader(invoices)
    for row in reader:
        print(row[2])

with open("CupcakeInvoices.csv") as invoices:
    reader = csv.reader(invoices)
    for row in reader:
        print(round(int(row[3]) * float(row[4]),2))

total = 0

with open("CupcakeInvoices.csv") as invoices:
    reader = csv.reader(invoices)
    for row in reader:
        total = round(total + int(row[3]) * float(row[4]),2)

print(total)



invoices.close()