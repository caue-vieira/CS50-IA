import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Verifica se o jogador venceu nas linhas, colunas ou diagonais
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Verifica se o tabuleiro está cheio
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def minimax(board, depth, is_maximizing):
    if is_winner(board, "X"):
        return -1
    if is_winner(board, "O"):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True  # True: jogador, False: IA

    print("Bem-vindo ao Jogo da Velha!")
    while True:
        print_board(board)

        if player_turn:
            row, col = map(int, input("Informe a linha e coluna (0-2): ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
                player_turn = not player_turn
        else:
            print("Vez da IA (O)...")
            row, col = find_best_move(board)
            board[row][col] = "O"
            player_turn = not player_turn

        if is_winner(board, "X"):
            print_board(board)
            print("Você ganhou! Parabéns!")
            break
        elif is_winner(board, "O"):
            print_board(board)
            print("A IA ganhou! Tente novamente.")
            break
        elif is_full(board):
            print_board(board)
            print("Empate! O jogo terminou em empate.")
            break

if __name__ == "__main__":
    main()
