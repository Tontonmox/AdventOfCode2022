f = open("Advent2022-8.txt","r").read().split('\n')

size = len(f[0])
map = [[] for i in range(size)]
visibility = [[] for i in range(size)]

#Transformation de l'input en liste 2D
for x,line in enumerate(f):
    for c in line:
        map[x].append(int(c))
        visibility[x].append(0)

#Parcours de la liste 2D dans les 4 sens et décompte des arbres les plus grands
for x in range(size):
    max_h = -1
    for y in range(size):
        if map[x][y] > max_h:
            max_h = map[x][y]
            visibility[x][y] = 1

    max_h = -1
    for y in reversed(range(size)):
        if map[x][y] > max_h:
            max_h = map[x][y]
            visibility[x][y] = 1

for y in range(size):
    max_h = -1
    for x in range(size):       
        if map[x][y] > max_h:
            max_h = map[x][y]
            visibility[x][y] = 1

    max_h = -1
    for x in reversed(range(size)):
        if map[x][y] > max_h:
            max_h = map[x][y]
            visibility[x][y] = 1

score_1 = 0
for line in visibility:
    score_1 += sum(line)

print(score_1)

max_view = 0
#EXERCICE 2
for y,line in enumerate(map):
    for x,tree in enumerate(line):
        #Traitement d'un arbre dans les 4 sens
        a=b=c=d=0
        for i in reversed(range(0,x)):
            a += 1
            if map[y][i] >= tree:break
        for i in range(x+1,size):
            b += 1
            if map[y][i] >= tree:break
        for i in reversed(range(0,y)):
            c += 1
            if map[i][x] >= tree:break
        for i in range(y+1,size):
            d += 1
            if map[i][x] >= tree:break

        max_view = max(a*b*c*d,max_view)

print(max_view)