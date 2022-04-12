from math import floor
from winChecker import checkWins


def create_board(x, y):
  board = []

  for i in range(x):
    row = ["-"] * y
    board.append(row)
  
  return board


xSize = 5
ySize = 5

def display(board):
  for row in board:
    row = " ".join(row)
    print(row)
    
board = create_board(xSize, ySize)
display(board)
symbols = ["X"]
winner = "none"

def placeOnBoard(spotX, set, list):
  if not list[floor(spotX / ySize + 1)][(spotX % xSize) - 1] == "-":
    return list

  list = list[floor(spotX / ySize + 1)][(spotX % xSize) - 1] = set
  return list

def playTurn(turn, board):
    pr = "{}'s turn! > ".format(turn)
    spotX = int(input(pr))
    board = placeOnBoard(spotX, turn, board)
    display(board)
    checkWins(board, turn)

#note to self, its in order y and then x, not x and then y.

while winner == "none":
  for i in range(len(symbols)):
    playTurn(symbols[i], board)
  