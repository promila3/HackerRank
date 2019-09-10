#https://www.hackerrank.com/challenges/nested-list/problem?h_r=profile
if __name__ == '__main__':
    listS = []
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scoreList.append(score)
        listS.append([name,score])
        #sorted(listS, key=lambda student: student[1])

    #scoreList.sort()
    scoreList = [ float(x) for x in set(scoreList)]
    scoreList.sort()
    #print(scoreList)
    #print(scoreList)
    secondMax = scoreList[1]
    #print(secondMax)
    secondList = [x[0] for x in listS if x[1] == secondMax]
    secondList.sort()
    for a in secondList:
        print(a)
