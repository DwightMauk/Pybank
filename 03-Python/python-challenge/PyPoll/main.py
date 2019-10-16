import os
import csv

path = os.getcwd()
#'C:\\Users\\Dwight\\source\\python\\python-challenge\\PyPoll'

csvpath=os.path.join("..","..","python-challenge","PyPoll","pypoll","election_data.csv")


total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        
        total_votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

         
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]


print("Election Results")
print("_____________________")
print("Total Votes:"  + str(total_votes))
print("_____________________")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("_______________________")
print("Winner: " + winner)
print("_______________________")


output_file = os.path.join("..","..","python-challenge","PyPoll","election_data.text")


with open(output_file, 'w') as file:
    file.write("Election Results \n")
    file.write("____________________\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("____________________ \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    file.write("____________________ \n")
    file.write("Winner: " + winner + "\n")
    file.write("_____________________ \n")
