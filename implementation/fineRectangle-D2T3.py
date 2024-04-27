import math

def solution(w,h):
    area = w * h
    w, h = max(w, h), min(w, h)
    g = gcd(w, h) # 최대 공약수
    # 규칙 찾기... 1을 빼는 이유는 w, h이 중복으로 거치는 경우 때문에
    exclusive = ((w/g) + (h/g) - 1) * g
    return area - exclusive
    
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)