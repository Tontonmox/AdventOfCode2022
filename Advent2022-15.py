f = open("Advent2022-15.txt","r")

def dist(xs,ys,xb,yb):
    return abs(xs-xb) + abs(ys-yb)

def test_part2(segments,cury):
    xmax = 0
    for s in segments:
        if s[0] > xmax:
            print("Trou entre "+str(xmax)+" et "+str(s[0])+" sur ligne "+str(cury))
            print("Resultat 2 :"+str((xmax+1)*4000000+cury))
            break
        if s[0] <= xmax and s[1] > xmax:
            xmax = s[1]

#Création d'un set vide qui stockera les valeurs de x couvertes par la range d'un beacon connu sur la ligne visée
covered = set()
target = 2000000
beacons = set()
inputs = []

for line in f:
    #Récupération des coordonnées des sensors et beacons
    line = line.strip().replace('Sensor at x=','').replace(' y=','').replace(': closest beacon is at x=',',').replace(' y=','')
    xs,ys,xb,yb = [int(i) for i in line.split(',')]
    inputs.append((xs,ys,xb,yb))

    #Ajout du beacon dans les beacons
    beacons.add(str(xb)+':'+str(yb))

    #Calcul de la distance manhattan entre sensor et beacon
    d = dist(xs,ys,xb,yb)

    #Calcul de la distance entre la ligne cible et la ligne du sensor
    dy = abs(ys-target)

    #print(str(d) + '/' + str(dy))
    if d > dy:
        for x in range(d-dy+1):
            #print(x)
            covered.add(xs+x)
            covered.add(xs-x)

#Parcours du set des lignes couvertes pour rechercher celles dont y = target
res_1 = len(covered)
for b in beacons:
    if b.split(':')[1] == str(target):
        res_1 -= 1

print(res_1)

#Partie 2
for target in range(4000000+1):
    segments = []

    for i in inputs:
        xs,ys,xb,yb = i

        #Calcul de la distance manhattan entre sensor et beacon
        d = dist(xs,ys,xb,yb)

        #Calcul de la distance entre la ligne cible et la ligne du sensor
        dy = abs(ys-target)

        #Determination du min/max de x sur target
        xmin = min(max(xs-(d-dy),0),4000000)
        xmax = max(min(xs+(d-dy),4000000),0)
        segments.append((xmin,xmax))
                
    segments.sort()
    #print(segments)
    test_part2(segments,target)
        




