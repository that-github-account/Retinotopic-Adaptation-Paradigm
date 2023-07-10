class Fixation_Dot(object):
    
    def __init__(self, WindowX, WindowY, visualdegree, size, speed):
        
        self.WindowX = WindowX
        self.WindowY = WindowY
        
        self.visualdegree = visualdegree
        self.size = size
        
        self.require_refixation = False
        
        self.colour = "#D21404"
        
        self.speed = speed
        
    def display(self):
        stroke(self.colour)
        fill(self.colour)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 2*self.size + 5, self.size/2)
        rect(self.xpos, self.ypos, self.size/2, 2*self.size + 5)
        
    def refixate(self, location):
        
        if location == "left":

            self.xpos = (self.WindowX/2 - self.visualdegree)
            self.ypos = self.WindowY/2
            
            self.require_refixation = False
            
        if location == "right":
        
            self.xpos = (self.WindowX/2 + self.visualdegree)
            self.ypos = self.WindowY/2

            self.require_refixation = False

        if location == "top":
        
            self.xpos = self.WindowX/2
            self.ypos = self.WindowY/2 - self.visualdegree
            
            self.require_refixation = False
            
    def move_fixation(self, location):
        
        if location == "right":
            
            if abs(self.WindowX/2 + self.visualdegree - self.xpos) > 0.001:
                self.xpos = self.xpos + self.speed
            else:
                self.require_refixation = False
                
        if location == "left":
            
            if abs(self.WindowX/2 - self.visualdegree - self.xpos) > 0.001:
                self.xpos = self.xpos - self.speed
            else:
                self.require_refixation = False
