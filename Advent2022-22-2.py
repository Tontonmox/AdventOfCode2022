def move(sq,x,y,dir,l):
    for _ in range(l):
        nSq, nX, nY, nDir, nValue = nextPos(sq,x,y,dir)
        #print("Prochaine pos : ",nSq, nX, nY, nValue)
        if nValue == '#':
            break
        else:
            sq,x,y,dir = nSq, nX, nY, nDir
    
    return sq,x,y,dir

def nextPos(sq,x,y,dir):
    #On incrémente x / y
    nX = x + directions[dir][0]
    nY = y + directions[dir][1]

    #Si toutes les valeurs correctes, on retourne les positions + la valeur de la case
    if 0 <= nX < 50 and 0 <= nY < 50:
        return sq, nX, nY, dir, squares[sq][nY][nX]
    else:
        #Sortie par la gauche
        if nX < 0:
            outDir = 'L'
        #Sortie par la droite
        elif nX > 49:
            outDir = 'R'
        #Sortie par le haut
        elif nY < 0:
            outDir = 'U'
        #Sortie par le bas
        elif nY > 49:
            outDir = 'D'
        
        t = transitions[str(sq)+outDir]
        nSq = t[0]
        nDir = (dir + t[1]) % 4
        nX,nY = change(x,y,t[2],t[3])
        nValue = squares[nSq][nY][nX]
        return nSq, nX, nY, nDir, nValue

def change(x,y,cX,cY):
    nX , nY = x , y
    match cX:
        case 0 | 49:
            nX = cX
        case 's':
            nX = y
        case 'i':
            nX = 49 - x
        #L'autre valeur possible est =, on ne fait rien
    match cY:
        case 0 | 49:
            nY = cY
        case 's':
            nY = x
        case 'i':
            nY = 49 - y
        #L'autre valeur possible est =, on ne fait rien
    return nX,nY

#Transitions : destination (de 1 à 6) et rotation de la direction de déplacement (1 droite, 2 flip -1 gauche 0 tout droit)
transitions = {}
transitions['1R'] = (2,0,0,'=')
transitions['1D'] = (3,0,'=',0)
transitions['1L'] = (5,2,0,'i')
transitions['1U'] = (6,1,'s','s')
transitions['2R'] = (4,2,49,'i')
transitions['2D'] = (3,1,'s','s')
transitions['2L'] = (1,0,49,'=')
transitions['2U'] = (6,0,'=',49)
transitions['3R'] = (2,-1,'s','s')
transitions['3D'] = (4,0,'=',0)
transitions['3L'] = (5,-1,'s','s')
transitions['3U'] = (1,0,'=',49)
transitions['4R'] = (2,2,49,'i')
transitions['4D'] = (6,1,'s','s')
transitions['4L'] = (5,0,49,'=')
transitions['4U'] = (3,0,'=',49)
transitions['5R'] = (4,0,0,'=')
transitions['5D'] = (6,0,'=',0)
transitions['5L'] = (1,2,0,'i')
transitions['5U'] = (3,1,'s','s')
transitions['6R'] = (4,-1,'s','s')
transitions['6D'] = (2,0,'=',0)
transitions['6L'] = (1,-1,'s','s')
transitions['6U'] = (5,0,'=',49)

#Droite / Bas / Gauche / Haut, variations en x,y
directions = [(1,0),(0,1),(-1,0),(0,-1)]

input = open("Advent2022-22.txt","r").read().split('\n')

map = input[:-2]
instructions = input[-1].replace('R',';R;').replace('L',';L;').split(';')

squares = {}
squares[1] =[line[50:100] for line in map[0:50]]
squares[2] =[line[100:] for line in map[0:50]]
squares[3] =[line[50:100] for line in map[50:100]]
squares[4] =[line[50:100] for line in map[100:150]]
squares[5] =[line[0:50] for line in map[100:150]]
squares[6] =[line[0:50] for line in map[150:]]

print("Square 5 : ",squares[5])

offset = {}
offset[1]=(51,1)
offset[2]=(101,1)
offset[3]=(51,51)
offset[4]=(51,101)
offset[5]=(1,101)
offset[6]=(1,151)

#Position de départ : Carré 1, position 0,0, direction vers la droite
sq = 1
x = 0
y = 0
dir = 0

#Traitement des instructions
for ins in instructions:
#while False:
    #Rotation
    if ins == 'R':
        dir = (dir + 1) % 4
    elif ins == 'L':
        dir = (dir - 1) % 4
    #Deplacement de x
    else:
        l = int(ins)
        sq,x,y,dir = move(sq,x,y,dir,l)

print(1000*(y+offset[sq][1])+4*(x+offset[sq][0])+dir)