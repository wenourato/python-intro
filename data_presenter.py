cupcake_invoices = open("CupcakeInvoices.csv")

# for line in cupcake_invoices:



#  cupcake_invoices.seek(0,0)

# for line in cupcake_invoices:
#     if 'Chocolate' in line:
#         print('Chocolate')
#     elif 'Vanilla' in line:
#         print('Vanilla')
#     elif 'Strawberry' in line:
#          print('Strawberry')


# for line in cupcake_invoices:
#     results = line.rstrip('\n').split(',')
#     price = float(results[-1])
#     print(price)

total = 0

for line in cupcake_invoices:
    results = line.rstrip('\n').split(',')
    price = float(results[-1]) * float(results[-2])

    total = total + price
print(round(total, 2))






# cupcake_invoices.seek(0,0)
# for line in cupcake_invoices:
#     line = line.rstrip('\n').split(',')
#     print(line)
#     cost = []
#     value_one = float(line[-1])
#     value_two = float(line[-2])
#     order_total = value_one * value_two
#     cost.append(order_total)
#     print(cost)


cupcake_invoices.close()