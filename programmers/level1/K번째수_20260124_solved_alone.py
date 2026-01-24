def solution(array, commands):
    answer = []
    for y in range(1,len(commands)+1):
        cmd = commands[y-1]
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]

    #리스트 추출(슬라이싱)
    
        array2 = array[i-1:j]
        array3 =array2.sort()
        x = array2[k-1]
        answer.append(x)

    
    return answer
