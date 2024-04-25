board = [[' ' for _ in range(3)] for _ in range(3)]
def printBoard(board1):
  for row in board:
    print('|'.join(row))

def winner(board, player):
  for row in board:
    if all(cell == player for cell in row):
      return True
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
  if all(board[i][i] == player for i in range(3) or \
         all(board[i][2-i] == player for i in range(3))):
    return True
def check(board):
  for row in board:
    if ' ' in row:
      return False

def tic_toe():
  player= 'X'
  while True:
    printBoard(board)
    row = int(input('Enter row (1-3): '))-1
    column = int(input('Enter column (1-3): '))-1
    if board[row][column] == ' ':
      board[row][column] = player
      if winner(board, player):
        print(f'Player {player} wins!')
        printBoard(board)
        break
      elif check(board):
        print("it is a draw")
        break
      player = 'O' if player == 'X' else 'X'
    else:
      print('position has been filled')

tic_toe()