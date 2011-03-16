

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
		
	def left(self):
		return ( self.parts[ self.orientation ], self.parts[ (self.orientation + 1) % self.n_sides ] )
	
	def down(self):
		return ( self.parts[ (self.orientation + 1) % self.n_sides ], self.parts[ (self.orientation + 2) % self.n_sides ] )
	
	def right(self):
		return ( self.parts[ (self.orientation + 2) % self.n_sides ], self.parts[ (self.orientation + 3) % self.n_sides ] )
	
	def up(self):
		return ( self.parts[ (self.orientation + 3) % self.n_sides ], self.parts[ (self.orientation + 4) % self.n_sides ] )
		
	def sides(self):
		return [ self.left(), self.down(), self.right(), self.up() ]
		
	def rotate(self, times = 1):
		self.orientation = ( self.orientation + times ) % self.n_sides
		
	def make_left(self, side):
		self.orientation = self.parts.index(side[0])
	
	def make_down(self, side):
		self.orientation = ( self.parts.index(side[0]) - 1 ) % self.n_sides
	
	def make_right(self, side):
		self.orientation = ( self.parts.index(side[0]) - 2 ) % self.n_sides
		
	def make_up(self, side):
		self.orientation = ( self.parts.index(side[0]) - 3 ) % self.n_sides

	def match_sides(self, self_side, target_side):
		return self_side[1] == target_side[0] and self_side[0] == target_side[1]
	

def test():

	p = Piece( [0, 1, 2, 3] )
	
	print p.left()
	print p.down()
	print p.right()
	print p.up()
	print p.sides()
	
	p.rotate(2)
	
	print p.sides()
	
	p.make_down( (0,1) )
	print p.sides()
	
if __name__ == "__main__":
	test()