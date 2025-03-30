# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 21:43:17 2025

@author: User
"""

import random

def print_board(board):
    print("   0   1   2")
    print("  ---|---|---")
    for i in range(3):
        print(f"{i}  " + " | ".join(board[i]))
        if i < 2:
            print("  ---|---|---")

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"
    
    while True:
        print_board(board)
        
        if player == "X":
            try:
                row, col = map(int, input("행과 열 입력 (0-2, 공백으로 구분): ").split())
                if board[row][col] != " ":
                    print("이미 차있는 자리입니다. 다시 선택하세요.")
                    continue
            except (ValueError, IndexError):
                print("잘못된 입력입니다. 0-2 범위의 숫자 두 개를 입력하세요.")
                continue
        else:
            row, col = computer_move(board)
            print(f"컴퓨터가 {row}, {col} 위치에 놓았습니다.")
        
        board[row][col] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"{player}가 승리했습니다!")
            break
        
        if is_full(board):
            print_board(board)
            print("무승부입니다!")
            break
        
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
    
    #Refer to ChatGPT