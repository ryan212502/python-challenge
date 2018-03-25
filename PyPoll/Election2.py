import os
import csv

csvpath = os.path.join("Election1.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    total_votes1 = 0
    all_votes1 = {}
    for row in csvreader:
        vote = row["Canadiate"]
        if vote in all_votes1:
            all_votes1[vote] += 1
        else:
            all_votes1[vote] = 1

        total_votes1 += 1

csvpath = os.path.join("Election2.csv")

with open(csvpath, newline="") as csvfile:
    csvreader2 = csv.DictReader(csvfile)

    total_votes2 = 0
    all_votes2 = {}
    for row in csvreader2:
        vote2 = row["Candidate"]
        if vote2 in all_votes2:
            all_votes2[vote2] += 1
        else:
            all_votes2[vote2] = 1

        total_votes2 += 1

    all_votes2.update(all_votes1)
 
    total_votes3 = total_votes1 + total_votes2

    for name in all_votes2:
        print(name + " " + str(all_votes2[name]) + " " + str(round((all_votes2[name] / (total_votes1 + total_votes2)) * 100)) + "%")

    winner3 = None
    winner_votes3 = 0
    for name in all_votes2:
        if all_votes2[name] > winner_votes3:
            winner3 = name   
            winner_votes3 = all_votes2[name]

    print("Winner:", winner3)

    print(str((total_votes1) + (total_votes2)) + " Total Votes")


#text_file = open('output.txt', 'w')
#for name in all_votes2:
    #text_file.write(name) + " " + str(all_votes2[name]) + " " + str(round((all_votes2[name] / (total_votes1 + total_votes2)) * 100)) + "%")
#text_file.write("Winner:", winner3)
#text_file.write(str((total_votes1) + (total_votes2)) + " Total Votes")
#text_file.close()

    