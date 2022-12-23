def checkDir(elve):
    x,y = elve
    result = []
    for d in directions:
        free = True
        #On fait les 3 vérifications
        for offset in to_check[d]:
            oX,oY = offset
            if (x+oX,y+oY) in elves:
                free = False
        if free:
            result.append(0)
        else:
            result.append(1)
        
    return result

def planMove(elf,eDir):
    oX,oY = to_check[directions[eDir.index(0)]][1]
    x,y = elf
    return(x+oX, y+oY)
    
    

#Récupération de la position initiale des elfes
f = open("Advent2022-23.txt","r")

elves = []
y = 0
for line in f:
    x = 0
    for c in line:
        if c == '#':
            elves.append((x,y))
        x += 1
    y += 1

directions = ['N','S','W','E']
#Coordonnées à checker pour chaque directions
to_check = {}
to_check['N'] = [(-1,-1),(0,-1),(1,-1)]
to_check['S'] = [(-1,1),(0,1),(1,1)]
to_check['W'] = [(-1,-1),(-1,0),(-1,1)]
to_check['E'] = [(1,-1),(1,0),(1,1)]

#Boucle de 10 tours
#for _ in range(10):
turns = 0
while True:
    #Check les 4 triplets de case dans les 4 directions
    elvesDir = []
    [elvesDir.append(checkDir(e)) for e in elves]

    #Enregistrer les propositions de mouvements
    elvesMoves = []
    forbiddenMoves = set()
    for i,eDir in enumerate(elvesDir):
        #Si personne en vue on ne fait rien --> position actuelle sinon on récupère la proposition s'il reste une direction valide ()
        if sum(eDir) == 0 or sum(eDir) == 4:
            elvesMoves.append(elves[i])
        else:
            move = planMove(elves[i],eDir)
            #On vérifie si ce mouvement est déjà prévu : si oui c'est un doublon il va dans les mouvements interdits
            if move in elvesMoves:
                forbiddenMoves.add(move)
            elvesMoves.append(move)

    #Supprimer les propositions de mouvements qui regroupent plusieurs elfes
    for i,move in enumerate(elvesMoves):
        if move in forbiddenMoves:
            elvesMoves[i] = elves[i]


    #Compter combien d'elfes bougent
    moveCount = 0
    for i,move in enumerate(elvesMoves):
        if move != elves[i]:
            moveCount += 1

    #Appliquer les mouvements
    elves = elvesMoves

    #Faire tourner l'ordre des directions
    directions.append(directions.pop(0))

    turns += 1
    print("Fin du tour ",turns," avec ",moveCount," mouvements")
    if moveCount == 0:
        break

#Solution de la partie 1, recherche du plus petit rectangle
xMin = yMin = 999
xMax = yMax = -999
for e in elves:
    x,y = e
    xMin = min(xMin,x)
    xMax = max(xMax,x)
    yMin = min(yMin,y)
    yMax = max(yMax,y)

print(xMin,xMax,yMin,yMax)
print(abs((xMax - xMin + 1)*(yMax - yMin + 1)) - len(elves))
