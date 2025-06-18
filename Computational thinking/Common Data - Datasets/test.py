import csv

data = []
with open('scores.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        data.append(row)
#print(data)
data.pop(0)
count = 0
for row in data:
    c = 0
    if int(row[5]) < 80:
        c = c + 1

    if int(row[6]) < 80:
        c = c + 1

    if int(row[7]) < 80:
        c = c + 1

    if c == 2:
        count += 1
print(count)
