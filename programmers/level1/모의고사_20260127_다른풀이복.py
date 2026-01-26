from itertools import cycle
p1= [1, 2, 3, 4, 5]
p2= [2, 1, 2, 3, 2, 4, 2, 5]
p3= [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

scores = [0,0,0]
def solution(answers):
    
    scores = [ sum(a==p for a,p in zip(answers,cycle(p1))),
                  sum(a==p for a,p in zip(answers,cycle(p2))),
                      sum(a==p for a,p in zip(answers,cycle(p3))) ]
    
    
    max_score = max(scores)
    return [ x+1 for x, y in enumerate(scores) if y==max_score ]
