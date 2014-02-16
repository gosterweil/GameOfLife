#GAME OF LIFE
# This script is a implementation of Conway's game of life, using
# pygame.
#
########################################################################
import pygame, time, numpy, sys
from pygame.locals import *


#One-time program initialization
pygame.init()

SCREEN_SIZE_X = 640		
SCREEN_SIZE_Y = 480 
CELL_SIZE = 20
assert not SCREEN_SIZE_X % CELL_SIZE, "Error! Scren size must be divisible by cell size."
assert not SCREEN_SIZE_Y % CELL_SIZE, "Error! Screen size must be divisible by cell size."

GRID_SIZE_X = SCREEN_SIZE_X / CELL_SIZE
GRID_SIZE_Y = SCREEN_SIZE_Y / CELL_SIZE

surface = pygame.display.set_mode((SCREEN_SIZE_X,SCREEN_SIZE_Y))
surface.fill(pygame.Color(255,255,255))
grid = numpy.zeros((GRID_SIZE_X,GRID_SIZE_Y))

pygame.display.set_caption("Conway's Game of Life")


def draw_grid_lines():
	""" Draw the lines of the game grid based on the size of a cell """
	for x in range(CELL_SIZE, SCREEN_SIZE_X, CELL_SIZE): #Vertical Grid lines
		pygame.draw.line(surface, pygame.Color(0,0,0),
		 (x,0), (x, SCREEN_SIZE_Y))
	for y in range(CELL_SIZE, SCREEN_SIZE_Y,CELL_SIZE):
		pygame.draw.line(surface, pygame.Color(0,0,0),
			(0,y),(SCREEN_SIZE_X,y))
def draw_grid():
	""" Update grid cells. White if dead, black if  alive """
	for cell_pos, cell_val in numpy.ndenumerate(grid):
		cell_x, cell_y = cell_pos
		cell_rect = pygame.Rect( (cell_x * CELL_SIZE, cell_y * CELL_SIZE), 
				(cell_x * CELL_SIZE + CELL_SIZE, cell_y * CELL_SIZE + CELL_SIZE) )
		if cell_val == 0: #Make white
			pygame.draw.rect(surface,pygame.Color(255,255,255),cell_rect)
		elif cell_val == 1: #Make black
			pygame.draw.rect(surface,pygame.Color(0,0,0),cell_rect)
def get_mouse_cell():
	""" Returns the grid cell of the curent mouse position """
	mouse_pos_x,mouse_pos_y = pygame.mouse.get_pos()
	#This uses integer floor divison to get the cell the mouse is in, since
	# we don't care about individual pixels, only grid positions
	cell = (mouse_pos_x / CELL_SIZE, mouse_pos_y / CELL_SIZE) 
	return cell
def get_neighbors(cell):
	"""Returns 3x3 matrix of adjacent cells, centered on cell """
	x,y = cell
	neighbors = grid.take(range(x-1,x+2),mode='wrap',axis=0).take(range(y-1,y+2),mode='wrap',axis=1)
	return neighbors

def count_living_neighbors(cell):
	"""Returns the number of neighbors alive in the eight adjacent cells to cell """
	count = 0
	neighbors = get_neighbors(cell)
	for cell_pos, cell_val in numpy.ndenumerate(neighbors):
		if not cell_pos == (1,1): # Make sure we don't count the cell we're looking at
			if cell_val == 1:
				count = count + 1
	return count 
def is_living(val):
	return val == 1
def update_grid():
	global grid
	newgrid = grid.copy()
	for cell_pos,cell_val in numpy.ndenumerate(grid):
		count = count_living_neighbors(cell_pos)
		if is_living(cell_val): 
			if count < 2: #Dies
				newgrid[cell_pos] = 0
			elif count > 3: #dies
				newgrid[cell_pos] = 0
			elif count == 3 or count == 2: # lives on
				newgrid[cell_pos] = 1
		else: # cell is dead:
			if count == 3: #Revived
				newgrid[cell_pos] = 1
			else:
				newgrid[cell_pos] = 0
	grid = newgrid
timer_on = False 
frame_length = 500
#Begin main loop
while True:
	draw_grid()
	draw_grid_lines()
	for event in pygame.event.get(): 	#Event loop
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if not timer_on:
					pygame.time.set_timer(pygame.USEREVENT+1,frame_length)
					timer_on = True
				else:
					pygame.time.set_timer(pygame.USEREVENT+1,0)
					timer_on = False
	
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: #Left Mouse
				cell = get_mouse_cell()
				
				#Toggle dead or alive value
				if grid[cell] == 0:
					grid[cell] = 1
				
				elif grid[cell] == 1:
					grid[cell] = 0
		if event.type == pygame.USEREVENT+1:
			update_grid()
	pygame.display.update()
