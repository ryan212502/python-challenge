import os
import csv

csvpath = os.path.join("Bank1.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    total = 0
    for current_row in csvreader:
        total += int(current_row[1])

    
    row_count1 = int(csvreader.line_num - 1)
   
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    max_revenue_row1 = None
    min_revenue_row1 = None
    revenue1 = []

    for current_row in csvreader:
        change = int(current_row[1])
        revenue1.append(change) 

        current_row_revenue1 = int(current_row[1])
        
        if max_revenue_row1 == None:
            max_revenue_row1 = current_row

        if min_revenue_row1 == None:
            min_revenue_row1 = current_row

        current_max_revenue1 = int(max_revenue_row1[1])

        if current_max_revenue1 < current_row_revenue1:
            max_revenue_row1 = current_row 

        current_min_revenue1 = int(min_revenue_row1[1])

        if current_min_revenue1 > current_row_revenue1:
            min_revenue_row1 = current_row 

    avg_revenue1 = [x - revenue1[i - 1] for i, x in enumerate(revenue1)][1:]
    
csvpath = os.path.join("Bank2.csv")

with open(csvpath, newline="") as csvfile:
    csvreader3 = csv.reader(csvfile, delimiter=",")
    next(csvreader3, None)

    total2 = 0
    for current_row in csvreader3:
        total2 += int(current_row[1])

    row_count2 = int(csvreader3.line_num - 1)

with open(csvpath, newline="") as csvfile:
    csvreader3 = csv.reader(csvfile, delimiter=",")
    next(csvreader3, None)
    max_revenue_row2 = None
    min_revenue_row2 = None
    revenue2 = []
    for current_row in csvreader3:
        change = int(current_row[1])
        revenue2.append(change)

        current_row_revenue2 = int(current_row[1])
        
        if max_revenue_row2 == None:
            max_revenue_row2 = current_row

        if min_revenue_row2 == None:
            min_revenue_row2 = current_row

        current_max_revenue2 = int(max_revenue_row1[1])

        if current_max_revenue2 < current_row_revenue2:
            max_revenue_row2 = current_row 

        current_min_revenue2 = int(min_revenue_row2[1])

        if current_min_revenue2 > current_row_revenue2:
            min_revenue_row2 = current_row 

    
    if max_revenue_row1[1] < max_revenue_row2[1]:
        print("The maximum revenue was record on " + str(max_revenue_row1[0]) + " at " + str(max_revenue_row1[1]) + " dollars.")
    else:
        print("The maximum revenue was record on " + str(max_revenue_row2[0]) + " at " + str(max_revenue_row2[1]) + " dollars.")

    if min_revenue_row1[1] > min_revenue_row2[1]:
        print("The minimum revenue was record on " + str(min_revenue_row1[0]) + " at " + str(min_revenue_row1[1]) + " dollars.")
    else:
        print("The minimum revenue was record on " + str(min_revenue_row2[0]) + " at " + str(min_revenue_row2[1]) + " dollars.")

    avg_revenue2 = [x - revenue2[i - 1] for i, x in enumerate(revenue2)][1:]
            
        
    avg_revenue3 = sum(avg_revenue1 + avg_revenue2) / float(len(avg_revenue1 + avg_revenue2))
           

    total_revenue = (total + total2)
    total_months = (row_count1 + row_count2)

    print ("Total revenue is " + str(total_revenue))
    print ("Total number of months " + str(total_months))
    print ("Average change in revenue per month is " + str(avg_revenue3))

text_file = open('output.txt', 'w')
text_file.write("Total revenue is " + str(total_revenue))
text_file.write("Total number of months " + str(total_months))
text_file.write("Average change in revenue per month is " + str(avg_revenue3))
if max_revenue_row1[1] < max_revenue_row2[1]:
    text_file.write("The maximum revenue was record on " + str(max_revenue_row1[0]) + " at " + str(max_revenue_row1[1]) + " dollars.")
else:
    text_file.write("The maximum revenue was record on " + str(max_revenue_row2[0]) + " at " + str(max_revenue_row2[1]) + " dollars.")

if min_revenue_row1[1] > min_revenue_row2[1]:
    text_file.write("The minimum revenue was record on " + str(min_revenue_row1[0]) + " at " + str(min_revenue_row1[1]) + " dollars.")
else:
    text_file.write("The minimum revenue was record on " + str(min_revenue_row2[0]) + " at " + str(min_revenue_row2[1]) + " dollars.")

text_file.close()