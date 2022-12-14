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

#Partie 2 : Tri du fichier en utilisant la fonction de la partie 1
inputs_2 = [line for line in open("Advent2022-13.txt","r").read().split('\n') if line != '']
inputs_2.append('[[2]]')
inputs_2.append('[[6]]')
permutation = 999
#On fait des permutations 2 à 2 tant que la liste change (tri à bulles)
while permutation > 0:
    permutation = 0
    #Boucle de permutation 2 à 2
    for i in range(len(inputs_2)-1):
        if not validPair(inputs_2[i],inputs_2[i+1]):
            inputs_2 = inputs_2[:i]+[inputs_2[i+1]]+[inputs_2[i]]+inputs_2[i+2:]
            permutation += 1

res_2 = (inputs_2.index('[[2]]')+1)*(inputs_2.index('[[6]]')+1)
print(res_2)