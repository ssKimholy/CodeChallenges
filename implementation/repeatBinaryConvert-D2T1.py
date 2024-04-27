def solution(s):
    answer = []
    zero_count = 0 # 제거된 0 개수
    transform_count = 0 # 반복 횟수
    current_str = s
    
    while len(current_str) > 1:
        one_count = current_str.count('1')
        zero_count += len(current_str) - one_count # 0 또는 1인 점을 이용
        current_str = binaryNumber(one_count)
        transform_count += 1
    
    answer.extend([transform_count, zero_count])
    return answer

# 이진수 변환 알고리즘
def binaryNumber(num):
    if num == 0:
        return ""
    
    if num == 1:
        return "1"
    
    return binaryNumber(num//2) + str((num % 2))
