import csv
import numpy
import sys

def hour_param(elem):
    return elem[1]

def date_param(elem):
    return elem[0]

def last_elem(elem):
    return elem[-1]

def find_si(row, t_tutor):
	i = 0
	buf = 0
	for case in row:
		if case == "Si" and t_tutor[i][1] < t_tutor[buf][1]:
			buf = i
		i += 1
	return (buf)
			

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

t_tutor[0][1] = 99999999
i = 0
buf1 = 0
buf2 = 0
for row in tab3:
	j = 0
	if i != 0:
		for case in row:
			if j < key and case == 'Oui':
				if  t_tutor[j][1] <  t_tutor[buf1][1]:
					if t_tutor[j][1] < t_tutor[buf2][1]:
						buf1 = buf2
						buf2 = j
					elif t_tutor[j][1] > t_tutor[buf2][1]:
						buf1 = j
			j += 1
		if buf1 != 0:
			tab3[i][buf1] = 'OK'
			t_tutor[buf1][1] += 1
		else :
			buf1 = find_si(row, t_tutor)
			if buf1 != 0:
				tab3[i][buf1] = 'OK' 
				t_tutor[buf1][1] += 1
		
		if buf2 != 0:
			tab3[i][buf2] = 'OK' 
			t_tutor[buf2][1] += 1
		else : 
			buf2 = find_si(row, t_tutor)
			if buf2 != 0:
				tab3[i][buf2] = 'OK' 
				t_tutor[buf2][1] += 1
	i += 1

tab3.sort(key=hour_param)
tab3.sort(key=date_param)

i = 0
for row in tab3:
	for case in row:
		if isinstance(case, int):
			sys.stdout.write(str(case))
		else:
			sys.stdout.write("'")
			sys.stdout.write(str(case))
			sys.stdout.write("'")
		if i != len(row) - 1:
			sys.stdout.write(',')
		i += 1
	sys.stdout.write('\n')
	i = 0 
file.close()
