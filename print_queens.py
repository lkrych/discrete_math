#helper function to print n_queens board for visually verifying if solution is correct:
diagonal_dict = {
	0: " ",
	1: "/",
	2: "\\",

}

def print_queens(n, board):
	row = "| "
	for idx, square in enumerate(board):
		if idx % n == 0:
			row = row + diagonal_dict[square] + " | \n"
			print(row)
			row = "| "
		else:
			row = row + diagonal_dict[square] + " | "


print_queens(2, [0, 2, 1, 0])
