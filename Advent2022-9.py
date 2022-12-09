import math

f = open("Advent2022-9.txt","r")

#Initialisation des positions (0 = Head, 1-X = tails)
rope = [[0,0] for i in range(10)]
xh = yh = xt = yt = 0
visited_1 = set()
visited_9 = set()

for line in f:
    d,n = line.strip().split()

    for i in range(int(n)):
        #Deplacement de la tête (rope[0] dans la direction d)
        match d:
            case 'U':
                rope[0][1] += 1
            case 'D':
                rope[0][1] -= 1
            case 'L':
                rope[0][0] -= 1
            case 'R':
                rope[0][0] += 1

        #Pour chaque noeud après H
        for i in range(1,len(rope)):
            xt,yt = rope[i]
            xh,yh = rope[i-1]
            #Controle de la position de T par rapport à H :
            #Si l'écart en x ET en y est > 1 on rapproche de 1 sur x et y
            if abs(xh-xt) >1 and abs(yh-yt) >1:
                xt += math.copysign(1,xh-xt)
                yt += math.copysign(1,yh-yt)
            else:
                #Si l'écart entre xh et xt est > 1 on rapproche xt de xh et on met yt sur yh (mouvement diagonal)
                if abs(xh-xt) >1:
                    xt += math.copysign(1,xh-xt)
                    yt = yh

                #Si l'écart entre yh et yt est > 1 on rapproche yt de yh et on met xt sur xh (mouvement diagonal)
                if abs(yh-yt) >1:
                    yt += math.copysign(1,yh-yt)
                    xt = xh
            
            #On enregistre la nouvelle position de T dans la corde
            rope[i] = [int(xt),int(yt)]

        #Si la nouvelle position du noeud 1 ne fait pas partie de la liste des positions visitees, on l'ajoute
        pos = str(rope[1][0])+':'+str(rope[1][1])
        visited_1.add(pos)

        #Idem pour noeud 9
        pos = str(rope[9][0])+':'+str(rope[9][1])
        visited_9.add(pos)

#Resultat de l'exercice : nombre de valeurs distinctes dans visited
print(len(visited_1))
print(len(visited_9))