import csv
import numpy

def last_elem(elem):
    return elem[-1]

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

key = len(tab)
tab.append([])
for case in tab[0]:
    tab[key].append(int(0))

temp = numpy.transpose(tab)
tab2 = numpy.array(temp)
key = len(tab2[1]) - 1

tab3 = []
for row in tab2:
    tab3.append([])
    for case in row:
        tab3[len(tab3) - 1].append(case)

i = 0
for row in tab3:
    tab3[i][key] = 0
    i += 1

i = 0
key = len(tab3[1]) - 1
for line in tab3:
    if i >= 1:
        j = 0
        for case in line:
            if j != 0 and case == 'Oui':
                tab3[i][key] += 1
            j += 1
    i += 1


t_tutor = []
i = 0
for r in tab:
    if i < len(tab) - 1:
        t_tutor.append([tab[i][0], 0])
    i += 1
tab3.sort(key=last_elem)

t_tutor[0][1] = -1
i = 0
buf1 = 0
buf2 = 0
for row in tab3:
	j = 0
	for case in row:
		if j < key and case == 'Oui':
			if  t_tutor[j][1] >  t_tutor[buf1][1]:
				if t_tutor[j][1] > t_tutor[buf2][1]:
					buf1 = buf2
					buf2 = j
				else:
					buf1 = j
		j += 1
	if buf1 != 0:
		tab3[i][buf1] = 'OK'
		t_tutor[buf1][1] += 1
		print buf1 
	if buf2 != 0:
		tab3[i][buf2] = 'OK' 
		t_tutor[buf2][1] += 1 
		print buf2 
	i += 1

print tab3
print t_tutor

file.close()
