f = open("Advent2022-7.txt","r")

dir_size = {}
cur_dir = []

for line in f:
    line = line.split()

    #Traitement des commandes
    if line[0] == "$":
        #On traite uniquement les cd (les ls nous servent à rien)
        if line[1] == "cd":
            #Cas du .. : retour arrière
            if line[2] == "..":
                cur_dir.pop()
            #Autres cas : 
            else:
                #Ajout dans la liste des répertoires courants et création de son dir siee
                if line[2] == '/':
                    path = '/'
                else:
                    path = cur_dir[-1] + '/' +line[2]
                cur_dir.append(path)
                dir_size[path] = 0
    #Traitement des résultats de ls
    else:
        #Comptage de la taille des fichiers (on ignore les répertoires)
        if line[0] != "dir":
            for d in cur_dir:
                dir_size[d] += int(line[0])

#Pour la recherche du plus petit répertoire à supprimer pour avoir une taille libre de 30000000 sur les 70000000
#La taille à supprimer est donc la taille de / moins 40000000
goal = dir_size['/'] - 40000000
min_supp = 70000000

#Comptage des répertoires de taille <= à 100000
res1 = 0

for d in dir_size:
    #Traitement question 1
    if dir_size[d] <= 100000:
        res1 += dir_size[d]

    #Traitement question 2
    if goal < dir_size[d] < min_supp:
        min_supp = dir_size[d]

print(res1)
print(min_supp)



