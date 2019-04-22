import itertools as it

# in this optimized n queens solution, we will use the following idea
# if the current (partial) permutation cannot be extended to a solution (it
# contains two queens that can attack each other), we will stop trying to extend it
# the main idea is to cut the dead ends of the recursive tree
def find_n_queens_optimize(n):
  find_n_queens_backtrack([], n)


# we need to write our own permutations function because we don't want
# to generate a permutation that will obviously not work
def find_n_queens_backtrack(perm, n):
  if len(perm) == n:
    print(perm)
    exit()
  
  for k in range(n):
    if k not in perm:
      perm.append(k)

      # if the permutation can be extended, lets keep recursively diving until we find a
      # permutation of the correct length
      if can_be_extended_to_solution(perm):
        find_n_queens_backtrack(perm, n)

      #get rid of the last added element to permutation because it wasn't useful
      perm.pop()

# this helper function does the work of is_solution in the naive
# implementation of n_queens
# the input is a permutaiton
# and it checks for every index if the absolute value of the length of the permutation
# minus the index is equal to the difference between the values in the permutation at those indices
#
# this means that it just checks whether or not the last added queen (the last index) conflicts with any of the
# previous queens
def can_be_extended_to_solution(perm):
  i = len(perm) - 1
  for j in range(i): # for all indices
    if i - j == abs(perm[i] - perm[j]):
      return False
  return True

find_n_queens_optimize(20)