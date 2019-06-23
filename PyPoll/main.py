import os
import csv
from statistics import mean 

pro_los = []
total_months = None
pro_los = None
total_months = None
dates = []
total = None
average = None
maximum = None
minimum = None
index_max = None
index_min = None
max_month = None
min_month = None

csv_path= os.path.join("/Users/demiurgo/Documents/bc_homeworks/3_py_ch_assignment/pybank/budget_data.csv")

with open(csv_path, newline="") as csvfile:
    reader = csv.reader(csv_path, delimiter=',')
    next(reader)

rows = [row for row in reader]

for row in reader:
    pro_los = int(row[1])
    total_months = total_months + 1
    dates = row[0]
    def Average(pro_los): 
        return mean(pro_los)
    total = sum(pro_los)
    average = Average(pro_los)
    maximum = max(pro_los)
    minimum = min(pro_los)
    index_max = reader.index(maximum)
    index_min = reader.index(minimum)
    max_month = dates.pop(index_max)
    min_month = dates.pop(index_min)

output = (
    f"Total Months: {total_months}\n"
    f"Total : {total}\n"
    f"Average Change: ${average}\n"
    f"Greatest increase in Profits: {max_month} ${maximum}\n"
    f"Greatest decrease in Profits: {min_month} ${minimum}\n"
)

print(output)
