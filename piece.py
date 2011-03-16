LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

UP_LEFT = 0
DOWN_LEFT = 1
DOWN_RIGHT = 2
UP_RIGHT = 3

class Piece( object ):
	n_sides = 4
	
	def __init__(self, parts, pid):
		self.parts = parts
		self.orientation = 0
		self.pid = pid
	
	def __str__(self):
		return str(self.pid)
	
	def __eq__(self, other):
		return self.pid == other.pid
		
	def __repr__(self):
		return str(self.pid)
		
	def sides(self):
		return [ self.side(i) for i in range(self.n_sides) ]
		
	def side(self, i):
		return ( self.parts[ (self.orientation + i) % self.n_sides ], self.parts[ (self.orientation + i + 1) % self.n_sides ] )
		
	def corners(self):
		return [ self.corner(i) for i in range(self.n_sides) ]
	
	def corner(self, i):
		return ( self.parts[ (self.orientation + i - 1) % self.n_sides ], \
				 self.parts[ (self.orientation + i) % self.n_sides ], 	 \
				 self.parts[ (self.orientation + i + 1) % self.n_sides ] )
		
	def rotate(self, times = 1):
		self.orientation = ( self.orientation + times ) % self.n_sides
		
	def positionate_side(self, target_side, target_direction):
		self.orientation = (self.parts.index(target_side[0]) - target_direction ) % self.n_sides
	
	def positionate_corner(self, target_corner, target_direction):
		self.orientation = (self.parts.index(target_corner[1]) - target_direction ) % self.n_sides
		
	def match_sides(self, self_side, target_side):
		return self_side[1] == target_side[0] and self_side[0] == target_side[1]
	

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