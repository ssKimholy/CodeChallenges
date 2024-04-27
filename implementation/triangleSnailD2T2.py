def solution(n):
    answer = []
    x, y = -1, 0 # 삼각형 꼭대기를 위해 x는 -1로 초기화
    snail = [[0] * i for i in range(1, n+1)] # 삼각형 모양으로 미리 세팅
    num = 1
        
    for i in range(0, n):
        remainder = i % 3 # 방향은 총 세 개 (순서대로 하, 우, 상)
        for _ in range(i, n): # n - i 번 반복해서 빈칸채우기
            if remainder == 0: # 아래 방향
                x += 1
            elif remainder == 1: # 오른쪽 방향
                y += 1
            else: # 위쪽 방향
                x -= 1
                y -= 1
            snail[x][y] = num
            num += 1
    
    for s in snail:
        answer.extend(s)
    
    return answer
