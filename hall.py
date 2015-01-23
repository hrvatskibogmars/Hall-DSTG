ukupno = 101010101010


def ZauzetoPoStupcu(matrica, red, stupac):
	for i in range(red+1, len(matrica)):
		if matrica[i][stupac] == 'D':
			return True
	for i in range(red-1, -1, -1):
		if matrica[i][stupac] == 'D':
			return True
	return False


rjesenje = []
def dodjela(matrica, pomocna, red):
	global ukupno
	global rjesenje
	global iteracija
	if red == len(pomocna):
		suma = 0
		koordinate = []
		for i in range(len(pomocna)):
			for j in range(len(pomocna)):
				if pomocna[i][j] == 'D':
					koordinate.append([i,j])
					suma += matrica[i][j]
		if suma < ukupno:
			ukupno = suma
			rjesenje = koordinate				  
	elif red < len(pomocna):
		for j in range(len(pomocna)):
			pamti = pomocna[red][j]
			if not ZauzetoPoStupcu(pomocna, red, j):
				pomocna[red][j] = 'D'
				dodjela(matrica, pomocna, red+1)			
			pomocna[red][j] = pamti
			
	

matrica = [
    [458, 341, 712, 256, 452, 132, 456, 862, 995, 204, 630],
    [258, 452, 312, 722, 450, 620, 482, 236, 302, 474, 447],
    [786, 119, 278, 542, 912, 301, 452, 401, 603, 256, 187],
    [312, 205, 450, 778, 215, 654, 102, 448, 596, 123, 315],
    [206, 289, 712, 199, 665, 147, 258, 213, 330, 901, 526],
    [368, 812, 620, 265, 458, 186, 304, 812, 774, 563, 912],
    [912, 663, 213, 726, 226, 413, 123, 354, 712, 204, 469],
    [465, 601, 130, 345, 344, 558, 812, 586, 862, 300, 505],
    [128, 345, 753, 445, 910, 736, 332, 255, 255, 312, 450],
    [170, 335, 166, 266, 554, 338, 200, 130, 200, 109, 112],
    [832, 245, 455, 300, 882, 620, 475, 258, 304, 889, 861]
]

pomocna = [
    [458, 341, 712, 256, 452, 132, 456, 862, 995, 204, 630],
    [258, 452, 312, 722, 450, 620, 482, 236, 302, 474, 447],
    [786, 119, 278, 542, 912, 301, 452, 401, 603, 256, 187],
    [312, 205, 450, 778, 215, 654, 102, 448, 596, 123, 315],
    [206, 289, 712, 199, 665, 147, 258, 213, 330, 901, 526],
    [368, 812, 620, 265, 458, 186, 304, 812, 774, 563, 912],
    [912, 663, 213, 726, 226, 413, 123, 354, 712, 204, 469],
    [465, 601, 130, 345, 344, 558, 812, 586, 862, 300, 505],
    [128, 345, 753, 445, 910, 736, 332, 255, 255, 312, 450],
    [170, 335, 166, 266, 554, 338, 200, 130, 200, 109, 112],
    [832, 245, 455, 300, 882, 620, 475, 258, 304, 889, 861]
]


dodjela(matrica, pomocna, 0)
print "Koordinate rezultata"
print "--------------------"
for i in rjesenje:
	print "(" + str(i[0]) + "," + str(i[1]) + ")"

print "\n\n"
print "Ukupno prijedenih metara"
print "------------------------"
suma = 0
for i in rjesenje:
	x = i[0]
	y = i[1]
	suma += matrica[x][y]
print suma
