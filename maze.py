from cell import Cell
import time
import random
class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win,seed):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        random.seed(seed)

        self.cells = []
        self.create_cells()
        self.break_entrance_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()
    
    def create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i,j)

    def draw_cell(self,i,j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1,x2,y1,y2)
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def break_entrance_exit(self):
        self.cells[0][0].topwall = False
        self.cells[self.num_cols-1][self.num_rows-1].bottomwall = False
        self.draw_cell(0,0)
        self.draw_cell(self.num_cols-1,self.num_rows-1)
  
    
    def break_walls_r(self,i,j):
        self.cells[i][j].visited = True
        while True:
            directions =[]
            if j > 0 and not self.cells[i][j-1].visited:
                directions.append((i,j-1)) 
            if j < self.num_rows-1 and not self.cells[i][j+1].visited:
                directions.append((i,j+1))
            if i > 0 and not self.cells[i-1][j].visited:
                directions.append((i-1,j)) 
            if i < self.num_cols-1 and not self.cells[i+1][j].visited:
                directions.append((i+1,j))
            if not directions :
                self.draw_cell(i,j) 
                return       
            else:
                chosen_direction = directions[random.randrange(len(directions))]
                if chosen_direction[1] == j - 1:
                    self.cells[i][j].topwall = False
                    self.cells[i][j-1].bottomwall = False   
                if chosen_direction[1] == j + 1:
                    self.cells[i][j].bottomwall = False
                    self.cells[i][j+1].topwall = False
                if chosen_direction[0] == i - 1:
                    self.cells[i][j].leftwall = False
                    self.cells[i-1][j].rightwall = False
                if chosen_direction[0] == i + 1:
                    self.cells[i][j].rightwall = False
                    self.cells[i+1][j].leftwall = False

                self.break_walls_r(chosen_direction[0],chosen_direction[1])

    def reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False