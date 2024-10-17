class curve() :
    def __init__(self, color : tuple = (255,0,0) , points : list = []) -> object :
        
        self.color = color
        self.points = points
        
    def update(self,point,location) :
        self.points[location] = [point[0],point[1]]