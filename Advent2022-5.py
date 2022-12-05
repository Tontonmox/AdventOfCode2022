f = open("Advent2022-5.txt","r").read().split("\n\n")

input_1 = f[0].split("\n")[:-1]
input_2 = f[1].split("\n")[:-1]

stock = [[] for i in range(9)]

#Chargement des caisses
for line in input_1:
    for i in range (9):
        if line[4*i+1] != " ":
            stock[i].append(line[4*i+1])


#Traitement des déplacements
for line in input_2:   
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
