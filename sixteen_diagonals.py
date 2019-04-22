# given an 5 x 5 board, you can place a piece in each box of the grid
# that diagonals from top left to bottom right, or bottom left to top right
# can you place fifteen pieces so that none of the pieces diagonals touch each other?

def sixteen_diagonals(perm, count):
  # return if 16 diagonals have been placed
  if count == 16:
    print(perm)
    exit()

  for k in range (25):
    for d in range(3): # 0 is empty, 1 is TL to BR, 2 is BL to TR

      # otherwise try adding a diagonal to the board
      # at the next open spot
      perm.append(d)


      #check to see if this board can be extended
      if can_be_extended(perm):
        sixteen_diagonals(perm, count + 1)
  
      #if not, remove the piece
      perm.pop()

def can_be_extended(perm):
  # find the index of the last element
  # look at the indexes of the elements to the diagonal of this element
  # and to the side of it=
  if conflict_diagonal(perm):
    return False
  else if conflict_horizontal(perm):
    return False
  else:
    return True

# check to see if elements in diagonal spots conflict with last placed element
def conflict_diagonal(element, perm):
