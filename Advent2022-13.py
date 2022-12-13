inputs = open("Advent2022-13.txt","r").read().split('\n\n')

def parseList(a):
    lvl = 1
    res = ''
    for c in a[1:-1]:
        if c == '[':
            lvl += 1
        if c == ']':
            lvl -= 1
        if c == ',' and lvl == 1:
            res += ';'
        else:
            res += c
    return res


def validPair(a,b):
    if validList(a,b) == -1:
        return False
    return True

def compareElem(a,b):
    #print("Compare elem "+a+":"+b)
    #Si 2 listes, on les compare :
    if a[0] == '[' and b[0] == '[':
        return validList(a,b)
    #Si a est une liste et b entier, ou l'inverse, on transforme l'entier isolé en liste et on compare
    if a[0] == '[' and b[0] != '[':
        strList = '['+str(b)+']'
        return validList(a,strList)
    if a[0] != '[' and b[0] == '[':
        strList = '['+str(a)+']'
        return validList(strList,b)
    #Si 2 entiers
    if a[0] != '[' and b[0] != '[':
        if int(a) < int(b) : return 1
        if int(a) > int(b) : return -1
        return 0

def validList(a,b):
    #Parser chaquer liste et remplacer les virgules de "niveau 1" par des |
    #print("Valid list "+str(a)+":"+str(b))
    a = parseList(a).split(';')
    b = parseList(b).split(';')

    #Test listes vides :
    if a[0] == '' and b[0] != '':
        return 1
    if a[0] != '' and b[0] == '':
        return -1
    if a[0] == '' and b[0] == '':
        return 0

    #Parcours de la liste a
    for i in range(len(a)):
        #S'il n'y a plus d'éléments dans b --> Return False
        if i >= len(b): return -1

        #On a 2 éléments,on les compare, on retourne le résulat si la comparaison donne un résultat VRAI ou FAUX (si 0 ils sont identiques on continue)
        if compareElem(a[i],b[i]) != 0: return compareElem(a[i],b[i])


    #On a fini a --> s'il y a encore des éléments dans b, Return False
    if len(a) < len(b) : return 1

    #Sinon listes identiques
    return 0

i = 1
res_1 = 0
#Boucle de comparaison des paires
for pair in inputs:
    a,b = pair.split('\n')
    #print(a)
    #print(b)
    #print(validPair(a,b))
    if validPair(a,b):
        res_1 += i
    i += 1

print(res_1)