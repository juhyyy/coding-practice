answer =[]
def solution(array, commands):
    for x in range(0,len(commands)):
        command = commands[x]
        i= command[0]
        j= command[1]
        k= command[2]
        
        array_2 = sorted(array[i-1:j])
        answer.append(array_2[k-1])
    
    return answer
