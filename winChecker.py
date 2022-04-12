from math import sqrt;

def playerWon(player, method):
	print(f'{player} WON!! YAY!!\nMethod: {method}')
	quit()

def checkWins(board, symbols):
	rowLength = int(sqrt(len(board)))
	# Horizontal Winning
	for i in range(len(board)):
		for symbol in symbols:
			if 0 <= i + 2 < len(board):
				if board[i] == symbol and board[i + 1] == symbol and board[i + 2] == symbol:
					playerWon(symbol, 'horizontal')

	# Vertical Winning
	for i in range(rowLength):
		for symbol in symbols:
			if max(1, i) * 3 * rowLength < len(board) - 1:
				if board[i * rowLength] == symbol and board[max(1, i) * 2 * rowLength] == symbol and board[max(1, i) * 3 * rowLength] == symbol:
					playerWon(symbol, 'vertical')

	# Diagonal Winning
	for i in range(rowLength):
		for symbol in symbols:
			if i + 2 * rowLength + (i + 2) < len(board) - 1:
				if board[i * rowLength + i] == symbol and board[(i + 1) * rowLength + i + 1] == symbol and board[(i + 2) * rowLength + i + 2] == symbol:
					playerWon(symbol, 'diagonal')

	for i in range(1, rowLength):
		for symbol in symbols:
			if (i + 2) * rowLength - i - 2 < len(board) - 1:
				if board[i * rowLength - i] == symbol and board[(i + 1) * rowLength - i - 1] == symbol and board[(i + 2) * rowLength - i - 2] == symbol:
					playerWon(symbol, 'diagonal')
