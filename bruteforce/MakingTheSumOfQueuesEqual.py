from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    # 연산의 효율을 위해 deque으로
    que1, que2 = deque(queue1), deque(queue2)
    length = len(que1+que2) / 2
    
    sum1, sum2 = sum(que1), sum(que2)
    
    # 홀수인 경우 제외
    if sum1+sum2 % 2 == 1:
        return -1
    
    # 두 큐가 완벽히 switching 하는 시간
    while answer < (4 * length):
        # sum함수 사용 X
        if sum1 > sum2:
            sum1 = sum1 - que1[0]
            sum2 = sum2 + que1[0]
            que2.append(que1.popleft())
        elif sum1 < sum2:
            sum1 = sum1 + que2[0]
            sum2 = sum2 - que2[0]
            que1.append(que2.popleft())
        else:
            return answer
        answer = answer + 1
    
    return -1