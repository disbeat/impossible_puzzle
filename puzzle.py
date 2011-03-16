from piece import *
from copy import deepcopy
import sys
from datetime import datetime

# time tracking
start = datetime.now()

# problem definition
ROW_SIZE = 6
COL_SIZE = 6

# output handling
f = open( "results.txt", "w" )

def log( msg ):
	''' Outputs the message with the current timestamp, for both console and output file f. '''
	global f
	
	f.write( "%s - %s\n" % ( str( datetime.now() ), str( msg ) ) )
	f.flush()
	print "%s - %s" % ( str( datetime.now() ), str( msg ) )

	
def out( msg ):
	''' Outputs the message for both console and output file f. '''
	global f
	f.write( "%s\n" % str(msg) )
	print "%s" % str(msg) 


# pieces initialization
	
pieces = [ Piece([3,6,5,2], 0),Piece([3,7,4,6], 1),Piece([7,6,1,4], 2),Piece([6,4,2,1], 3),Piece([4,1,3,2], 4),Piece([5,7,2,3], 5),Piece([1,5,2,6], 6),Piece([4,1,5,2], 7),Piece([1,6,2,4], 8),Piece([2,1,5,3], 9),Piece([6,3,5,1], 10),Piece([3,4,6,2], 11),Piece([2,3,4,5], 12),Piece([1,4,6,3], 13),Piece([1,4,2,6], 14),Piece([1,2,3,5], 15),Piece([1,6,5,4], 16),Piece([3,4,6,5], 17),Piece([6,2,4,5], 18),Piece([6,1,5,3], 19),Piece([5,1,2,4], 20),Piece([5,2,6,4], 21),Piece([4,2,7,5], 22),Piece([2,3,6,1], 23),Piece([1,4,3,2], 24),Piece([3,1,2,4], 25),Piece([6,7,1,3], 26),Piece([7,3,4,1], 27),Piece([3,2,6,4], 28),Piece([6,5,1,3], 29),Piece([4,3,5,1], 30),Piece([2,5,6,3], 31),Piece([3,2,5,4], 32),Piece([5,6,2,1], 33),Piece([6,3,5,4], 34),Piece([3,4,2,5], 35) ]

# dictionary with pieces indexed by side and corner
available_pieces = {}

# founded solutions
solutions = []

# max pieces added
max = 0

def add_piece( p ):
	''' Indexes piece p by side and conrners in available_pieces. '''
	global available_pieces
	
	for side in p.sides() + p.corners():
		if side not in available_pieces.keys():
			available_pieces[side] = list()
		if p not in available_pieces[side]:
			available_pieces[side].append( p )

		
def remove_piece( p ):
	''' Removes piece p from available pieces. '''
	global available_pieces
	for side in p.sides() + p.corners():
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
	''' Prints the solution and its ids. '''
	out( "========== PRINTING SOLUTION ============" )
	for row in solution:
		ups = []
		downs = []
		for piece in row:
			ups.append( (piece.side( UP )[1], piece.side( UP )[0]) )
			downs.append( piece.side( DOWN ) )
		out( ups )
		out( downs )
		
		out( "" )
	
	out( ":::::::::::::::: ID's :::::::::::::::::" )
	for row in solution:
		out( row )
	
	out( "========== SOLUTION PRINTED ============" )
		
		
def create_rows( solution, cur, restriction = None ):
	''' Creates a row of pieces, recursively. Restriction is the row above. '''
	
	global max, ROW_SIZE
	if len(cur) == ROW_SIZE:
		solution.append( cur )
		create_solution( solution )
		solution.remove( cur )
		return
	
	if (len(solution) * ROW_SIZE + len(cur) > max):
		max = len(solution) * ROW_SIZE + len(cur)
		
	side = cur[-1].side( RIGHT )
	side = (side[1], side[0])

	if restriction:
		side = ( restriction[len(cur)].side( DOWN )[1], side[0], side[1] )
	
	try:
		avail = deepcopy( available_pieces[side] )
	except:
		avail = []
	
	while len(avail) > 0:
		p = avail.pop()
		
		if restriction:
			p.positionate_corner( side, UP_LEFT )
		else:
			p.positionate_side( side, LEFT )
		
		cur.append( p )
		remove_piece( p )
		
		create_rows( solution, cur, restriction )
		
		cur.pop()
		add_piece( p )
		
	
def create_solution( solution ):
	''' Finds the first piece for the new row '''
	global solutions, COL_SIZE
	if len(solution) == COL_SIZE:
		print_solution( solution )
		solutions.append( deepcopy(solution) )
		return
	
	prev_row = solution[-1]
	
	side = prev_row[0].side( DOWN )
	side = (side[1], side[0])
	try:
		avail = deepcopy( available_pieces[side] )
		while len(avail) > 0:
			p = avail.pop()
			remove_piece( p )
			p.positionate_side( side, UP )		
			create_rows( solution, [p], prev_row )
			add_piece( p )
	except:
		pass
	

		
# add pieces to dict
for p in pieces:
	add_piece( p )


# iterate for all pieces as starting piece
for p in pieces:
	
	out( "\n CURRENT PIECE: %d \n\n" % p.pid )
	
	remove_piece( p )

	# test the piece in it's four possible positions
	for i in range(4):
		create_rows([], [p])
		
		p.rotate()
		log( "Tested Piece: %d with POSITION: %d. Total Pieces achieved: %d" % (p.pid, i+1, max) )
		max = 0
		
	add_piece( p )
	

for solution in solutions:
	print_solution( solution )
	
out( "# solutions: %d\nstarted at: %s\nended at: %s" % ( len(solutions), start, datetime.now() ) )