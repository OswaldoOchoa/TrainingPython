def isSolved(board):
   vertical = []
   diagonal1 = []
   diagonal2 = []
   counter = 0
   win = 3
   for lines in board:
      if win in (lines.count(1), vertical.count(1)):
         return 1
         break
      if win in (lines.count(2), vertical.count(2)):
         return 2 
         break
      if 0 in lines:
         empty = -1
      vertical.append(lines[0])
      diagonal1.append(lines[0+counter])
      diagonal2.append(lines[2-counter])
      counter+=1
   if win in (diagonal1.count(1), diagonal2.count(1)):
         return 1
   elif win in (diagonal1.count(2), diagonal2.count(2)):
         return 2
   elif empty == -1:
         return empty
   else:
         return 0
   return(vertical)
   return(diagonal1)
   return(diagonal2)




board = [[0, 0, 1],
         [1, 1, 2],
         [2, 1, 0]]


isSolved(board)