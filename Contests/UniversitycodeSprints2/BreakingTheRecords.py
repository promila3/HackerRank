'''
Maria plays  game

of college basketball in a season. Because she wants to go pro, she tracks her points scored per game sequentially in an array defined as . After each game , she checks to see if score  breaks her record for most or least points scored so far during that season.

Given Maria's array of  for a season of  games, find and print the number of times she breaks her record for most and least points scored during the season.

Note: Assume her records for most and least points at the start of the season are the number of points scored during the first game of the season.

Input Format

The first line contains an integer denoting  (the number of games). 
The second line contains  space-separated integers describing the respective values of .

Constraints

Output Format

Print two space-seperated integers describing the respective numbers of times her best (highest) score increased and her worst (lowest) score decreased.

Maria plays  games of college basketball in a season. Because she wants to go pro, she tracks her points scored per game sequentially in an array defined as . After each game , she checks to see if score  breaks her record for most or least points scored so far during that season.

Given Maria's array of  for a season of  games, find and print the number of times she breaks her record for most and least points scored during the season.

Note: Assume her records for most and least points at the start of the season are the number of points scored during the first game of the season.

Input Format

The first line contains an integer denoting  (the number of games). 
The second line contains  space-separated integers describing the respective values of .

Constraints

Output Format

Print two space-seperated integers describing the respective numbers of times her best (highest) score increased and her worst (lowest) score decreased.
*/
'''
#!/bin/python

import sys
def getMaxBreaks(scores,n):
    result = 0
    maxScore = scores[0]
    for i in range(1,n):
        if scores[i] > maxScore :
            result +=1
            maxScore = scores[i]
    return result

def getMinBreaks(scores,n):
    result = 0
    minScore = scores[0]
    for i in range(1,n):
        if scores[i] < minScore :
            result +=1
            minScore = scores[i]
    return result
        


n = int(raw_input().strip())
score = map(int, raw_input().strip().split(' '))
minscore,maxscore =getMinBreaks(score,n),getMaxBreaks(score,n)
print maxscore, minscore
# your code goes here
