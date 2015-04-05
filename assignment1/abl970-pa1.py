# VI. Notice that I have provided a file called pa1tests.py and another called pa1tests-output.txt. These files are intended to show you how I will call your code, and what I expect your code to output. They are not intended to be exhaustive, but rather just to provide you with some testing. Please design more tests for your code as you see fit.

#Name: Austin Lawrence		netID:abl970
#This is a homework submission for assignment number 1 of EECS-348 Spring 2015.  It should be pretty snazzy.
import time
import math

def twoToTheN(n):
	"""returns 2^n after log(n) seconds"""
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
	for i in L:
		total = total + i
	return total/len(L)

def median(L):
	"""computes the median of list L"""
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

# You will probably want to read about how lists can be used as Stacks and Queues in the Python documentation (or it may be intuitive to you to just create Stack and Queue classes). IMPORTANT: to demonstrate that your functions actually perform breadth first, and depth first search, you must print each element in the tree just before it has been examined (on a line by itself). See an example of what this looks like as output in the file pa1tests-output.txt.

#breadth first: expand 4, then expand 10,3,14,1, then 33,2, then 12
# [4, [10, [33], [2]], [3], [14, [12]], [1]]
def bfs(tree,elem):
	"""performs breadth-first search for a given tree and search term 'element'"""
	from collections import deque
	# myTree = deque(tree)

	# Add the initial state (root) to the <fringe>
	fringe = deque()
	for i in tree:
		fringe.append(i)
	curr = fringe[0]
	fringe.popleft()
	print curr

	# Choose a node (curr) to examine from the <fringe> (if there is nothing in <fringe> - FAILURE)
	while curr != elem:
		node = fringe[0]
		# print 'node = ', node
		curr = node[0]
		for i in range(len(node)):
			if i != 0:
				fringe.append(node[i])
		fringe.popleft()
		print curr
		# print fringe
		# print ''
		if len(fringe) == 0:
			print "no match found"
			break

print "This should work:"
bfs([4, [10, [33], [2]], [3], [14, [12]], [1]],1)
print ''
print "I want this to work:"
bfs([4, [10, [33], [2]], [3], [14, [12]], [1]],2)
print ''
print "This should fail:"
bfs([4, [10, [33], [2]], [3], [14, [12]], [1]],40)



	# Is curr a goal state?
	

	# Expand curr by applying all possible actions (add the new resulting states to the <fringe>)



def dfs(tree,elem):
	"""performs depth-first search for a given tree and search term 'element'"""
	pass

class TTTBoard:
	def __init__(self):
		"""Initialize a 3x3 tic tac toe board. The board should contain a single attribute, a list, that initially contains nine star characters.  This list contains contents of the board.  A star denotes that this position has not yet been claimed by 'X' or 'O'.  Again, this is simply a flat list of 9 items, not a list of lists."""
		pass
	def __str__(self):
		"""Returns a string representation of the board. Instead of just displaying a flat list of the 9 items, I want you to display this list like a tic tac toe board, with 3 rows of 3 items each. See the test file output for what this looks like."""
		pass
	def makeMove(self,player,pos):
		"""Places a move for player in the position pos (where the board squares a numbered from left to right, starting in the top left squares with 0, and beginning at the left in each new row), if possible.  'player' is a character ('X' or 'O') and pos is an integer.  Returns True if the move was made and False if not (because te spot was full, or outside the boundaries of the board)."""
		pass
	def hasWon(self,player):
		"""Returns True if player has won the game, and False if not"""
		pass
	def gameOver(self):
		"""Returns True if someone has won or if the board is full, False otherwise"""
		pass
	def clear(self):
		"""Clears the board to reset the game"""
		pass




















