class Room:
    def __init__(self,flow_rate,next):
        self.flow_rate = flow_rate
        self.next = next
        self.dist_to = {}

f = open("Advent2022-16.txt","r")

#Recherche récursive BFS pour distance la plus courte entre 2 noeuds
def calcul_dist(next,goal):
    dist = 1
    while True:
        next_depth = set()
        for x in next:
            if x == goal:
                return dist
            for y in rooms[x].next:
                next_depth.add(y)
        next = next_depth
        dist += 1
        
#Traitement des inputs et constitution d'un dict des classes
rooms = {}
targets = []
for line in f:
    id, flow_rate,next = line.strip().replace('Valve' ,'').replace(' has flow rate=',';').replace('tunnels','tunnel').replace('leads','lead').replace('valves','valve').replace(' tunnel lead to valve ','').split(';')
    id = id.strip()
    flow_rate = int(flow_rate)
    next = next.replace(' ','').split(',')
    rooms[id] = Room(flow_rate,next)

    #Si le flow_rate est > 0 alors on doit viser l'ouverture de cette valve
    if flow_rate > 0:
        targets.append(id)

#Pour chaque Room intéressante (flow > 0) + celle de départ, découverte de la distance vers les autres Room intéressantes
for start in targets + ['AA']:
    for goal in targets:
        if start != goal:
            rooms[start].dist_to[goal] = calcul_dist(rooms[start].next,goal)

#Part 1 : Recherche du meilleur score possible en 30 tours au départ de A
def part_1():
    #Variable globale pour la sauvegarde du meilleur score trouvé tout parcours confondu
    best = 0
    #Fonction récursive
    def next_moves(opened, score, current_room, turns_left):
        nonlocal best
        if score > best:
            best = score

        if turns_left <= 0:
            return

        if current_room not in opened:
            #Si on est dans une salle ou la valve est fermée (et vaut des points) on l'ouvre
            next_moves(opened.union([current_room]), score + rooms[current_room].flow_rate * turns_left, current_room, turns_left - 1)
        else:
            #Sinon, on génère tous les chemins possibles vers une autre salle qui n'a pas encore été ouverte
            for k in rooms[current_room].dist_to.keys():
                if k not in opened:
                    next_moves(opened, score, k, turns_left - rooms[current_room].dist_to[k])

    next_moves(set(['AA']), 0, 'AA', 29)
    print(best)

part_1()

#Part 2 : Recherche du meilleur score possible en 26 tours au départ de A
#Mais en faisant évoluer joueur et éléphant en parallèle
def part_2():
    #Variable globale pour la sauvegarde du meilleur score trouvé tout parcours confondu
    best_2 = 0
    #Fonction récursive
    def next_moves_2(opened, score, current_room, current_room_el, turns_left, turns_left_el, elephant,log):
        nonlocal best_2
        if score > best_2:
            best_2 = score
            print(log +" "+str(best_2))

        if turns_left <= 0 and turns_left_el <= 0:
                return
        if turns_left <= 0 and turns_left_el > 0 and not elephant:
            next_moves_2(opened, score, current_room, current_room_el, turns_left, turns_left_el, True,log)
        if turns_left > 0 and turns_left_el <=  0 and elephant:
            next_moves_2(opened, score, current_room, current_room_el, turns_left, turns_left_el, False,log)

        cur = current_room
        if elephant:
            cur = current_room_el

        if cur not in opened:
            #Si on est dans une salle ou la valve est fermée (et vaut des points) on l'ouvre
            if not elephant:
                #Evolution du score
                score += rooms[current_room].flow_rate * turns_left 
                #log += " / Joueur ouvre "+str(current_room)+ " avec "+str(turns_left)+" tours = "+str(rooms[current_room].flow_rate * turns_left)+" points"
                #Décompte d'un tour
                turns_left -= 1
            else:
                #Evolution du score
                score += rooms[current_room_el].flow_rate * turns_left_el
                #log += " / El ouvre "+str(current_room_el)+ " avec "+str(turns_left_el)+" tours = "+str(rooms[current_room_el].flow_rate * turns_left_el)+" points"
                #Décompte d'un tour
                turns_left_el -= 1
            if turns_left >= turns_left_el:
                elephant = False
            else:
                elephant = True
            next_moves_2(opened.union([cur]), score, current_room, current_room_el, turns_left, turns_left_el, elephant,log)
        else:
            #Sinon, on génère tous les chemins possibles vers une autre salle qui n'a pas encore été ouverte
            if not elephant : 
                for k in rooms[current_room].dist_to.keys():
                    if k not in opened:
                        next_moves_2(opened, score, k,current_room_el, turns_left - rooms[current_room].dist_to[k],turns_left_el, elephant,log)
            else:
                for k in rooms[current_room_el].dist_to.keys():
                    if k not in opened:
                        next_moves_2(opened, score, current_room,k, turns_left ,turns_left_el - rooms[current_room_el].dist_to[k], elephant,log)

    next_moves_2(set(['AA']), 0, 'AA', 'AA', 25, 25, False,'')
    print(best_2)

part_2()