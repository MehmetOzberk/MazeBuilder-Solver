from graphics import Line,  Point
class Cell:
    def __init__(self,win):
        self.leftwall = True
        self.rightwall = True
        self.topwall = True
        self.bottomwall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
        self.visited = False

    def draw(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        leftline = Line(Point(self.x1,self.y1),Point(self.x1,self.y2))
        topline = Line(Point(self.x1,self.y1),Point(self.x2,self.y1))
        rightline = Line(Point(self.x2,self.y1),Point(self.x2,self.y2))
        bottomline = Line(Point(self.x2,self.y2),Point(self.x1,self.y2))
        if(self.leftwall):
            self.win.draw_line(leftline,"black")
        else:
            self.win.draw_line(leftline,"white")   
        if(self.topwall):
            self.win.draw_line(topline,"black")
        else:
            self.win.draw_line(topline,"white")  
        if(self.rightwall):
            self.win.draw_line(rightline,"black")
        else:
            self.win.draw_line(rightline,"white")  
        if(self.bottomwall):  
            self.win.draw_line(bottomline,"black")
        else:
            self.win.draw_line(bottomline,"white")  
    
    def draw_move(self, to_cell, undo):
        selfymid = (self.y1-self.y2)/2+self.y2
        selfxmid = (self.x2-self.x1)/2+self.x1
        otherymid = (to_cell.y1-to_cell.y2)/2+to_cell.y2
        otherxmid = (to_cell.x2-to_cell.x1)/2+to_cell.x1
        centerline = Line(Point(selfxmid,selfymid),Point(otherxmid,otherymid)) 
        if undo:
            self.win.draw_line(centerline,"white")
        else:
            self.win.draw_line(centerline,"red")