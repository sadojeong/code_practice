def solution(board, moves):
    box = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                box.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(box) > 1:
                    if box[-1] == box[-2]:
                        box.pop(-1)
                        box.pop(-1)
                        answer += 2
                break
    return answer