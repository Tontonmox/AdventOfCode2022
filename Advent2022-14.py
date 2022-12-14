f = open("Advent2022-14.txt","r")

obstacles = set()
max_depth = 0

for line in f:
    coords = line.strip().split(' -> ')

    #Tracage des lignes
    for i in range(len(coords)-1):
        x1,y1 = [int(x) for x in coords[i].split(',')]
        x2,y2 = [int(x) for x in coords[i+1].split(',')]
        #Ligne horizontale
        if x1 == x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                obstacles.add(str(x1)+','+str(y))
                max_depth=max(max_depth,y)

        #Ligne verticale
        if y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                obstacles.add(str(x)+','+str(y1))
                max_depth=max(max_depth,y1)

start = '500,0'
sand_count = 0
fall = False
#Boucle de génération du sable
while not fall:
    #Génération du sable au départ
    x,y = [int(i) for i in start.split(',')]
    while True:
        #Boucle de déplacement en suivant les règles (bas, bas-gauche,bas-droite)
        if str(x)+','+str(y+1) not in obstacles:
            y += 1
        elif str(x-1)+','+str(y+1) not in obstacles:
            y += 1
            x -= 1
        elif str(x+1)+','+str(y+1) not in obstacles:
            y += 1
            x += 1
        else:
            #Si immobile, incrémentation du compteur de sable, ajout du grain aux obstacles et passage au grain suivant
            obstacles.add(str(x)+','+str(y))
            sand_count += 1
            break
        if y > max_depth:
            fall = True
            break
        #Si profondeur > max_depth --> fall à true et arrêt de la boucle

print(sand_count)
        
    