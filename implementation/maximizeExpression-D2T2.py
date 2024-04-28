import itertools

def operation(l, r, op):
    tmp = ''
    if op == '*':
        tmp = str(int(l) * int(r))
    elif op == '+':
        tmp = str(int(l) + int(r))
    else:
        tmp = str(int(l) - int(r))
    return tmp
    
def onResult(expr, priority):
    expr = expr[:] # 파이썬의 특성 상 복사본으로 하지 않으면 원본 mutable
    for op in priority:
        stack = []
        while expr:
            # expr에서 빼와서 스택에 넣고 계산 후 다시 스택에 있는 값 expr에 넣기
            e = expr.pop(0)
            if e == op:
                stack.append(operation(stack.pop(), expr.pop(0), e))
            else:
                stack.append(e)
        expr = stack
    return abs(int(expr.pop(0)))

def solution(expression):
    answer = 0
    expr = []
    buffer = ""
    
    # 우선 순위 순열 (팩토리얼)
    priorities = list(itertools.permutations(['-', '+', '*'], 3))
    
    # 숫자, 연산자로 구분해서 모두 리스트에 집어넣기
    for e in expression:
        if e.isdigit():
            buffer += e
        else:
            expr.extend([buffer, e])
            buffer = ""
    
    expr.append(buffer)
    
    for priority in priorities:
        # 우선 순위 조합 별로 결과값보고 가장 큰 값 출력
        answer = max(answer, onResult(expr, priority))
    
    return answer