class Collision(object):
    
    def __init__(self, angle, distance, size, WindowX, WindowY, visualdegree):
        self.angle = angle
        self.distance = distance
        self.size = size
        self.WindowX = WindowX
        self.WindowY = WindowY
        
        self.visualdegree = visualdegree
    
        self.radian = radians(self.angle)
        self.condition = 1
        
        self.showAB = False
    
    def reposition(self, locationX, stimuli_fixation_relative_location, locationY, angle, overlap, iterations):
        
        self.overlap = overlap
        self.sfrl = stimuli_fixation_relative_location
        
        self.angle = angle
        self.radian = radians(angle)
        
        self.iterations = iterations
        
        if self.sfrl == "left":
            
            self.CenterX = locationX - self.visualdegree
            self.CenterY = locationY
            
        if self.sfrl == "right":
            
            self.CenterX = locationX + self.visualdegree
            self.CenterY = locationY
            
        if self.sfrl == "override; adaptation":
            
            self.CenterX = self.WindowX/2
            self.CenterY = self.WindowY/2
        
        self.StartX = self.CenterX - cos(self.radian)*self.distance
        self.StartY = self.CenterY + sin(self.radian)*self.distance
        
        self.EndX = self.CenterX + cos(self.radian)*self.distance
        self.EndY = self.CenterY - sin(self.radian)*self.distance
        
        self.Ax = self.StartX - cos(self.radian)*self.size
        self.Ay = self.StartY + sin(self.radian)*self.size
        
        self.Bx = self.CenterX - cos(self.radian)*((self.size)*(self.overlap))
        self.By = self.CenterY + sin(self.radian)*((self.size)*(self.overlap))
        
        self.repositioned = True
    
    def require_repositioning(self):
        
        self.repositioned = True
    
    def display(self):
        
        stroke(128)
        fill(128)
        ellipseMode(CENTER)
        
        ellipse(self.Ax, self.Ay, self.size, self.size)
        ellipse(self.Bx, self.By, self.size, self.size)
        
        if self.showAB == True:
            fill(255)
            textSize(25)
            textMode(CENTER)
            text("A", self.Ax - self.size/2 - 10, self.Ay - self.size/2)            
            text("B", self.Bx - self.size/2 - 10, self.By - self.size/2)
        
    def moveCenter(self, speed):
        
        if self.condition == 1:            
            distanceX = abs(self.Ax - (self.CenterX - cos(self.radian)*((self.size)*(1))))
            distanceY = abs(self.Ay - (self.CenterY + sin(self.radian)*((self.size)*(1))))
            
            if distanceX > 0.001 or distanceY > 0.001:
                self.Ax = self.Ax + cos(self.radian)*speed
                self.Ay = self.Ay - sin(self.radian)*speed
            else:
                self.condition = 2
    
    def moveEnd(self, speed):
        
        if self.condition == 2:
            distanceX = abs(self.Bx - self.EndX)
            overX = self.size*abs(cos(self.radian))*(self.overlap)
            distanceY = abs(self.By - self.EndY) 
            overY = self.size*abs(sin(self.radian))*(self.overlap)
            
            if distanceX > (0.001 + overX) or distanceY > (0.001 + overY):
                self.Bx = self.Bx + cos(self.radian)*speed
                self.By = self.By - sin(self.radian)*speed
            else:
                self.condition = 3
    
    def moveStart(self):
        
        if self.condition == 3:
            
            if self.iterations > 0:
                self.condition = 1
                self.iterations = self.iterations - 1
                    

    def moveFull(self, speed):
        self.moveCenter(speed)
        self.moveEnd(speed)
                
    def single_iteration(self, speed):
        self.display()
        self.moveFull(speed)
        self.moveStart()
        
        

        
        
