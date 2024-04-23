import math

def solution(n, k):
    answer = 0
    
    # k진수로 바꾸고 "0"을 기준으로 나누면 조건 만족
    candidates = convertToKNumber(n, k).split("0")
    
    # 공백 포함 시 제거
    while '' in candidates:
        candidates.remove('')
    
    for candidate in candidates:
        # 소수 반펼
        if isPrime(int(candidate)):
            answer += 1
    
    return answer

# k진수 변환
def convertToKNumber(n, k):
    if n < k:
        return str(n)
    
    return convertToKNumber(n//k, k) + str(n%k)

# 소수 판별 알고리즘
def isPrime(n):
    if n == 0 or n == 1:
        return False
    
    # 종료 조건 주의
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    