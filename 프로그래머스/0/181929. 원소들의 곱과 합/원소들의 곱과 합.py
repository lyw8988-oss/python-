def solution(num_list):
    answer = 0
    sums=0
    multiples=1
    for i in num_list:
        sums += i
        multiples *=i
    if multiples < sums*sums : answer =1
    return answer