def solution(s):
    answer = 0
    for i in range(len(s)):
        # 문자열 rotate
        if (isRightStr(s, i)):
            answer += 1
    return answer

def isRightStr(string, startIndex):
    stack = []
    n = len(string)
    match = {']': '[', '}': '{', ')': '('} # object 이용
    
    for i in range(n):
        c = string[(startIndex + i) % n] # 문자열 rotate 식
        if c in match:
            # 닫는 괄호가 나왔을 때, 스택이 비어있거나 여는 괄호 짝이 안 맞을 때, 모두 올바르지 않은 문자열
            if not stack or stack[-1] != match[c]:
                return False
            else:
                # 올바른 형식이라면 스택에서 팝
                stack.pop()
        else:
            # 여는 괄호라면 집어넣기
            stack.append(c)         
    return not stack