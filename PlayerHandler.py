"""
- This file defines the classes used for players and hand management for mahjong bot
- Not really meant to be run as a standalone script, but should be imported in the main game
"""

class player:
    def __init__(self ,hand:list ,wind:int ,points:int):
        
        self.hand = hand
        self.wind = wind
        self.points = points

    def show_hand():
        print(self.hand)