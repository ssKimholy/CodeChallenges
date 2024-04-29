def solution(n):
    answer = 0
    # 좌표를 (index, col)로 표현한다. 2차원 배열을 써도 되지만 메모리 아끼기.
    coordinate = [0] * n
    # 같은 열, 왼쪽 대각선, 오른쪽 대각선에 중복 확인용 set
    colS = set() # 1,2,3,4,... 순차적 숫자의 중복 검사
    diags = set() # x-y -> 규칙 상 x와 y의 차가 일치하면 동일한 왼쪽 대각선
    anti_diags = set() # x+y -> 규칙 상 x와 y의 합이 일치하면 동일한 오른쪽 대각선
    
    def n_queens(row):
        nonlocal answer
        if row == n:
            # n_queen이 완성된 경우
            answer += 1
            return
        else:
            # 한 행에 무조건 하나의 queen만 놓을 수 있기 때문에 n번만 탐색한다.
            for col in range(n):
                coordinate[row] = col # queen 두기
                diag = row - col # 왼쪽 대각선 
                anti_diag = row + col # 오른쪽 대각선
                # 만약 현재 (row, col)이 놓을 수 있는 위치라면 놓고 다음 행으로
                if isValidLocation(col, diag, anti_diag):
                    # 놓을 수 있는 위치라면 set에 삽입
                    colS.add(col)
                    diags.add(diag)
                    anti_diags.add(anti_diag)
                    # 다음 행으로
                    n_queens(row+1)
                    # 현재 행의 column, 왼쪽 대각선, 오른쪽 대각선이 달라지기에 set에서 지우고 새로운 col, diag, anti_diag 삽입 
                    colS.remove(col)
                    diags.remove(diag)
                    anti_diags.remove(anti_diag)
                    
    def isValidLocation(col, diag, andti_diag):
        # 현재 놓을 위치에 column, diag, anti_diag들 위치에 이미 놓여져 있는 퀸이 없는지 확인
        if col in colS or diag in diags or andti_diag in anti_diags:
            return False
        return True
    
    n_queens(0)
    return answer



    
    
