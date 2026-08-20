import csv

fieldnames = ['id', 'name', 'price', 'amount']
data = [
    {'id':'1','name':'apple','price':'5000', 'amount':'5'},
    {'id':'2','name':'pencil','price': '500', 'amount' :'42'},
    {'id':'3','name':'pineapple','price': '8000', 'amount':'5'},
    {'id':'4','name':'pen','price': '1500', 'amount':'10'}
]

f = open('data2.csv', 'w')
writer = csv.DictWriter(f, fieldnames=fieldnames)

writer.writeheader()
writer.writerows(data)

# for row in data:
#     writer.writerow(row)

f.close()