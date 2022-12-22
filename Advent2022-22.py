#Récupération de la tranche de map horizontale ou verticale dans laquelle on va se déplacer
#On enlève les espaces de début/fin
def sliceMap(posx,posy,rot,map):
    if rot == 'H':
        return map[posy].strip()
    else:
        return ''.join([map[i][posx] for i in range(len(map))]).strip()

def applyDepl(pos,depl,dir,slice):
    #print("Deplacement depuis "+str(pos)+" de "+str(depl)+" Direction "+str(dir)+ "dans {"+slice+"}")
    for i in range(depl):
        #On s'arrete a un mur
        if slice[(pos+dir)%len(slice)] == '#':
            break
        else:
            pos = (pos+dir)%len(slice)
    
    return pos

#4 directions en indiquant le sens (H / V Horizontal / Vertical) et la direction en indice (+1 / -1)
#Droite / Bas / Gauche / Haut
directions = [('H',1),('V',1),('H',-1),('V',-1)]

input = open("Advent2022-22.txt","r").read().split('\n')

map = input[:-2]
instructions = input[-1].replace('R',';R;').replace('L',';L;').split(';')

#Pour offset des positions x/y
#Nombre de blancs en début de chaque ligne
whiteH = []
for line in map:
    num = 0
    for c in line:
        if c == ' ':
            num += 1
        else:
            break
    whiteH.append(num)
#Nombre de blancs en début de chaque colonne
whiteV = []
for i in range(len(map[0])):
    col = ''.join([map[x][i] for x in range(len(map))])
    num = 0
    for c in col:
        if c == ' ':
            num += 1
        else:
            break
    whiteV.append(num)

#Position de départ + tourné vers la droite
posx = map[0].index('.')
posy = 0
curDir = 0

#Traitement des instructions
for ins in instructions:
    #Rotation
    if ins == 'R':
        curDir = (curDir + 1) % 4
    elif ins == 'L':
        curDir = (curDir - 1) % 4
    #Deplacement de x
    else:
        depl = int(ins)
        rot,dir = directions[curDir]
        slice = sliceMap(posx,posy,rot,map)
        if rot == 'H':
            offset = whiteH[posy]
            #print("X avant : "+str(posx))
            posx = applyDepl(posx-offset,depl,dir,slice) + offset
            #print("X avant : "+str(posx))
        else:
            offset = whiteV[posx]
            #print("Y avant : "+str(posy))
            posy = applyDepl(posy-offset,depl,dir,slice) + offset
            #print("Y apres : "+str(posy))
        
#print(str(posx)+':'+str(posy)+':'+str(curDir))

res_1 = 1000 * (posy+1) + 4 * (posx+1) + curDir
print(res_1)