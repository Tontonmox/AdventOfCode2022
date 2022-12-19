def doTurn(newState,new_robots):
    #Récolte des ressources puis création des robots
    for i in range(4):
        #Ajout aux ressources selon le nombre de robots
        newState[i] += newState[i+4]
        #Ajout aux robots selonl e nombre de nouveaux robots
        newState[i+4] += new_robots[i]
    
    return newState

def simulateAll(gameState,blueprint):
    futures = []
    ore2ore,ore2cla,ore2obs,cla2obs,ore2geo,obs2geo = [int(i) for i in blueprint[1:]]
    resources = gameState[:3]
    robots = gameState[4:]

    bestRobot = 0
    for i,n in enumerate(robots):
        if n > 0:
            bestRobot = i+1

    robotPossible = 0
    #Test construction d'un robot ore
    if resources[0] >= ore2ore:
        robotPossible += 1
        newState = list(gameState)
        newState[0] -= ore2ore
        new_robots = [1,0,0,0]
        newState = doTurn(newState,new_robots)
        futures.append(tuple(newState))
    #Test construction d'un robot clay
    if resources[0] >= ore2cla:
        robotPossible += 1
        newState = list(gameState)
        newState[0] -= ore2cla
        new_robots = [0,1,0,0]
        newState = doTurn(newState,new_robots)
        futures.append(tuple(newState))
    #Test construction d'un robot obsidian
    if resources[0] >= ore2obs and resources[1] >= cla2obs:
        robotPossible += 1
        newState = list(gameState)
        newState[0] -= ore2obs
        newState[1] -= cla2obs
        new_robots = [0,0,1,0]
        newState = doTurn(newState,new_robots)
        futures.append(tuple(newState))
    #Test construction d'un robot geode
    if resources[0] >= ore2geo and resources[2] >= obs2geo:
        robotPossible += 1
        newState = list(gameState)
        newState[0] -= ore2geo
        newState[2] -= obs2geo
        new_robots = [0,0,0,1]
        newState = doTurn(newState,new_robots)
        futures.append(tuple(newState))
    #Creation du futur ou on ne construit rien, sauf si tous les robots du rang max atteint étaient possibles
    if robotPossible <= bestRobot:
        newState = list(gameState)
        new_robots = [0,0,0,0]
        newState = doTurn(newState,new_robots)
        futures.append(tuple(newState))

    return futures

f = open("Advent2022-19.txt","r")

blueprints = []
for line in f:
    blueprints.append(line.strip().replace('Blueprint ','').replace(': Each ore robot costs ',';').replace(' ore. Each clay robot costs ',';').replace(' ore. Each obsidian robot costs ',';').replace(' ore and ',';').replace(' clay. Each geode robot costs ',';').replace(' ore and ',';').replace(' obsidian.','').split(';'))

res_1 = 0
res_2 = 1
for b in blueprints:
    print(b)
    #Création du gameState de base pour le blueprint en cours
    gameStates = {(0,0,0,0,1,0,0,0)}

    #Boucle de 24 tours pour exo 1, 32 tours pour exo 2
    for i in range(32):
        newStates = set()
        for g in gameStates:
            for s in simulateAll(g,b):
                newStates.add(s)

        #Après le tour 18 on filtre sur les 200 000 meilleurs résultats par nombre de geodes
        if i <= 18:
            gameStates = newStates
        if i > 18:
            gameStates = sorted(newStates,key=lambda a:a[3],reverse=True)[:200000]

        #print("Apres tour "+str(i)+" nombre d'etats : "+str(len(gameStates)))
    #print("Pour blueprint "+str(b[0])+" geodes max = "+str(gameStates[0][3]))
    res_1 += int(b[0])*int(gameStates[0][3])
    res_2 *= int(gameStates[0][3])
    
print(res_1)
print(res_2)