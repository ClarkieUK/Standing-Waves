import pygame 
pygame.init()

class Button() :
    
    font = pygame.font.SysFont('didot.ttc', 36)
    buttons = []
    padding = 10
    ## NEED TO FINISH PADDING LOGIC - GOOD LUCK SOLDIER!
    i = 0
    def __init__(self,text,color : list,width,height,pos,depth,function : callable) :
        # Logic
        Button.buttons.append(self)
        self.clicked = False
        self.logged_click_position = False
        self.depth = depth
        self.color = color
        self.width = width
        self.function = function
        
        total_x_distance = 0
        
        for i in range(len(Button.buttons)) :
            total_x_distance -= (Button.buttons[i].width + (1) * Button.padding)
            
        pos[0] += total_x_distance  
        pos[1] += Button.padding    
        
        self.origin = pos
        self.loose_origin = pos
        
        # Top Rectangle
        self.top_rectangle = pygame.Rect((self.loose_origin),(width,height))
        self.top_color = color
        
        # Bottom Rectangle
        self.bottom_rectangle = pygame.Rect((pos[0],pos[1]+self.depth),(width,height))
        self.bottom_color = [x - 10 for x in color]
    
        # Text
        self.text_surface = Button.font.render(text,1,'#FFFFFF')
        self.text_rectangle = self.text_surface.get_rect(center = self.top_rectangle.center)
        
    def draw(self,surface) :
        
        pygame.draw.rect(surface,self.bottom_color,self.bottom_rectangle,border_radius=12)
        pygame.draw.rect(surface,self.top_color,self.top_rectangle,border_radius=12)
        surface.blit(self.text_surface,self.text_rectangle)
        
    def update(self) :
        
        mouse_position = pygame.mouse.get_pos()
        
        if self.top_rectangle.collidepoint(mouse_position) :
            self.top_color = [x + 20 for x in self.color]
        else :
            self.top_color = self.color
            x,y = self.origin
            self.top_rectangle[1] = y 
            self.text_rectangle = self.text_surface.get_rect(center = self.top_rectangle.center)
        
        if pygame.mouse.get_pressed()[0] :
            if not self.logged_click_position :
                self.clicked_initial_position = pygame.mouse.get_pos()
                self.logged_click_position = True

            if self.top_rectangle.collidepoint(mouse_position) and self.top_rectangle.collidepoint(self.clicked_initial_position) :      
                
                if pygame.mouse.get_pressed()[0] and self.clicked == False : 
                    self.clicked = True
                    self.top_rectangle[1] += (self.depth)/2
                    self.text_rectangle[1] += (self.depth)/2
                    # Do operation
                    self.function()
                    
        if not pygame.mouse.get_pressed()[0] :
            self.logged_click_position = False 
            self.clicked = False   
            self.top_rectangle[1] = self.origin[1]
            self.text_rectangle = self.text_surface.get_rect(center = self.top_rectangle.center)