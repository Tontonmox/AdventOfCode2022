def result(code):
    if code in numbers:
        return numbers[code]
    else:
        num1, op, num2 = operations[code]
        #On remplace num1 par sa valeur (chiffre si connu ou sinon on résoud l'opération)
        if num1 in numbers:
            num1 = numbers[num1]
        else:
            num1 = result(num1)
        #Idem pour num 2
        if num2 in numbers:
            num2 = numbers[num2]
        else:
            num2 = result(num2)
        #Une fois qu'on a les 2 on résoud l'opération
        return int(eval(str(num1)+op+str(num2)))

def result2(code):
    if code in numbers_2:
        return numbers_2[code]
    else:
        num1, op, num2 = operations[code]
        #On remplace num1 par sa valeur (chiffre si connu ou sinon on résoud l'opération)
        if num1 in numbers_2:
            num1 = numbers_2[num1]
        else:
            num1 = result2(num1)
        #Idem pour num 2
        if num2 in numbers_2:
            num2 = numbers_2[num2]
        else:
            num2 = result2(num2)
        #Une fois qu'on a les 2 on résoud l'opération si possible (pas de x)
        if isinstance(num1,int) and isinstance(num2,int):
            return int(eval(str(num1)+op+str(num2)))
        else:
            return '('+str(num1)+op+str(num2)+')'

f = open("Advent2022-21.txt","r")

numbers = {}
numbers_2 = {}
operations = {}

for line in f:
    parts = line.strip().split(' ')
    if len(parts) == 2:
        numbers[parts[0][0:4]] = int(parts[1])
        if parts[0][0:4] == 'humn':
            numbers_2[parts[0][0:4]] = 'x'
        else:
            numbers_2[parts[0][0:4]] = int(parts[1])
    else:
        operations[parts[0][0:4]] = parts[1:4]

#Partie 1
print(result('root'))

#Partie 2
print(result2('gvfh'))
print(result2('njlw'))
#Et ensuite passer les 2 parties dans un solver d'equations avec un = entre les deux (la flemme de le coder :D)