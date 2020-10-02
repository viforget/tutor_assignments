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


t_day = [[],[]]
i = 0
for r in tab[0]:
    t_day[0].append(tab[0][i] + ' ' + tab[1][i])
    t_day[1].append(0)
    i += 1


i = 0
for line in tab:
    if i >= 1:
        j = 0
        for case in line:
            if j != 0 and case == 'Oui':
                t_day[1][j] += 1
            j += 1
    i += 1


t_tutor = [[],[]]
i = 0
for r in tab:
    t_tutor[0].append(tab[i][0])
    t_tutor[1].append(0)
    i += 1
print t_tutor

file.close()
