def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit()==True: answer+=[int(i)]
    answer.sort()
    return answer