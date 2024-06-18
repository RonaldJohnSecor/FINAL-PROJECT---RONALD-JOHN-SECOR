def print_board(board):
    # Clear the screen for a fresh display of the board
    print("\033[H\033[J")
    
    # Print the board with current moves
    print("  1 2 3")
    for i in range(3):
        print(f"{i+1} {' '.join(board[i])}")
    print()

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def is_valid_move(board, move):
    # Check if the move is within the board boundaries and the cell is empty
    row, col = move
    return 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == ' '

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['Player 1', 'Player 2']
    symbols = ['X', 'O']
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        symbol = symbols[turn % 2]
        
        # Get player move
        while True:
            try:
                print(f"{player}'s turn ({symbol})")
                row = int(input("Enter row (1-3): "))
                col = int(input("Enter column (1-3): "))
                if is_valid_move(board, (row, col)):
                    board[row-1][col-1] = symbol
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Check for win
        if check_win(board, symbol):
            print_board(board)
            print(f"Congratulations! {player} ({symbol}) wins!")
            break
        
        # Check for draw
        if all([cell != ' ' for row in board for cell in row]):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1

# Start the game
tic_tac_toe()