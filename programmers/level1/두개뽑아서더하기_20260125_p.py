# https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
adds = []
def solution(numbers):
    for n in range(0,len(numbers)):
        for x in range(1,len(numbers)-1):
            b =n+x
            if b > len(numbers)-1: #인덱스 넘어가는 경우
                b = b - len(numbers)
            a = numbers[n]+numbers[b]
            if a not in adds:
                adds.append(a)
           
        
        adds.sort()
        set(adds)
    return  adds
