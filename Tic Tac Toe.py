print("Welcome to Tic Tac Toe!")
start = input("Do you want to play a game of Tic Tac Toe? ").lower()


if start == "yes":
    print("You are Player X. Your opponent is Player O.")
    print("This is the board layout")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8")
    print("Let's start the game!")
    board = [" "] * 9

    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("---------")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("---------")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def check_winner():
        winning_combinations = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
                return board[combo[0]]
        return None

    def is_draw():
        return " " not in board

    current_player = "X"

    while True:
        print_board()
        position = int(input(f"Player {current_player}, enter your move (0-8): "))

        if position < 0 or position > 8:
            print("Choose a number between 0 and 8.")
            continue

        if board[position] != " ":
            print("Please choose an empty position.")
            continue

        board[position] = current_player

        winner = check_winner()
        if winner:
            print_board()
            print(f"Player {winner} wins!")
            again = input("Want to play again? ").lower()
            if again == "yes":
                board = [" "] * 9
                current_player = "X"
                continue
            else:
                break

        if is_draw():
            print_board()
            print("It's a draw!")
            again = input("Want to play again? ").lower()
            if again == "yes":
                board = [" "] * 9
                current_player = "X"
                continue
            else:
                break

        current_player = "O" if current_player == "X" else "X"

else:
    print("Thank you for trying Tic Tac Toe!")
    print("Goodbye!")
