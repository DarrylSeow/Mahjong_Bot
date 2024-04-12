"""
- This file defines the classes used for players and hand management for mahjong bot
- Not really meant to be run as a standalone script, but should be imported in the main game
"""
import TileHandler

class player:
    def __init__(self, wind:int, CPU:bool, hand:TileHandler.tile_set):
        self.hand = hand
        self.wind = wind
        self.points = 0 # players should only be initiated with zero points
        self.CPU = CPU
        self.turn_count = 0

    def show_hand(self):
        TileHandler.display_tiles(self.hand)
    
    def check_win(self, thrown_tile): # check if taking the thrown/drawn (zimuo) tile can give a win
        # I feel like this algo might be damn hard    
        pass
    
    def check_gang(self, thrown_tile): # check if this player can gang
        # sort the hand
        self.hand.sort_tiles(key="both")
        # iterate through the hand and see if there's a three of a kind match
        in_a_row = 0
        for tile in self.hand.tile_list:
            # if the one is a special tile and the other is a normal, don't even need to compare anymore
            if tile.ttype != thrown_tile.ttype:
                curr_tile = tile
                in_a_row = 0
                continue
            # for normal thrown tile
            if thrown_tile.ttype == "normal":
                if (tile.suit == thrown_tile.suit) and (tile.value == thrown_tile.value):
                    in_a_row += 1
                else:
                    curr_tile = tile
                    in_a_row = 0
            # for special thrown tile
            else:
                if tile.ttype == curr_tile.ttype:
                    in_a_row += 1
                else:
                    curr_tile = tile
                    in_a_row = 0
            if in_a_row == 3: # if at any point we find 3 in a row, corresponding to the thrown tile just return True
                return True
        return False # if we finish iterating through the entire hand and no 3 in a row was found, return False

    def check_pong(self, thrown_tile): # check if this player can pong
        # sort the hand
        self.hand.sort_tiles(key="both")
        # iterate through the hand and see if there's a three of a kind match
        in_a_row = 0
        for tile in self.hand.tile_list:
            # if the one is a special tile and the other is a normal, don't even need to compare anymore
            if tile.ttype != thrown_tile.ttype:
                curr_tile = tile
                in_a_row = 0
                continue
            # for normal thrown tile
            if thrown_tile.ttype == "normal":
                if (tile.suit == thrown_tile.suit) and (tile.value == thrown_tile.value):
                    in_a_row += 1
                else:
                    curr_tile = tile
                    in_a_row = 0
            # for special thrown tile
            else:
                if tile.ttype == curr_tile.ttype:
                    in_a_row += 1
                else:
                    curr_tile = tile
                    in_a_row = 0
            if in_a_row == 2: # if at any point we find 2 in a row, corresponding to the thrown tile just return True
                return True
        return False # if we finish iterating through the entire hand and no 2 in a row was found, return False
    
    def check_chi(self, thrown_tile): # check if this player can chi
        pass
    def player_turn(self, thrown_tile):
        pass
    
    def CPU_turn(self, thrown_tile:TileHandler.tile):
        # check if can win by taking the tile that was just thrown
        self.check_win(thrown_tile)
        # do something if can (prob just take the tile and hu)
        
        
        
        
    def turn(self, thrown_tile:TileHandler.tile): # call this function to activate taking a turn for a given player
        self.turn_count += 1
        if self.CPU:
            self.CPU_turn(thrown_tile)
        else:
            self.player_turn(thrown_tile)
    
# class turn:
#     def __init__(self):
#         self.