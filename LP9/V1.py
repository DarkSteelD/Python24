import csv
with open('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP9\\15 - 1.csv', newline='',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
