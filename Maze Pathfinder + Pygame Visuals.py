import pygame
import sys

maze = [
    list("#####################"),
    list("#     #        #  E##"),
    list("# ### # ###### # ####"),
    list("# #   #      # #    #"),
    list("# # ###### # # ###  #"),
    list("# #        # #      #"),
    list("# ########## ########"),
    list("#        #          #"),
    list("###### # # ##########"),
    list("#      # #         ##"),
    list("# ###### ######### ##"),
    list("#        #         ##"),
    list("######## # ##########"),
    list("#R                 ##"),
    list("#####################")] # defines the maze as a 2d array so it is easily edited


#-------------------------------PYGAME-----------------------------------------------------


pygame.init()  # starts pygame

rows = len(maze)	#makes the size changeable depending on the maze size and cell multiplier
cols = len(maze[0])
cellSize = 40

screen = pygame.display.set_mode((cols*cellSize, rows*cellSize))#creates screen
pygame.display.set_caption("MAZE SOLVER")

white = (255,255,255) #colours
black = (0, 0, 0)
red   = (255, 0, 0)  # start
green = (0, 255, 0)  # end
blue  = (0, 0, 255)  # robot path

screen.fill(white)
pygame.display.update()

def drawMaze():					# turns the maze characters into coloured squares
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            cell = maze[r][c]
            x = c * cellSize
            y = r * cellSize
            if cell == "#":
                pygame.draw.rect(screen, black, (x, y, cellSize, cellSize))
            elif cell == "R":
                pygame.draw.rect(screen, red, (x, y, cellSize, cellSize))
            elif cell == "E":
                pygame.draw.rect(screen, green, (x, y, cellSize, cellSize))
            elif cell == ".":
                pygame.draw.rect(screen, blue, (x, y, cellSize, cellSize))
            else:
                pygame.draw.rect(screen, white, (x, y, cellSize, cellSize))



#-------------------------------Depth First Search-----------------------------------------------



moves = ((0,1), (1,0), (0,-1), (-1,0)) #sets out every possible move the robot can take
visited = set() #makes the variable visited a set so there is no duplicate variables in it

def find(m, item):					#finds the grid location of the start and end points
    for i in range(len(maze)):			#repeats for every row and column until answer is found
        for x in range(len(maze[i])):
            if m[i][x] == item:
                return (i,x) 			#returns coordinates
            
def allowedMove(row,col):
    if row >= 0 and row < len(maze) and col >= 0 and col < len(maze[0]) and (row, col) not in visited and maze[row][col] != '#':	#checks the new column fits the parameters to be allowed(in the maze, not a # and not visited)
        return True
    else:
        return False

def dfs(row, col, v):				#depth first search
    if maze[row][col] == 'E':		#checks if the endpoint has been found yet 
        return True	#goal found
    v.add((row,col))				#adds the current grid location to the set visited so it can be checked later
    for move in moves:					#repeats for all 4 possible moves
        newRow = row + move[0]			#starting from the 1st input in moves, increments the column and row by each possible move amount
        newCol = col + move[1]			
        if allowedMove(newRow,newCol):	#checks new location is possible
            if dfs(newRow,newCol,v):#if the move is possible recursively calls dsf from inside dsf allowing constant repetition until the solution is found
                if (row,col) != startPoint:
                    maze[row][col] = '.'#sets the correct path to . after recursion the path is found
                    drawMaze()
                    pygame.display.update()
                    pygame.time.delay(50)
                return True				#if dsf is true returns true
    return False # if no solution can be found


#-------------------------------Main Code------------------------------------------------


startPoint = (find(maze, 'R'))	#find the start and end
endPoint = (find(maze, 'E'))

dfs(startPoint[0],startPoint[1],visited)	#calls dsf and brings in the starting column and row as well as the empty set visited

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    drawMaze()
    pygame.display.update()

pygame.quit()
sys.exit()
