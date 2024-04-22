from collections import deque

# bfs 알고리즘
def bfs(start_node, graph, visit, n):
    num = 0
    deq = deque([start_node])
    visit[start_node] = True
    
    while deq:
        node = deq.popleft()
        num += 1
        for neighbor in graph[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                deq.append(neighbor)
    return num

def solution(n, wires):
    answer = n
    
    # 초기 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(len(wires)):
        a, b = wires[i]
        
        # 한 connection씩 끊어가며 관찰
        graph[a].remove(b)
        graph[b].remove(a)
        
        # bfs 방문 배열
        visit = [False] * (n + 1)
        
        m1 = bfs(1, graph, visit, n)
        m2 = n - m1  # 어짜피 전력망은 두 개이다
        answer = min(answer, abs(m2 - m1))
        
        # 다시 연결
        graph[a].append(b)
        graph[b].append(a)

    return answer
