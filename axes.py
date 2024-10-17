import pygame 
pygame.init()
import numpy as np

class axes() :
    
    scale : float = 1
    
    def __init__(self : object ,screen, x_length : float ,x_steps : float ,y_length : float ,y_steps : float, hat_length : float = 15, color : tuple = (255,255,255)) -> object :
        
        self.origin = (screen.get_width()*1/10,screen.get_height()/2)
        
        self.original_x_length = x_length
        self.original_y_length = y_length
        
        self.x_length   = x_length
        self.x_steps    = x_steps
        self.y_length   = y_length
        self.y_steps    = y_steps
        
        self.hat_length = hat_length
        
        self.color = color
        
    def draw(self : object, screen : object) -> None :  
           
        # x 
        pygame.draw.aaline(screen,self.color,(self.origin),(self.origin[0]+self.x_length,self.origin[1]))
        
        for i in range(self.x_steps) :
            pygame.draw.aaline(screen,self.color,
                               (i*np.floor(self.x_length/self.x_steps)+self.origin[0],self.origin[1]-3),
                               (i*np.floor(self.x_length/self.x_steps)+self.origin[0],self.origin[1]+3)
                               )
        
        # y 
        pygame.draw.aaline(screen,self.color,(self.origin),(self.origin[0],self.origin[1]-self.y_length))
        
        for i in range(self.y_steps) :
            pygame.draw.aaline(screen,self.color,
                               (self.origin[0]-3,-i*np.floor(self.y_length/self.y_steps)+self.origin[1]),
                               (self.origin[0]+3,-i*np.floor(self.y_length/self.y_steps)+self.origin[1])
                               )
        
    def update(self) -> None :
        # Scale
        self.x_length = self.original_x_length * axes.scale
        self.y_length = self.original_y_length * axes.scale    
        
    def draw_to_axes_curve(self : object, screen , curve : object) -> None :
        
        # Scale
        curve.points = [[a*axes.scale,b*axes.scale] for a,b in curve.points]
        # Translate
        curve.points = [[a+self.origin[0],(self.origin[1]-b)] for a,b in curve.points]
        
        try : 
            pygame.draw.aalines(
                screen,
                curve.color,
                closed=False,
                points=curve.points
            )
        except : 
            print("~Not a curve~ (?)")