import os
import csv

csvpath = 'budget_data.csv'

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    count = 0
    total = 0
    old = 0
    change = []
    maxgain = 0
    maxloss = 0

    next(csvreader)
    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        dif = int(row[1])-old
        change.append(dif)
        old = int(row[1])
        if dif > maxgain:
            maxgain = dif
            gaindate = row[0]
        if dif < maxloss:
            maxloss = dif
            lossdate = row[0]

change.pop(0)    
average = sum(change)/len(change)
bigup = max(change)
bigdown = min(change)
print('Financial Analaysis')
print('-------------------------')
print(f'Total Months: {count}')
print(f'Total: ${total}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {gaindate} (${bigup})')
print(f'Greatest Decrease in Profits: {lossdate} (${bigdown})')

txtfile = open('output.txt','w')
txtfile.write('Financial Analaysis')
txtfile.write('-------------------------')
#txtfile.write(f'Total Months: {count}')
#txtfile.write(f'Total: ${total}')
#txtfile.write(f'Average Change: ${average}')
#txtfile.write(f'Greatest Increase in Profits: {gaindate} (${bigup})')
#txtfile.write(f'Greatest Decrease in Profits: {lossdate} (${bigdown})')
txtfile.close() 