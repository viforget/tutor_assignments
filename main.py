import csv

fname = "tutor.csv"
file = open(fname, "rb")

tab = [[]]
i = 0;
reader = csv.reader(file)
for row in reader:
    for case in row:
        tab[i].append(case)
    tab.append([])
    i += 1
print tab
file.close()
