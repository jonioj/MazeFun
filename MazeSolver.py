import matplotlib.pyplot as plt
class MazeSolver:
    def __init__(self, maze):
        self.start = (1, 1)
        self.end = (maze.shape[0]-2, maze.shape[1]-2)
        self.s_stack = [self.start]
        self.current = self.s_stack[-1]
        self.history = []
        self.n_step = self.current
        self.maze = maze

    def go_e(self, x): return (x[0], x[1]+1)
    def go_s(self, x): return (x[0]+1, x[1])
    def go_w(self, x): return (x[0], x[1]-1)
    def go_n(self, x): return (x[0]-1, x[1])

    def go_forward(self):
        self.maze[self.current] = 4
        self.current = self.n_step
        self.s_stack.append(self.current)

    def try_to_go(self):
        self.n_step = self.go_e(self.current)
        if self.maze[self.n_step] == 1:
            self.go_forward()
        else:
            self.n_step = self.go_s(self.current)
            if self.maze[self.n_step] == 1:
                self.go_forward()
            else:
                self.n_step = self.go_w(self.current)
                if self.maze[self.n_step] == 1:
                    self.go_forward()
                else:
                    self.n_step = self.go_n(self.current)
                    if self.maze[self.n_step] == 1:
                        self.go_forward()
                    else:
                        self.s_stack.pop()
                        self.current = self.s_stack[-1]

    def solve(self):

        while self.current != self.end:

            if self.current in self.history:
                self.s_stack.pop()
                self.current = self.s_stack[-1]
                self.try_to_go()
            else:
                self.try_to_go()

            self.maze[self.current] = 4
        return self.maze
