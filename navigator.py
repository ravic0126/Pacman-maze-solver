from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start , end ):
        # IMPLEMENT FUNCTION HERE
        if self.navigator_maze[start[0]][start[1]]==1 or self.navigator_maze[end[0]][end[1]]==1:
            raise PathNotFoundException
        m=len(self.navigator_maze)
        n=len(self.navigator_maze[0])
        l=Stack()
        l.push(start)
        self.navigator_maze[start[0]][start[1]]=2
        while l.top()!=end:
            if l.isEmpty():
                raise PathNotFoundException
            a,b=l.top()
            if b < n - 1 and self.navigator_maze[a][b + 1] == 0:
                l.push((a,b+1))
                self.navigator_maze[a][b + 1] = 2
            elif a > 0 and self.navigator_maze[a - 1][b] == 0:
                l.push((a-1,b))
                self.navigator_maze[a - 1][b] = 2
            elif b > 0 and self.navigator_maze[a][b - 1] == 0:
                l.push((a, b - 1))
                self.navigator_maze[a][b - 1] = 2
            elif a < m - 1 and self.navigator_maze[a + 1][b] == 0:
                l.push((a + 1, b))
                self.navigator_maze[a + 1][b] = 2
            else:
                l.pop()
        return l.prt()