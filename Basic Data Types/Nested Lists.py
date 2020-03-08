#!/bin/python3
#problem can be resolved in many ways

if __name__ == '__main__':
    nestedList=list()
    scoreList=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nestedList.append([name,score])
        #scoreList used to calculcate the second min score,ie, first element in sorted list
        if score not in scoreList:
            scoreList.append(score)
    scoreList.sort()
    nestedList.sort()
    for item in nestedList:
        if scoreList[1]==item[1]:
            print(item[0])