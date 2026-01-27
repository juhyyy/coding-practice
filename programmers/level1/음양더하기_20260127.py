def solution(absolutes, signs):
    signed = []
    for i in range(0,len(signs)):
        if signs[i] == 0:
            
            signed.append(-absolutes[i])
        else :
           
            signed.append(absolutes[i])
            
    return sum(signed)

#    return sum(-a if not s else a for a, s in zip(absolutes, signs))
#     return sum(
        # -absolutes[i] if not signs[i] else absolutes[i]
        # for i in range(len(signs))
    )
