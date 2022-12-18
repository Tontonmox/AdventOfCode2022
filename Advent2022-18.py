def neighbours(cube):
    res = []
    x,y,z= [int(i) for i in cube.split(',')]
    res.append(str(x+1)+','+str(y)+','+str(z))
    res.append(str(x-1)+','+str(y)+','+str(z))
    res.append(str(x)+','+str(y+1)+','+str(z))
    res.append(str(x)+','+str(y-1)+','+str(z))
    res.append(str(x)+','+str(y)+','+str(z+1))
    res.append(str(x)+','+str(y)+','+str(z-1))
    return res

def neighbours_min_max(cube):
    min = -1
    max = 20
    res = []
    x,y,z= [int(i) for i in cube.split(',')]
    if x+1 <= max:
        res.append(str(x+1)+','+str(y)+','+str(z))
    if x-1 >= min:
        res.append(str(x-1)+','+str(y)+','+str(z))
    if y+1 <= max:
        res.append(str(x)+','+str(y+1)+','+str(z))
    if y-1 >= min:
        res.append(str(x)+','+str(y-1)+','+str(z))
    if z+1 <= max:
        res.append(str(x)+','+str(y)+','+str(z+1))
    if z-1 >= min:
        res.append(str(x)+','+str(y)+','+str(z-1))
    return res

#BFS pour flood depuis une case à l'extérieur
#On parcourt toutes les cases accessibles qui ne sont pas un cube depuis une case située à l'extérieur 
#On se limite aux coordonnées -1,-1,-1 jusqu'à 20,20,20
def flood(start,cubes):
    water = set()
    water.add(start)
    test = neighbours_min_max(start)
    while len(test) > 0:
        next_test = set()
        for cube in test:
            if cube in cubes:
                pass
            elif cube in water:
                pass
            else:
                water.add(cube)
                [next_test.add(x) for x in neighbours_min_max(cube)]
        test = next_test
    
    return(water)

f = open("Advent2022-18.txt","r")

cubes = []
air = []
for line in f:
    cubes.append(line.strip())
    #Recherche des x/y/z min
    x,y,z = cubes[-1].split(',')

res_1 = 0
#Recherche des voisins de chaque cube
for c in cubes:
    for n in neighbours(c):
        if n not in cubes: 
            air.append(n)
            res_1 += 1

print(res_1)

start = '-1,-1,-1'
water = flood(start,cubes)
res_2 = res_1
for a in air:
    if a not in water:
        res_2 -= 1

print(res_2)