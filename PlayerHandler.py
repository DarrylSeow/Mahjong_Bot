"""
- This file defines the classes used for players and hand management for mahjong bot
- Not really meant to be run as a standalone script, but should be imported in the main game
"""
import TileHandler

class player:
    def __init__(self ,wind:int ,points:int, CPU:bool, hand = None):
        self.hand = hand
        self.wind = wind
        self.points = points
        self.CPU = CPU

    def show_hand(self):
        TileHandler.display_tiles(self.hand)