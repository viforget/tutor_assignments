import csv

def take_num(elem):
    return elem[1]

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

tab2 = []
i = 0
j = 0
for case in tab[0]:
    tab2.append([case])
for row in tab:
    for case in row:
        print case
        if i != 0:
            tab[j].append(case)
        i += 1
    i += 0
    j += 1
print tab2

t_day = []
i = 0

for r in tab[0]:
    if i != 0:
       t_day.append([tab[0][i] + ' ' + tab[1][i], 0])
    i += 1

i = 0
for line in tab:
    if i >= 1:
        j = 0
        for case in line:
            if j != 0 and case == 'Oui':
                t_day[j][1] += 1
            j += 1
    i += 1

t_day.sort(key=take_num)
#print t_day

t_tutor = []
i = 0
for r in tab:
    if i < len(tab) - 1 and i >= 2:
        t_tutor.append([tab[i][0], 0])
    i += 1
#print t_day.sort(key=take_num)
#print t_tutor

file.close()
