f = open("Advent2022-1.txt","r")

max,cur = 0,0
last = ""
calories=[]

for line in f:
    #Fin d'une somme
    if line.strip() == "" :
        calories.append(cur)
        if cur > max : max = cur
        cur = 0
    else:
        cur += int(line.strip())

print(max)
calories.sort(reverse=True)
print(sum(calories[0:3]))