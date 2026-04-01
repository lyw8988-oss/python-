def solution(array):
    answer = []
    for i in array:
        if i == max(array): answer.append(i)
    for i in range(len(array)):
        if array[i] == max(array): answer.append(i)
    return answer