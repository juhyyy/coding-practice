from collections import Counter
def solution(participant, completion):
    # 부분 정답
    # incompletion = list(set(participant) - set(completion) )
    # answer = incompletion[0]
    # 참가자에 동명이인 있을 때 한명으로 처리됨
    
    incompletion = Counter(participant) - Counter(completion)

    # Counter는 key로 접근

    return next(iter(incompletion))
