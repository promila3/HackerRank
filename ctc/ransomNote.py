def ransom_note(magazine, ransom):
    global m,n
    magazine1 = {}
    note1 = {}
    word =''
    for word in magazine:
        if word in magazine1 :
            magazine1[word] +=1
        else :
            magazine1[word] = 1
    for word in ransom:
        if word in note1 :
            note1[word] +=1
        else :
            note1[word] = 1
    success = True
    for word in note1 :
        if (magazine1[word] < note1[word]) :
            success = False
            break
    return success
m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
