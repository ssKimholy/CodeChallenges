def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1): # right+1 로 설정해야 right까지 포함
        # 규칙찾기가 중요! 예시를 보며 하나씩 써내려가 보자
        quotient = (i // n) + 1
        remainder = (i % n) + 1
        answer.append(max(quotient, remainder))
    
    return answer