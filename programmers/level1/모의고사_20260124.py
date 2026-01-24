def solution(answers):
    
    #패턴 찾아주기 
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    patterns = [p1, p2, p3]

    # 각 점수
    scores = [0, 0, 0]
    
    ######################
    from itertools import cycle

    #zip 같은 인덱스 끼리 리스트로 묶어주는 함수 
    # cycle 
    scores = [
        sum(a == p for a, p in zip(answers, cycle(p1))),
        sum(a == p for a, p in zip(answers, cycle(p2))),
        sum(a == p for a, p in zip(answers, cycle(p3))),  ]

    max_score = max(scores)
    return [i + 1 for i, s in enumerate(scores) if s == max_score]
    
#     ### 다른 풀이 
#     for i, a in enumerate(answers):
#         for idx, p in enumerate(patterns):
#             if a == p[i % len(p)]:
#                 scores[idx] += 1

#     max_score = max(scores)
    # enumerate    👉 리스트(같은 반복 가능한 것)를 돌리면서 인덱스와 값을 튜플 형태로 주는 함수 
#     return [i + 1 for i, s in enumerate(scores) if s == max_score]
     # +1 을 왜 함? 인덱스는 0부터 시작하니까. 몇번째인지 답하려면 +1 을 해야함.
