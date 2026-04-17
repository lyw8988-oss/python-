def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)//code): 
        answer += cipher[code*(i+1)-1]
    return answer