# %%
import random
import numpy as np
import matplotlib.pyplot as plt


class Cell:
    def __init__(self, state):
        self.state = state


class MazeGenerator:

    def __init__(self):
        pass

    def createMaze(self, mWidth, mHeight):
        self.mWidth = mWidth
        self.mHeight = mHeight
        self.visited = 1
        self.stack = [{"x": 0, "y": 0}]
        self.maze = [{
            "visited": 1,
            "n_n": 0,
            "e_n": 0,
            "s_n": 0,
            "w_n": 0}]
        for i in range(self.mWidth*self.mHeight - 1):
            self.maze.append({
                "visited": 0,
                "n_n": 0,
                "e_n": 0,
                "s_n": 0,
                "w_n": 0})

        def offset(x, y): return (
            self.stack[-1]["y"] + y) * self.mWidth + (self.stack[-1]["x"] + x)

        while self.visited < len(self.maze):
            neighbours = []
            def choose_n(n): return random.choice(n)

            # NORTH
            if self.stack[-1]["y"] > 0:
                if self.maze[offset(0, -1)]['visited'] == 0:
                    neighbours.append(0)
            # EAST
            if self.stack[-1]["x"] < self.mWidth - 1:
                if self.maze[offset(1, 0)]["visited"] == 0:
                    neighbours.append(1)
            # SOUTH
            if self.stack[-1]["y"] < self.mHeight - 1:
                if self.maze[offset(0, 1)]['visited'] == 0:
                    neighbours.append(2)
            # WEST
            if self.stack[-1]["x"] > 0:
                if self.maze[offset(-1, 0)]["visited"] == 0:
                    neighbours.append(3)

            if len(neighbours) != 0:

                next_cell = choose_n(neighbours)
                if next_cell == 0:
                    self.maze[offset(0, 0)]['n_n'] = 1
                    self.maze[offset(0, -1)]['s_n'] = 1
                    self.stack.append(
                        {'x': self.stack[-1]['x'] + 0, 'y': self.stack[-1]['y']-1})
                elif next_cell == 1:
                    self.maze[offset(0, 0)]['e_n'] = 1
                    self.maze[offset(1, 0)]['w_n'] = 1
                    self.stack.append(
                        {'x': self.stack[-1]['x'] + 1, 'y': self.stack[-1]['y']-0})
                elif next_cell == 2:
                    self.maze[offset(0, 0)]['s_n'] = 1
                    self.maze[offset(0, 1)]['n_n'] = 1
                    self.stack.append(
                        {'x': self.stack[-1]['x'] + 0, 'y': self.stack[-1]['y']+1})
                elif next_cell == 3:
                    self.maze[offset(0, 0)]['w_n'] = 1
                    self.maze[offset(-1, 0)]['e_n'] = 1
                    self.stack.append(
                        {'x': self.stack[-1]['x'] - 1, 'y': self.stack[-1]['y']-0})

                self.maze[offset(0, 0)]['visited'] = 1
                self.visited += 1
            else:
                self.stack.pop()
        return self.maze

    def showMaze(self, maze):

        empty = np.zeros(
            (2*self.mHeight+self.mHeight+1, 2*self.mWidth+self.mWidth+1), dtype=int)
        i = 0
        for cell in maze:
            column = i//self.mWidth
            row = i - column*self.mWidth
            if cell['visited'] == 1:
                empty[3*column+1][3*row+1] = 1
                empty[3*column+1][3*row+2] = 1
                empty[3*column+2][3*row+1] = 1
                empty[3*column+2][3*row+2] = 1

            if cell['e_n'] == 1:
                empty[3*column+1][3*row+3] = 1
                empty[3*column+2][3*row+3] = 1

            if cell['n_n'] == 1:
                empty[3*column][3*row+1] = 1
                empty[3*column][3*row+2] = 1
                
            if cell["w_n"] == 1:
                empty[3*column+1][3*row] = 1
                empty[3*column+2][3*row] = 1
                
            if cell['s_n'] == 1:
                empty[3*column+3][3*row+1] = 1
                empty[3*column+3][3*row+2] = 1

            i += 1

        print(empty)
        return empty


# %%
generator = MazeGenerator()
maze = generator.createMaze(30, 4)
for cell in maze:
    print(cell)
maze = generator.showMaze(maze)
# %%
plt.imshow(maze)
