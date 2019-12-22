
import os
import csv

def print_percentages(PyBank_data):
    Months = str(PyBank[0])
    Budget = float(PyBank[1])

#Path to collect data from the Resources folder

PayBank_csv = os.path.join( 'Resources', 'budget_data.csv')

 #Open and read csv
with open(PayBank_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
  # Read the header row first (skip this part if there is no header) 
    next(csvreader)
    header = next(csvreader)
    previous = int(header[1])
    max = int(header[1])
    min = int(header[1])
    Total= int(header[1])
    total_changes = 0
    #print(header)
    #print (previous)

    # looping thorugh the file 
    months=1
    
    for row in csvreader:
       #print(row)
        current = int(row[1])
        #print (current)
        change = current- previous 
        total_changes=total_changes + change
        Total = Total + current
        months=months + 1
        if change > max:
            max = change
            date_max= row [0]
        if change < min:
            min = change 
            date_min= row [0]
        previous = current 

average = (total_changes/(months-1))

print("Financial Analysis")
print("-----------------------")
print("Total Months:" +str(months))
print("Total: $" + str(Total))
print (f'Average  Change: ${average}')
print(f'Greatest Increase in Profits:{date_max} ${max}') 
print(f'Greatest Decrease in Profits:{date_min} ${min}')

PayBank_outcsv = os.path.join( 'Resources', 'PyBank_data.csv')
with open(PayBank_outcsv, 'w', newline='') as csvfile1:
    csvwriter = csv.writer(csvfile1, delimiter=',')
    csvwriter.writerow (["Financial Analysis"])
    csvwriter.writerow (["-----------------------"])
    csvwriter.writerow (["Total Months:" +str(months)])
    csvwriter.writerow (["Total: $" + str(Total)])
    csvwriter.writerow ([f'Average  Change: ${average}'])
    csvwriter.writerow ([f'Greatest Increase in Profits:{date_max} ${max}']) 
    csvwriter.writerow ([f'Greatest Decrease in Profits:{date_min} ${min}'])
