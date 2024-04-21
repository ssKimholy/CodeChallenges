def solution(k, dungeons):
    answer = -1
    bo = [False] * len(dungeons) # dfs를 위한 방문 배열
    
    def dfs(k, dep):
        nonlocal answer # 상급 변수 사용
        answer = max(answer, dep)

        # dfs 알고리즘
        for i, dungeon in enumerate(dungeons):
            if not bo[i] and k >= dungeon[0]:
                bo[i] = True
                dfs(k-dungeon[1], dep+1)
                bo[i] = False
                
    dfs(k, 0)
    
    return answer