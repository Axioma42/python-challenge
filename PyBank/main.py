import os
import csv
from statistics import mean 

csv_path= os.path.join("../pybank", "budget_data.csv")

def total_months(dataset):
    result = 0
    for row in dataset:
        result += 1
    return result

def total(dataset):
    result = 0
    for row in dataset:
        result += int(row[1])
    return result

def average_change(dataset):
    return mean(dataset)

def greatest_increase(dataset):
    result = ""
    maximum = 0
    index = None 
    for row in dataset:
        maximum = max(int(row[1]))
        index = dataset.index(maximum)
    result = str(dataset.pop(index))
    return result

def greatest_decrease(dataset):
    result = ""
    minimum = 0
    index = None 
    for row in dataset:
        minimum = min(int(row[1]))
        index = dataset.index(minimum)
    result = str(dataset.pop(index))
    return result

with open(csv_path, "r") as csvfile:
    reader = csv.reader(csv_path, delimiter = ",")
    next(reader, None)
    rows = [row for row in reader]
    output_total_months = total_months(rows)
    output_total = total(rows)
    output_average_change = average_change(rows)
    output_greatest_increase = greatest_increase(rows)
    output_greatest_decrease = greatest_decrease(rows)
    
    output = (
    f"Total Months: {output_total_months}\n"
    f"Total : {output_total}\n"
    f"Average Change: ${output_average_change}\n"
    f"Greatest increase in Profits: {output_greatest_increase}\n"
    f"Greatest decrease in Profits: {output_greatest_decrease}\n")
    
    print(output)
    
