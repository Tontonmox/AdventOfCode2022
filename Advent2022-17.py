def pos_valid(new_rock,x,y,tower):
    #print("Test en "+str(x)+':'+str(y))
    #Test de la position de chaque bloc # par rapport aux blocs existants dans la tour
    for i in range(len(new_rock)):
        for j in range(len(new_rock[i])):
            #print("Test "+new_rock[i][j]+"/"+tower[y+j][x+i])
            if new_rock[i][j] == '#' and tower[y+i][x+j] == '#':
                return False
    #print("Test ok")
    return True

def log_cur_tower(new_rock,x,y,tower):
    cur_tower = [row[:] for row in tower]
    for i in range(len(new_rock)):
        for j in range(len(new_rock[i])):
            if new_rock[i][j] == '#':
                cur_tower[y+i][x+j] = new_rock[i][j]
    for i in range(10,-1,-1):
        print(''.join(cur_tower[i]))



f = open("Advent2022-17.txt","r")

jets = f.read().strip()

#Initialisation d'une tour vide (taille 40 000 AU PIF)
tower =[['.','.','.','.','.','.','.'] for i in range(75000)]

rocks = []
rocks.append(['####'])
rocks.append(['.#.','###','.#.'])
rocks.append(['###','..#','..#'])
rocks.append(['#','#','#','#'])
rocks.append(['##','##'])

#compteur de rochers
rock_count = 0
jet_pos = 0

y_var = [(0,0)]

#boucle d'apparition de x rochers
while rock_count < 132+1468:

    #Sélection du nouveau rocker
    new_rock = rocks[rock_count%5]

    #Position du coin bas à gauche du bloc qui spawne
    x = 2
    #Recherche de la hauteur d'apparition
    y = 0
    for i in range(len(tower)):
        if tower[i] == ['.','.','.','.','.','.','.']:
            y = i+3
            #print("Spawn en "+str(y))
            y_var.append((y,y-y_var[-1][0]))
            break

    #Boucle de déplacement du rocher
    while True:
        #1 - Application du jet
        jet = jets[jet_pos%len(jets)]
        jet_pos += 1
        if jet == '<':
            #Déplacement à gauche si possibl
            #print("Avant test vers la gauche")
            if x > 0 and pos_valid(new_rock,x-1,y,tower):
                #print('<')
                x -= 1
        else :
            #Déplacement à droite si possible
            #Test du mur
            #print("Avant test vers la droite")
            if x + len(new_rock[0]) -1 <= 5 and pos_valid(new_rock,x+1,y,tower):
                #print('>')
                x += 1
        
        #2 - Déplacement vers le bas
        #Impossible si on est au sol
        if y == 0:
            break
        #Impossible si l'on rencontre un obstacle
        if pos_valid(new_rock,x,y-1,tower):
            #print("down")
            y -= 1
        else :
            break
        #log_cur_tower(new_rock,x,y,tower)

    #Ajout du rocher à sa position finale
    #log_cur_tower(new_rock,x,y,tower)
    for i in range(len(new_rock)):
        for j in range(len(new_rock[i])):
            if new_rock[i][j] == '#':
                tower[y+i][x+j] = new_rock[i][j]

    #Incrémentation du compteur de rochers
    rock_count += 1

#Une fois les rochers tombés on affiche la hauteur totale de la tour
for i in range(len(tower)):
    if tower[i] == ['.','.','.','.','.','.','.']:
        print(i)
        break

#res = [y_var[i][1] for i in range(len(y_var))]
#print(res)