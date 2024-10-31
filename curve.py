class curve() :
    def __init__(self, color : tuple = (255,0,0) , points : list = []) -> object :
        
        self.color = color
        self.points = points
        
    def update(self,point,location) :
        self.points[location] = [point[0],point[1]]
        
    def superposition(self : object , other : object) -> object :
        return curve(self.color,[[a[0],a[1]+b[1]] for a,b in zip(self.points,other.points)])