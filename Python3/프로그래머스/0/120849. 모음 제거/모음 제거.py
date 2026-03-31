def solution(my_string):
    answer = ''
    vowels = "aeiou"
    
    answer = answer.join(c for c in my_string if c not in vowels)
    return answer