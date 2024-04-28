import heapq

def solution(scoville, K):
    answer = 0
    
    # 힙을 사용해 우선순위 큐 구현
    heapq.heapify(scoville)
    
    # 최소 원소가 2개여야 한다. top이 K보다 크거나 같은 경우 break
    while len(scoville) > 1 and scoville[0] < K:    
        first_least_spicy = heapq.heappop(scoville)
        second_least_spicy = heapq.heappop(scoville)
        mixed_spiciness = first_least_spicy + 2 * second_least_spicy
        heapq.heappush(scoville, mixed_spiciness)
        answer += 1
        
    # top이 K보다 작은데 원소가 하나인 경우 -1
    if scoville[0] < K:
        return -1
    
    return answer