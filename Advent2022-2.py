def rps_score(op,my):
    #Win
    if (my == "X" and op == "C") or (my == "Y" and op == "A") or (my == "Z" and op == "B") : return 6
    #Draw
    if (my == "X" and op == "A") or (my == "Y" and op == "B") or (my == "Z" and op == "C") : return 3
    #Loss
    return 0

#Retourne la valeur en point du choix qui sera fait pour obtenir le résultat voulu
#Valeur = position dans la liste de mes choix + 1
def rps_choice(op,res):
    opp_choices=['A','B','C']

    #Draw
    if res == "Y":
        return opp_choices.index(op) + 1
    #Win
    if res == "Z":
        return (opp_choices.index(op) +1)%3 +1
    #Loss
    if res == "X":
        return (opp_choices.index(op) -1)%3 +1


f = open("Advent2022-2.txt","r")

score_1 = 0
score_2 = 0
choice_points = {"X":1,"Y":2,"Z":3}
result_points = {"X":0,"Y":3,"Z":6}

for line in f:
    op,my = line.strip().split(" ")
    score_1 += choice_points[my]
    score_1 += rps_score(op,my)
    score_2 += rps_choice(op,my)
    score_2 += result_points[my]

print(score_1)
print(score_2)
