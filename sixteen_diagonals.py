# given an 5 x 5 board, you can place a piece in each box of the grid
# that diagonals from top left to bottom right, or bottom left to top right
# can you place fifteen pieces so that none of the pieces diagonals touch each other?
import time

def sixteen_diagonals(perm, piece_count):
  # return if 16 diagonals have been placed
  if len(perm) > 25:
    return
  if piece_count == 16:
    end = time.time()
    print("It took {elapsed} seconds to run this algorithm".format(elapsed=end-start)) 
    print(perm)
    exit()
  if len(perm) > 25 and piece_count < 16:
    return


  for d in [2, 1, 0]: # 0 is empty, 1 is TL to BR, 2 is BL to TR

    # otherwise try adding a diagonal to the board
    # at the next open spot
    perm.append(d)


    #check to see if this board can be extended
    if can_be_extended(perm):
      if d > 0:
        sixteen_diagonals(perm, piece_count + 1)
      else: 
        sixteen_diagonals(perm, piece_count)

    #if not, remove the piece
    perm.pop()

def can_be_extended(perm):
  # find the index of the last element
  # look at the indexes of the elements to the diagonal of this element
  # and to the side of it
  if conflict_diagonal(perm):
    return False
  elif conflict_horizontal_or_vertical(perm):
    return False
  else:
    return True

# check to see if elements in diagonal spots conflict with last placed element
def conflict_diagonal(perm):
  last_idx = len(perm) - 1
  #first check top left and right
  #must be at least first row
  if len(perm) > 5:
    if len(perm) % 5 > 1: #don't check TL diagonal for pieces on the left edge of the board
      top_left = perm[last_idx - 6]
      if perm[last_idx] == top_left:
        return True # there is a conflict
    elif len(perm) % 5 < 4: #don't check TR diagonal for pieces on the right edge of the board
      top_right = perm[last_idx - 4]
      check_conflict(perm[last_idx], top_right)
      if perm[last_idx] == top_right:
        return True
    else:
      return False
  
def conflict_horizontal_or_vertical(perm):
  last_idx = len(perm) - 1
  # check above and to the left of the current element
  if len(perm) > 5:
    above = perm[last_idx - 5]
    check_conflict(perm[last_idx], above)
    if abs(perm[last_idx] - above) == 1 and perm[last_idx] != 0 and above != 0:
      return True
  elif len(perm) % 5 > 1: #don't check to the left for pieces on the left edge of the board
    left = perm[last_idx - 1]
    if abs(perm[last_idx] - left) == 1 and perm[last_idx] != 0 and left != 0:
      return True
  else:
    return False
  
def check_conflict(i,j):
  difference = abs(i - j)
  if difference ==  1:
    return True     #there is a conflict
  else:
    return False

start = time.time()
sixteen_diagonals([], 0)
