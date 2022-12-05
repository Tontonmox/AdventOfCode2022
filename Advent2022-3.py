import string

#Initialisation du dictionnaire alphabet
priorities={}
num=1
for c in string.ascii_lowercase:
    priorities[c]=num
    num+=1
for c in string.ascii_uppercase:
    priorities[c]=num
    num+=1



f = open("Advent2022-3.txt","r")
score_1 = 0
score_2 = 0
group_pos = 0
bags = ["","",""]
for line in f:
    #Traitement exercice 1
    line = line.strip()
    half = int(len(line)/2)
    part1 = line[0:half]
    part2 = line[half:2*half]
    
    for c in part1:
        if c in part2 : 
           score_1 += priorities[c]
           break
    
    #Traitement exercice 2
    bags[group_pos] = line
    if group_pos == 2:
        for c in bags[0]:
            if c in bags[1] and c in bags[2]:
                score_2 += priorities[c]
                break
        group_pos=0
    else:
        group_pos += 1
    
print(score_1)
print(score_2)