def solution(sizes):
    answer = 0
    
    # 각 리스트 속 리스트를 내림차순 정렬
    sizes = [sorted(size, reverse=True) for size in sizes]
    
    # 1행에서는 가로의 최대값, 2행에서는 세로의 최대값을 구함
    width = max(size[0] for size in sizes)
    height = max(size[1] for size in sizes)
    
    # 산술 기하 평균에 의해 해당 곱이 가장 작은 수가 됨.
    answer = width * height
    
    return answer