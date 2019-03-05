import os
import csv

csvpath = 'election_data.csv'

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    count = 0
    pollresults = {}
    next(csvreader)
    for row in csvreader:
        count = count + 1
        if row[2] not in pollresults:
            pollresults[row[2]]= 0
        pollresults[row[2]] +=1

print('Election Results')
print('-------------------------')
print(f'Total Votes: {count}')
print('-------------------------')
mostvotes = 0
for key,val in pollresults.items():
    if val > mostvotes:
        mostvotes = val
        winner = key
    percent = round((val/count)*100,3)
    print(f'{key}: {percent}% ({val})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

txtfile = open('output.txt','w')
txtfile.write('Election Results\n')
txtfile.write('-------------------------\n')
txtfile.write('Total Votes:'+ str(count))
txtfile.write('\n-------------------------')
for key,val in pollresults.items():
    percent = round((val/count)*100,3)
    txtfile.write(f'\n{key}: {percent}% ({val})')
txtfile.write('\n-------------------------')
txtfile.write(f'\nWinner: {winner}')
txtfile.close()

