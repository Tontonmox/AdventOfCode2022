from collections import Counter

def result(chain,size):
    result = 0
    #Boucle sur les caractères pour trouver les paquets de 4 uniques
    for i in range(len(chain)):
        quad = Counter(chain[i:i+size])
        valid = True

        for c in chain[i:i+size]:
            if quad[c] > 1:
                valid = False
                break
        
        if valid:
            result = i+size
            break
    
    return result

f = open("Advent2022-6.txt","r").read()

print(result(f,4))
print(result(f,14))

    