def playerWon(player, method):
	print(f'{player} WON!! YAY!!\nMethod: {method}')
	quit()

def checkWins(board, symbols):
	# Vertical Winnin
	for row in board:
		for symbol in symbols:
			if row[0] == symbol and row[1] == symbol and row[2] == symbol:
				playerWon(symbol, 'vertical')

	# Horizontal Winning
	for i in range(len(board)):
		for symbol in symbols:
			if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
					playerWon(symbol, 'horizontal')

	# Diagonal Winning
	for symbol in symbols:
		if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
			playerWon(symbol, 'diagonal')
		if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
			playerWon(symbol, 'diagonal')