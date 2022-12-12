import string

#Une destination valide doit être : 
#   - Dans la Map
#   - a une hauteur comprise entre 0 et hauteur actuelle + 1
#   - Pas déjà visitée (aucun intérêt à boucler)
#   - On ne peut pas sortir par la gauche ou la droite de la map
def valid_dest(start,end,visited,max,map,side):
    #Coordonnées en dehors de la map = impossible
    if end < 0 or end > max:
        return False
    #Hauteur > hauteur actuelle + 1 = impossible
    if map[start]+1 < map[end]:
        return False
    #Destination déjà visitée = impossible
    if end in visited:
        return False
    #Si le départ est sur le bord gauche : impossible de faire -1
    #Idem pour le passage de droite à gauche
    if start%(side) == 0 and end == start-1:
        return False
    if end%(side) == 0 and end == start+1:
        return False
    return True
    
inputs = ''.join(open("Advent2022-12.txt","r").read().split('\n'))

start = end = 0
side = len(open("Advent2022-12.txt","r").read().split('\n')[0].strip())

b_squares = []

#Initialisation d'une liste des hauteurs (1 case = 1 valeur, 0 pour start et end)
map = []
for i,c in enumerate(inputs):
    if c in string.ascii_lowercase:
        map.append(string.ascii_lowercase.find(c))
    if c == 'S':
        map.append(0)
        start = i
    if c == 'E':
        map.append(25)
        end = i
    if c == 'b':
        b_squares.append(i)

max = len(map) - 1

possible_start = []
#Pour chaque case b existante, on recherche une case a adjacente, comme étant un point de départ potentiel pour l'exercice 2, cela permet de limiter les départs à tester
#Note : je triche en ne testant que les -1 / +1 vu le positionnement des b dans l'input (ligne verticale)
for i in b_squares:
    if map[i-1] == 0:
        possible_start.append(i-1)
    elif map[i+1] == 0:
        possible_start.append(i+1)
    
#Initialisation du parcours : on est sur le point de départ
#start_path = [start]
#all_paths = [start_path]

shortest = 99999
for s in possible_start:
    start_path = [s]
    all_paths = [start_path]
    res_1 = 0
    visited = [start]

    #Boucle de pathfinding
    while True:
        new_paths = []
        #Parcours des path
        for p in all_paths:
            #Pour chaque path enregistré, on crée un nouveau path pour chaque destination valide qu'il peut atteindre
            # 4 directions possibles : Haut (-side) Bas(+side) Gauche (-1) Droite (1)
            for dir in [-side,+side,-1,1]:
                if valid_dest(p[-1],p[-1]+dir,visited,max,map,side):
                    new_path = p + [p[-1]+dir]
                    new_paths.append(new_path)

                    #On ajoute le noeud atteint à ceux qui sont visités : inutile de l'atteindre une nouvelle fois avec un parcours de même taille ou plus
                    visited.append(p[-1]+dir)

                    #On vérifie si on a trouvé un path gagnant, si oui on enregistre sa taille
                    if p[-1]+dir == end:
                        res_1 = len(new_path)-1
                    
                #On stoppe tout si on a trouvé un path gagnant
                if res_1 > 0:break
            
            #On stoppe tout si on a trouvé un path gagnant
            if res_1 > 0:break
        
        #On stoppe tout si on a trouvé un path gagnant
        if res_1 > 0:break
        #Sinon on reboucle sur les nouveaux chemins
        all_paths = new_paths

    print(res_1)
    if res_1 < shortest:
        shortest = res_1
    #print(res_1)

print(shortest)
