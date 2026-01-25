def solution(answers):
    forgiver1=[1,2,3,4,5]
    forgiver2=[2, 1, 2, 3, 2, 4, 2, 5]
    forgiver3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    n=1
    while len(forgiver1) <  len(answers):
        forgiver1 *= n 
        forgiver1=forgiver1[0:len(answers)]
        n += 1
        
    
    while len(forgiver2) <  len(answers):
        forgiver2 *= n 
        forgiver2=forgiver2[0:len(answers)]
        n += 1
    while len(forgiver3) <  len(answers):
        forgiver3 *= n 
        forgiver3=forgiver3[0:len(answers)]
        n += 1
    
    forgiver1_score = 0
    forgiver2_score = 0
    forgiver3_score = 0
    for i in range(0,len(answers)):
            
        if answers[i] == forgiver1[i]:
            forgiver1_score += 1

        if answers[i] == forgiver2[i]:
            forgiver2_score += 1

        if answers[i] == forgiver3[i]:
            forgiver3_score += 1
                   
                    
    
    max_score = int(max([forgiver1_score,forgiver2_score,forgiver3_score]))
    answer = []
    if max_score == forgiver1_score:
        answer.append(1)
    if max_score == forgiver2_score:
        answer.append(2)
    if max_score == forgiver3_score:
        answer.append(3)
    
    return answer
