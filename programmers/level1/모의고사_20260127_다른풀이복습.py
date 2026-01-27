def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0,0,0]
    from itertools import cycle
    scores = [sum(a==p for a,p in zip (answers,cycle(p1))),
    sum(a==p for a,p in zip (answers,cycle(p2))),
    sum(a==p for a,p in zip (answers,cycle(p3)))]
    max_score = max(scores)
    
    return [i+1 for i,x in enumerate(scores) if max_score == scores[i] ]
# 인덱스, 값 (순서 주의)
