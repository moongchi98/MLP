def solution(board, moves):
    catch_box = []
    answer = 0
    for move in moves:
        for j in range(len(board)):
            #왜 이거를 doll이라고 선언하면 안돼지?
            if board[j][move-1] != 0:
                catch_box.append(board[j][move-1])
                board[j][move-1] = 0
                #if 문이 추가한 이후에 설정되야 한다
                if len(catch_box) > 1:
                    if catch_box[-1] == catch_box [-2]:
                        catch_box.pop(-1)
                        catch_box.pop(-1)
                        answer += 2
                #다음 move로 가기위함
                break
    
    return answer

