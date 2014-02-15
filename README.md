#Game Of Life
==========
##About 
A very simple implementation of Conway's Game of Life with Python and Pygame
Conway's Game of Life is a cellular automaton designed by the British mathematician John Conway.
The 'game' simulates the growth of cells from an inital state by following a very simple set of rules.
Each Generation:
	1. Living cells with fewer than two live neighbours die
	2. Living cells with two or three live neighbours live on
	3. Living cells with more than three live neighbours die
	4. Dead cells with exactly three live neighbours become alive
These simple rules can create very intricate patterns.
For more information on The Game of Life, see it's [Wikipedia page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

##Running
This application depends on Python version 2.7, NumPy version 1.8, and Pygame version 1.9.1

[Python Download](http://python.org/download/)
[NumPy Download] (http://www.scipy.org/scipylib/download.html)
[PyGame Download] (http://pygame.org/download.shtml)

Once the dependencies have been installed, simply open game_life.py with Python.
##Usage
Click on any cell to toggle it from alive to dead or vice-versa.
Press the space bar to start and pause the simulation. 
