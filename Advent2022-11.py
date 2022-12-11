class Monkey:
    items = []
    operation = ""
    divisor = 0
    dest_true = 0
    dest_false = 0
    inspect_count = 0

f = open("Advent2022-11.txt","r")

monkey_inputs = f.read().split('\n\n')
monkeys = []
#Reducer sera le produit de l'ensemble des diviseurs des singes : le résultat sera donc un nombre qui pourra être retiré
#de la valeur des items tout en restant neutre pour le test sur les divisions
reducer = 1

#Initialisation des singes
for i,m in enumerate(monkey_inputs):
    lines = m.split('\n')
    new_monkey = Monkey()
    new_monkey.items =[int(x.strip()) for x in lines[1].replace(':',',').split(',')[1:]]
    new_monkey.operation = lines[2].split('=')[1][4:]
    new_monkey.divisor = int(lines[3].split('by')[1].strip())
    new_monkey.dest_true = int(lines[4][-1])
    new_monkey.dest_false = int(lines[5][-1])
    monkeys.append(new_monkey)

    reducer *= new_monkey.divisor

#Nombre de tours de l'exo 1
#for turn in range(20):
#Nombre de tours de l'exo 2
for turn in range(10000):
    for m in monkeys:
        #Parcours des items
        for i in m.items:
            #Application de l'operation puis division par 3 arrondie à l'inférieur
            #Formule de l'exo 1
            #i = eval(str(i)+m.operation.replace('old',str(i)))//3
            #Formule de l'exo 2
            i = eval(str(i)+m.operation.replace('old',str(i)))%reducer
            #Test du divisor et envoi de l'item selon résultat
            if i % m.divisor == 0:
                monkeys[m.dest_true].items.append(i)
            else:
                monkeys[m.dest_false].items.append(i)
            
            #Incrémentation du compteur d'objets inspectés
            m.inspect_count += 1

        #Vidage de la liste des items
        m.items = []

res = []
for m in monkeys:
    res.append(m.inspect_count)
res.sort()
print(res[-1]*res[-2])