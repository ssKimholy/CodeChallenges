from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 코스요리 후보들
    candidates = {}
    
    for c in course:
        temp = []
        for order in orders:
            # 문자열들을 c개로 조합낸다.
            comb_list = combinations(sorted(order), c)
            temp.extend(comb_list)
            
        # counter를 사용해 각 원소가 몇 번 중복(등장) 했는지 본다
        counter = Counter(temp)
        
        if counter:
            max_count = max(counter.values())
            # 2번 이상 선택
            if max_count >= 2:
                # ''.join은 튜플 원소들을 쭉 이어서 하나의 문자열로 만들 때 사용, 제일 많이 선정된 하나 혹은                  여러 개 선택
                answer.extend([''.join(k) for k, v in counter.items() if v == max_count])
    
    answer.sort()
    
    return answer