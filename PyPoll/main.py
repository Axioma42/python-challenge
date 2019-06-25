import os
import csv

csv_path= os.path.join("../pypoll", "election_data.csv")

#The total number of votes cast
def total_votes(dataset):
    result = 0
    for row in dataset:
        result += 1
    return result

#The total number of votes each candidate won
def candidate_votes(dataset):
    lst = [row[2] for row in dataset]
    result = {x:lst.count(x) for x in lst}
    return result

with open(csv_path, "r") as csvfile:
    reader = csv.reader(csv_path, delimiter = ",")
    next(reader, None)
    rows = [row for row in reader]
    total_number_votes = total_votes(rows)
    candidates_dict = candidate_votes(rows)
    sorted(candidates_dict.values())
    #The winner of the election
    winner_candidate = candidates_dict.keys()[-1]
    
    #The percentage of votes each candidate won
    for k, v in candidates_dict.items():
        candidates_dict[k] = [f'{100 * (v / total_number_votes)}%', v]
    
    output = (
    f"Election Results\n"
    f"Total Votes: ${total_number_votes}\n"
    f"{candidates_dict}\n"
    f"Winner: {winner_candidate}\n")

print(output)
