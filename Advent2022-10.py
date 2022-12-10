f = open("Advent2022-10.txt","r")

#Initialisation des positions (0 = Head, 1-X = tails)
register = []
crt =  [[' ' for i in range(40)] for j in range (6)]

for line in f:
    param = line.strip().split()
    register.append(0)
    if param[0] == 'addx':
        register.append(int(param[1]))
register[0] += 1

res_1 = 0
for i in range(19,221,40):
    res_1 += sum(register[:i])*(i+1)

print(res_1)

for i,x in enumerate(register):
    print(str(i//40)+' '+str(i%40))
    #print(str(i)+':'+str(sum(register[:i])))
    center = sum(register[:i])
    pixels = [center-1,center,center+1]
    if i%40 in pixels:
        crt[i//40][i%40] = '#'


for line in crt:
    print(''.join(line))