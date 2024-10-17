import numpy as np

def standing_wave_locked_ends(x : float , t : float , amplitude : float , order : int , string_length : float , wave_speed : float) -> float :

    # wavelength = 2 * L / n 

    k = order * np.pi / string_length
    
    return amplitude * np.sin(k*x) * np.sin(k*wave_speed*t) 

def standing_wave_locked_end(x : float , t : float , amplitude : float , order : int , string_length : float , wave_speed : float) -> float:
    
    # wavelength = 4L / (2n-1)
    
    k = ((2*order-1) * np.pi) / (2 * string_length)
    
    return amplitude * np.sin(k*x) * np.sin(k*wave_speed*t)

def standing_wave_unlocked_ends(x : float , t : float , amplitude : float , order : int , string_length : float , wave_speed : float) -> float :
    
    # wavelength = 2 * L / n (but out of phase by pi/2)
    
    k = order * np.pi / string_length
    
    return amplitude * np.cos(k*x)*np.sin(k*wave_speed*t)