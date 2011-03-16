LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

UP_LEFT = 0
DOWN_LEFT = 1
DOWN_RIGHT = 2
UP_RIGHT = 3

class Piece( object ):
	''' Class that represents a puzzle piece. It has its contents in self.parts. One can request sides or corners using the above directions. '''
	n_sides = 4
	side_size = 2
	
	def __init__(self, parts, pid):
		''' Piece initialization. Set the content (parts) of the piece, its id and the base orientation. '''
		self.parts = parts
		self.orientation = 0
		self.pid = pid
	
	def __str__(self):
		''' String representation of the piece. '''
		return str(self.pid)
	
	def __eq__(self, other):
		''' Comparison needed for copied objects matches. '''
		return self.pid == other.pid
		
	def __repr__(self):
		''' Representation needed for list prints. '''
		return str(self.pid)
		
	def sides(self):
		''' Return a list of the sides as tuples. '''
		return [ self.side(i) for i in range(self.n_sides) ]
		
	def side(self, direction):
		''' Returns a side tuple correspondent to the given direction. '''
		return tuple([ self.parts[ (self.orientation + direction * (self.side_size-1) + i) % self.n_sides ] for i in range(self.side_size) ])
		
	def corners(self):
		''' Returns a list of the corners as tuples. '''
		return [ self.corner(i) for i in range(self.n_sides) ]
	
	def corner(self, direction):
		''' Returns a corner as tuple. The corner corresponds to the both sides it joins united. '''
		return tuple([ self.parts[ (self.orientation + direction * (self.side_size-1) + i ) % self.n_sides ] for i in range(-(self.side_size-1), self.side_size) ])
		
	def rotate(self, times = 1):
		''' Rotates the piece 90 degrees counter clockwise. '''
		self.orientation = ( self.orientation + times * (self.side_size-1) ) % self.n_sides
		
	def positionate_side(self, side, direction):
		''' Orientates the piece so side places at direction '''
		self.orientation = (self.parts.index(side[0]) - direction * (self.side_size-1) ) % self.n_sides
	
	def positionate_corner(self, corner, direction):
		''' Orientates the piece so corner places at direction '''
		self.orientation = (self.parts.index(corner[1]) - direction * (self.side_size-1) ) % self.n_sides
		
	
def test():

	p = Piece( [0, 1, 2, 3], 0 )
	
	print p.sides()
	
	p.rotate(2)
	
	print p.sides()
	
	p.positionate_side( (0,1), UP )
	print p.sides()
	
	p.positionate_corner( (0,1,2), DOWN_RIGHT )
	print p.corners()
	
	print p.side( LEFT )
	
	p.positionate_corner( (0,1,2), UP_LEFT )
	print p.corners()
	
	p.positionate_side( (0,1), LEFT )
	print p.sides()
	
if __name__ == "__main__":
	test()