import itertools as it
# on an n x n chessboard, can you find a chessboard
# where n queens are placed on it, but no queens are 
# able to attack each other?

def find_n_queens(n):
  #will return an array of integers where the index of the array
  #corresponds to the column, and the integer correponds to the row

  # create every possible permutation of queens on an n x n chessboard
  # and see if this permutation is a solution.
  for possible_solution in it.permutations(range(n), n):
    if is_solution(possible_solution):
      print(possible_solution)
      return


def is_solution(arr_of_queens):
  # because every queen will have their own row and column, we do not need to check the horizontal/vertical axis
  # we only need to check whether or not the diagonals of the queens overlap
  # this is where we need to translate the intuitive knowledge of what two queens attacking eachother
  # looks like in terms of discrete math:

  # Moving diagonally across a chessboard means moving exactly up/down the same squares as you move across
  # Thus two queens are on the same diagonal if:
  # |i1 - i2| = |j1 - j2|

  # Let's do an example. 
  # imagine there's a queen at (2,3) and another queen at (5,6)
  # |5 - 2| = |6 -3|, so the queens are the on same diagonal!

  for (i1, i2) in it.combinations(range(len(arr_of_queens)), 2):
    # for every combination of queens in the arr_of_queens
    # check to see if they are on a diagonal
    if abs(i1 - i2) == abs(arr_of_queens[i1] - arr_of_queens[i2]):
      return False
  
  return True

find_n_queens(8)