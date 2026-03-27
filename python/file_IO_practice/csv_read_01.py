import csv

f = open('output.csv', 'r', encoding ='utf-8', newline='')
reader = list(csv.reader(f))
print(reader)
for row in reader:
    print(row)

f.close()