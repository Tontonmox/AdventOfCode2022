f = open("Advent2022-19.txt","r")

daList = []
id = 0
decrypt = 811589153
for line in f:
    daList.append((id,int(line.strip())*decrypt))
    id += 1

newList = [i for i in daList]

#Parcours de la liste d'origine pour garder l'ordre de traitement
for i in range(10):
    for x in daList:
        #Recherche de l'index actuel de l'élément
        pos = newList.index(x)
        #Je calcule la future position de l'élément
        newpos = (pos+x[1])%(len(daList)-1)
        newList.remove(x)
        #Si la nouvelle pos est 0 : insert à la fin à la plce
        if newpos == 0:
            newList.insert(len(daList),x)
        else:
            newList.insert(newpos,x)

pos0 = -1
#Recherche du 0
for x in newList:
    if x[1] == 0:
        pos0 = newList.index(x)
        break

res_1 = newList[(pos0+1000)%len(newList)][1] + newList[(pos0+2000)%len(newList)][1] + newList[(pos0+3000)%len(newList)][1]
print(res_1)

