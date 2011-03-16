from piece import Piece
from copy import deepcopy
import sys
from datetime import datetime

start = datetime.now()

f = open( "result_puzzle.txt", "w" )

def log( msg ):
	global f
	
	f.write( "%s - %s\n" % ( str( datetime.now() ), str( msg ) ) )
	f.flush()
	print "%s - %s\n" % ( str( datetime.now() ), str( msg ) )

def out( msg ):
	global f
	f.write( "%s\n" % str(msg) )
	print "%s\n" % str(msg) 


pieces = [ Piece([3,6,5,2], 0),Piece([3,7,4,6], 1),Piece([7,6,1,4], 2),Piece([6,4,2,1], 3),Piece([4,1,3,2], 4),Piece([5,7,2,3], 5),Piece([1,5,2,6], 6),Piece([4,1,5,2], 7),Piece([1,6,2,4], 8),Piece([2,1,5,3], 9),Piece([6,3,5,1], 10),Piece([3,4,6,2], 11),Piece([2,3,4,5], 12),Piece([1,4,6,3], 13),Piece([1,4,2,6], 14),Piece([1,2,3,5], 15),Piece([1,6,5,4], 16),Piece([3,4,6,5], 17),Piece([6,2,4,5], 18),Piece([6,1,5,3], 19),Piece([5,1,2,4], 20),Piece([5,2,6,4], 21),Piece([4,2,7,5], 22),Piece([2,3,6,1], 23),Piece([1,4,3,2], 24),Piece([3,1,2,4], 25),Piece([6,7,1,3], 26),Piece([7,3,4,1], 27),Piece([3,2,6,4], 28),Piece([6,5,1,3], 29),Piece([4,3,5,1], 30),Piece([2,5,6,3], 31),Piece([3,2,5,4], 32),Piece([5,6,2,1], 33),Piece([6,3,5,4], 34),Piece([3,4,2,5], 35) ]

available_pieces = {}

possibilities = []

solutions = []

max = 0

def add_piece( p ):
	global available_pieces
	for side in p.sides():
		if side not in available_pieces.keys():
			available_pieces[side] = list()
		if p not in available_pieces[side]:
			available_pieces[side].append( p )

		
def remove_piece( p ):
	global available_pieces
	for side in p.sides():
		try:
			a = available_pieces.pop(side)
			if p in a:
				try:
					a.remove(p)
				except:
					pass
			if len(a) > 0: 
				available_pieces[side] = a
		except:
			pass

def print_solution( solution ):
	out( "========== PRINTING SOLUTION ============" )
	for row in solution:
		ups = []
		downs = []
		for piece in row:
			ups.append( (piece.up()[1], piece.up()[0]) )
			downs.append( piece.down() )
		out( ups )
		out( downs )
		
		out( "" )
	
	out( ":::::::::::::::: ID's :::::::::::::::::" )
	for row in solution:
		out( row )
	
	out( "========== SOLUTION PRINTED ============" )
		
		
def create_rows( solution, cur, restriction = None ):
	if len(cur) == 6:
		solution.append( cur )
		create_solution( solution )
		solution.remove( cur )
		return
	
	side = cur[-1].right()
	side = (side[1], side[0])
	try:
		avail = deepcopy( available_pieces[side] )
	except:
		avail = []
	
	while len(avail) > 0:
		p = avail.pop()
		
		p.make_left(side)
		if restriction and not p.match_sides(p.up(), restriction[len(cur)].down()):
			continue

		cur.append( p )
		remove_piece( p )
		
		create_rows( solution, cur, restriction )
		
		cur.pop()
		add_piece( p )
		
	
def create_solution( solution ):
	global max, solutions
	if len(solution) == 6:
		print_solution( solution )
		solutions.append( deepcopy(solution) )
		return
	
	
	if len(solution) > max:
		max = len(solution)
		log( "max solution size: %d" % len( solution ) ) 
		
	prev_row = solution[-1]
	
	side = prev_row[0].down()
	side = (side[1], side[0])
	try:
		avail = deepcopy( available_pieces[side] )
		while len(avail) > 0:
			p = avail.pop()
			remove_piece( p )
			p.make_up(side)		
			create_rows( solution, [p], prev_row )
			add_piece( p )
	except:
		pass
	

		
# add pieces to dict
for p in pieces:
	add_piece( p )

	

	
rows = []
count = 0

for p in pieces:
	
	log( "\n\n\n CURRENT PIECE: %d \n\n\n" % p.pid )
	
	remove_piece( p )

	for i in range(4):
		create_rows([], [p])
		
		p.rotate()
		log( "Piece: %d ; POSITION: %d" % (p.pid, i) )
		sys.stdout.flush()
		max = 0
		
	add_piece( p )
	

for solution in solutions:
	print_solution( solution )
	
print "# solutions: %d\n started at: %s\n ended at: %s" % ( len(solutions), start, datetime.now() )