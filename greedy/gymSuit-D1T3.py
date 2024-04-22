def solution(n, lost, reserve):
    answer = 0
    
    # 정렬되어 있단 말 없음
    lost.sort()
    reserve.sort()
    
    # 공통되는 원소 제거 (여벌 가져온 놈도 도난 당할 수 있음)
    for r in reserve[:]: # copy list로 순회
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    
    for r in reserve:
        front = r-1
        back = r+1
        # 여벌이 있으면 앞 먼저 있다면 뒤로 빌려준다.
        if front in lost:
            lost.remove(front)
        elif back in lost:
            lost.remove(back)
            
    # 전체에서 옷 못 빌린 학생들 수만 빼면 답 
    answer = n - len(lost)
    
    return answer