f = open("Advent2022-5.txt","r")

stock = [[] for i in range(9)]

#Lecture des input
for line in f:
    #Ignorer la ligne vide
    if len(line.strip()) == 0 : continue

    #Ignorer la ligne avec les indices
    if line[1] == '1' : continue

    #Chargement des caisses
    if line[0] != 'm':
        for i in range (int(len(line)/4)):
            if line[4*i+1] != " ":
                stock[i].append(line[4*i+1])

    #Traitement des déplacements
    if line[0] == 'm':
        decoup = line.split(" ")
        num,fro,to = int(decoup[1]), int(decoup[3])-1, int(decoup[5])-1

        #Récupération des caisses à déplacer (en les retournant)
        move = stock[fro][:num]
        #move.reverse()
        del stock[fro][:num]
        stock[to][:0] = move

reponse_1 = ''
for c in stock:
    if len(c) == 0:
        reponse_1 += ' '
    else:
        reponse_1 += c[0]

print(reponse_1)
