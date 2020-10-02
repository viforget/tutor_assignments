import csv
import numpy

def take_num(elem):
    return elem[1]

fname = "tutor.csv"
file = open(fname, "rb")

tab = []
i = 0;
reader = csv.reader(file)
for row in reader:
    tab.append([])
    for case in row:
        tab[i].append(case)
    i += 1

tab2 = numpy.transpose(tab)
print (tab)
print ("---------------------------")
print (tab2)

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
