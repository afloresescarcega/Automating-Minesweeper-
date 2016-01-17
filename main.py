#!/usr/bin/env python

"""
This is the main file. The script finds the game window and sets up the 
coordinates for each block.


The MIT License (MIT) 
(c) 2016
"""

import pyautogui, logging, time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

# logging.disable(logging.DEBUG) # uncomment to block debug log messages

__author__ = "Alex Flores Escarcega"
__copyright__ = "Copyright 2007, Alex Flores Escarcega"
__credits__ = ["Alex Flores Escarcega"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Alex Flores Escarcega"
__email__ = "alex.floresescar@gmail.com"
__status__ = "Development"

def find_game_region():
    """
    Uses image inactive_window.png to find the coordinates of the game
    Inputs: None
    Outputs: the tuple of the coordinates of the game window
    """
    logging.debug("About to take a screenshot and look for inactive_window.png")
    coors = pyautogui.locateOnScreen("images/inactive_window.png")
    if coors is None:
        logging.debug("Did not find inactive_window.png")
        logging.debug("Maybe the window is active instead. Will look for active_window.png")
        coors = pyauto.locateOnscreen("images/inactive_window.png")
        if coors is None:
            raise Exception("The game as not found on this screen. Make sure it is visible.")
    return (coors[0],coors[1])

def main():
    """
    No inputs
    No outputs
    Starts up the gameregionfinder
    """




if __name__ == "__main__":
        main()
