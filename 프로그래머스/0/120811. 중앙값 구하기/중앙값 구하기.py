def solution(array):
    array.sort()
    i = (len(array)-1)//2
    answer = array[i]
    return answer