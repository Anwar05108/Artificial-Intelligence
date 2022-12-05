# Objective: Write a program to solve the n-puzzle problem using the A* search algorithm, where
# 𝑛 = 𝑘ଶ − 1, 𝑘 = 3, 4, 5 ...
# Problem description: The n-puzzle is a puzzle invented and popularized by Noyes Palmer
# Chapman in the 1870s. It is played on a 𝑘 × 𝑘 grid with 𝑛 = 𝑘ଶ − 1 square blocks labeled 1
# through 𝑛 and a blank square. Your goal is to rearrange the blocks so that they are in order, using
# as few moves as possible. You are permitted to slide blocks horizontally or vertically into the blank
# square. The following shows a sequence of legal moves from an initial board (left) to the goal
# board (right)

# Input: The input file contains a sequence of boards, with each board occupying 𝑘 lines, where
# each line contains 𝑘 integers between 0 and 𝑛, inclusive, with the 0 denoting the blank square.
# The boards are separated by blank lines. The first board in the file is the initial board, and the
# last board is the goal board. You may assume that all boards in the file are solvable.

# Output: For each board in the input file (except the last one), print the board, followed by a
# blank line, followed by the sequence of boards that leads from the initial board to the goal board,
# followed by a blank line. If no solution exists, print the word “No solution possible.”

# Sample input:
# 1 2 3
# 4 5 6
# 7 8 0



def main():
	# Read the input file
	with open('input.txt', 'r') as f:
		lines = f.readlines()

	# Parse the input file
	board = []
	for line in lines:
		if line == '\n':
			continue
		board.append([int(x) for x in line.split()])

	# Print the board
	print_board(board)

	# Solve the board
	solve_board(board)

def print_board(board):
	# Print the board
	for row in board:
		print(row)

def solve_board(board):
	# Solve the board
	print('Solving board...')
	print_board(board)

if __name__ == '__main__':
	main()

# Sample output:
# 1 2 3
# 4 5 6