# Imports
import pygame 
pygame.init()
import numpy as np
from axes import axes
from standing_wave_functions import *
from curve import curve
from button import Button


# Constants
BLACK   = (0,0,0)
WHITE   = (255,255,255)
RED     = (255,0,0)
PURPLE  = (218,177,218)

def main() -> None :
    
    # Define primary screen variables
    screen = pygame.display.set_mode((1024,1024))
    clock = pygame.time.Clock()
    running = True

    # Define physical string properties
    string_length   = 200
    string_elements = np.linspace(0,800,500)
    
    sinusoid_locked_ends    = curve(WHITE,[[] for _ in range(len(string_elements))])
    sinusoid_locked_end     = curve(RED,[[] for _ in range(len(string_elements))])
    sinusoid_unlocked_ends  = curve(PURPLE,[[] for _ in range(len(string_elements))])

    test = Button('test',list(PURPLE),100,100,[1024,0],10,lambda : None )
    test2 = Button('testing',list(PURPLE),100,100,[1024,0],10,lambda : None )

    # Create an axes
    main_axes = axes(screen,800,10,400,10) 

    # Screen loop
    while running : 
        
        # Event handling
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                
                running = False
                
                pygame.quit()
                
                exit()
            
            if event.type == pygame.KEYDOWN :
                
                if event.key == pygame.K_ESCAPE :
                    
                    running = False
                    
                    pygame.quit()
                    
                    exit()
                    
        
        # Logic steps
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] :
            axes.scale += 0.025
                
        if keys_pressed[pygame.K_DOWN] :
            axes.scale -= 0.025    
        
        # Update entities
        axes.update(main_axes)
        
        for i,x in enumerate(string_elements) : 
            
            t = pygame.time.get_ticks()/1000
            
            curve.update(sinusoid_locked_ends,[x,standing_wave_locked_ends(x,t,amplitude=200,order=1,string_length=string_length,wave_speed=100)],i)   
            
            curve.update(sinusoid_locked_end,[x,standing_wave_locked_end(x,t,amplitude=200,order=1,string_length=string_length,wave_speed=100)],i)   
            
            curve.update(sinusoid_unlocked_ends,[x,standing_wave_unlocked_ends(x,t,amplitude=200,order=1,string_length=string_length,wave_speed=100)],i)   
            
        for entity in Button.buttons : 
            entity.update()
            
        # Drawing
        screen.fill(BLACK)
        
        main_axes.draw(screen)
        
        main_axes.draw_to_axes_curve(screen,sinusoid_locked_ends)
        main_axes.draw_to_axes_curve(screen,sinusoid_locked_end)
        main_axes.draw_to_axes_curve(screen,sinusoid_unlocked_ends)
        
        for entity in Button.buttons :
            entity.draw(screen)
        
        pygame.display.flip()
        
        clock.tick(144)
    
if __name__ == "__main__" :
    main()