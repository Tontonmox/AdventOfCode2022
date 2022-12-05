f = open("Advent2022-4.txt","r")

score_1 = score_2 = 0

for line in f:
    x1,y1,x2,y2 = [int(i) for i in line.strip().replace(',','-').split('-')]
    
    if (x1 <= x2 and y1 >= y2) or (x2 <= x1 and y2 >= y1):
        score_1 += 1

    if (x2 <= x1 <= y2) or (x2 <= y1 <= y2) or (x1 <= x2 <= y1) or (x1 <= y2 <= y1) :
        score_2 +=1
    
print(score_1)
print(score_2)
