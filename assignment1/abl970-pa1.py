#Name: Austin Lawrence		netID:abl970
#This is a homework submission for assignment number 1 of EECS-348 Spring 2015.  It should be pretty snazzy.



def twoToTheN(n):
	"""returns 2^n after log(n) seconds"""
	import time
	import math

	# set up timer
	start = time.time()
	val = 2**n 
	wait = math.log10(n)
	timer = time.time()

	# loop until time elapsed meets threshold
	while timer-start<=wait:
		timer = time.time() #update timer


def mean(L):
	"""computes the mean of list L"""
	total = 0

	# sum all of the terms and divide
	for i in L:
		total = total + i
	return total/len(L)


def median(L):
	"""computes the median of list L"""

	# get the length of the list
	length = len(L)
	if length%2 == 0:

		#the value is even, average the two middle terms
		index1 = length/2-1
		index2 = length/2
		return (L[index1]+L[index2])/2
	
	else:
		#the value is odd, take the middle term
		index = (length-1)/2+1
		return L[index]


def bfs(tree,elem):
	"""performs breadth-first search for a given tree and search term 'element'"""
	from collections import deque	# library that allows us to pop and append at the beginning of a list easily

	# Add the initial state (root) to the <fringe>
	fringe = deque() # creates a list that allows us to pop and append on the left side (slow operation)
	
	# take every available node in the tree and add it to fringe
	for i in tree:
		fringe.append(i)
	curr = fringe[0]  # the first element should not be a list
	fringe.popleft()
	print curr

	# Choose a node (curr) to examine from the <fringe> (if there is nothing in <fringe> - FAILURE)
	while curr != elem:
		node = fringe[0]
		curr = node[0]
		for i in range(len(node)):
			if i != 0:
				fringe.append(node[i])
		fringe.popleft()
		print curr

		# Test that data still exists in fringe and that the goal has been met
		if len(fringe) == 0 and curr == elem:
			return True
		elif len(fringe) == 0 and curr != elem:
			return False
	return True  #if we get this far, then we found a match


def dfs(tree,elem):
	"""performs depth-first search for a given tree and search term 'element'"""
	from collections import deque

	# Add the initial state (root) to the fringe
	myList = deque(tree)
	curr = myList.popleft()
	print curr

	# repeat until the list is length zero or the target is found 
	while curr != elem:
		node = myList.pop()
		curr = node[0]
		print curr
		if len(node) > 1:
			for i in range(len(node)):
				if i != 0:   # skip the first element of node because we've evaluated it as curr
					myList.append(node[i])
		
		# Test that data still exists in myList and that the goal has been met
		if len(myList) == 0 and curr == elem:
			return True
		elif len(myList) == 0 and curr != elem:
			return False
	return True  #if we get this far, then we found a match

class TTTBoard:
	def __init__(self):
		"""Initialize a 3x3 tic tac toe board. The board should contain a single attribute, a list, that initially contains nine star characters.  This list contains contents of the board.  A star denotes that this position has not yet been claimed by 'X' or 'O'.  Again, this is simply a flat list of 9 items, not a list of lists."""
		self.board = ['*','*','*','*','*','*','*','*','*']
		self.count = 0  #used for tracking the number of moves that have been made.  If == 8, then game cannot continue.

	def __str__(self):
		"""Returns a string representation of the board. Instead of just displaying a flat list of the 9 items, I want you to display this list like a tic tac toe board, with 3 rows of 3 items each. See the test file output for what this looks like."""
		return str(self.board[0])+"|"+str(self.board[1])+"|"+str(self.board[2])+"\r\n"+"--"+"--"+"--"+"\r\n"+str(self.board[3])+"|"+str(self.board[4])+"|"+str(self.board[5])+"\r\n"+"--"+"--"+"--"+"\r\n"+str(self.board[6])+"|"+str(self.board[7])+"|"+str(self.board[8])
	
	def makeMove(self,player,pos):
		"""Places a move for player in the position pos (where the board squares a numbered from left to right, starting in the top left squares with 0, and beginning at the left in each new row), if possible.  'player' is a character ('X' or 'O') and pos is an integer.  Returns True if the move was made and False if not (because te spot was full, or outside the boundaries of the board)."""
		if self.board[pos] == "*":  # checks to see if a move has been made already
			self.board[pos] = player
			self.count += 1
			return True
		else:
			return False
	
	def hasWon(self,player):
		"""Returns True if player has won the game, and False if not"""

		# check diagonals
		if self.board[0] == player and self.board[4] == player and self.board[8] == player:
			return True
		elif self.board[2] == player and self.board[4] == player and self.board[6] == player:
			return True

		# check horizontals
		elif self.board[0] == player and self.board[1] == player and self.board[2] == player:
			return True
		elif self.board[3] == player and self.board[4] == player and self.board[5] == player:
			return True
		elif self.board[6] == player and self.board[7] == player and self.board[8] == player:
			return True

		# check verticals
		elif self.board[0] == player and self.board[3] == player and self.board[6] == player:
			return True
		elif self.board[1] == player and self.board[4] == player and self.board[7] == player:
			return True
		elif self.board[2] == player and self.board[5] == player and self.board[8] == player:
			return True

		# if nothing, return false
		return False

	def gameOver(self):
		"""Returns True if someone has won or if the board is full, False otherwise"""
		if hasWon('X') or hasWon('O') or self.count>=8:
			return True
		else:
			return False

	def clear(self):
		"""Clears the board to reset the game"""
		self.board = ['*','*','*','*','*','*','*','*','*']
		self.count = 0




















