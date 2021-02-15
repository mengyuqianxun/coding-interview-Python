board = [[1,2,3],[4,1,5],[6,4,6]]

n, m = len(board), len(board[0])
board = [['#'] + row + ['#'] for row in board]
board.insert(0, ['#' for _ in range(m + 2)])
board.append(['#' for _ in range(m + 2)])

print(board)
