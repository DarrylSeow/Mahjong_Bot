"""
- This file defines the classes used for tiles and tile management for mahjong bot
- Not really meant to be run as a standalone script, but should be imported in the main game
"""
import random

# regular tiles
# wan, suo, tong suits, value goes from 1 to 9
class tile:
    def __init__(self, suit:str, value:int):
        self.suit = suit
        self.value = value

# for wind, dragon, flowers, animals (ttype)
# value is only used to specify flower tiles
class special_tile:
    def __init__(self, ttype:str, value=None, color=None ):
        if ttype.upper() == "FLOWER" or ttype.upper() == "ANIMAL" :
            if value == None or color == None:
                print("WARNING: Flower and animal tiles require a value and color!")
            else:
                self.value = value
                self.color = color # color is either 0 or 1
        self.ttype = ttype

# a tile_set object is made up of any number of tiles
# call tile_set.shuffle() to shuffle the tiles
class tile_set:
    def __init__(self, tile_list:list):
        self.tile_list = tile_list
        
    def shuffle(self): # shuffle the tiles in the tile_set. This directly alters the tile list.
        random.shuffle(self.tile_list)
        
    def topdraw(self): # draw from the top of the tile_list (topdeck a card), used when drawing from the maindeck
        return self.tile_list.pop(0) # remove the tile and return it
    
    def botdraw(self): # draw a tile from the bottom of the deck, used for special draws
        return self.tile_list.pop(-1)
    
    def multidraw(self, drawcount:int) -> list: # draws drawcount number of cards from the top of the deck
        returnlst = []    
        for i in range(drawcount):
            returnlst.append(self.topdraw())
        return returnlst
    
    def remove(self, tile_obj): # remove a specific tile from the list of tiles, used when throwing tiles
        for idx in range(len(self.tile_list)):
            item = self.tile_list[idx]

            if isinstance(tile_obj, tile) and isinstance(item, tile): # check if both are normal tiles
                if tile_obj.suit == item.suit and tile_obj.value == item.value: # if suit and value match, remove tile
                    return self.tile_list.pop(idx)
                
            elif isinstance(tile_obj, special_tile) and isinstance(item, special_tile):
                if tile_obj.ttype == item.ttype: # if ttype matches
                    if tile_obj.ttype.upper() == "FLOWER":
                        if tile_obj.value == item.value:
                            return self.tile_list.pop(idx)
                    return self.tile_list.pop(idx)
                
        print("Specified tile is not in this tile set!")
        return
    
    def add(self, tile_obj):
        if isinstance(tile_obj, tile) or isinstance(tile_obj, special_tile):
            self.tile_list.append(tile_obj)
        else:
            print("Only tiles can be added to tile sets!")
            

# generate a full set of mahjong tiles and store it in a "tile_set" object
def generate_tiles() -> tile_set:
    # create an empty tile_set
    all_tiles = tile_set([])
    
    for i in range(4): # bag size in mahjong is 4 only for most tiles
        # populate with regular tiles
        for val in range(1,10):
            for suits in (["wan", "suo", "tong"]):
                all_tiles.add(tile(suits, val))   
                
        # populate  wind tiles
        for wind in (["dong", "nan", "xi", "bei"]):
            all_tiles.add(special_tile(wind))
            
        # populate with dragon tiles
        for dragon in (["hongzhong", "facai", "baiban"]):
            all_tiles.add(special_tile(dragon))
            
    # populate with animal tiles
    for color in range(2):
        for val in range(1, 3):
            all_tiles.add(special_tile("animal", val, color))
            
    # populate with flower tiles
    for color in range(2):
        for val in range(1, 5):
            all_tiles.add(special_tile("flower", val, color))

    return all_tiles

# display a tile set
def display_tiles(tiles:tile_set):
    for tile in tiles.tile_list:
        try: # try print as if it was a normal tile
            print(tile.suit, tile.value)
        except:
            if tile.ttype.upper() != "FLOWER" and tile.ttype.upper() != "ANIMAL":
                print(tile.ttype)
            else:
                print(tile.ttype, tile.value, tile.color)




# for testing the functions, will not run if importing
if __name__ == "__main__":
    test = generate_tiles() # maindeck
    garbage_pool = tile_set([]) # garbage pool is where players throw their tiles each turn
    display_tiles(test)
    print ("########################")
    
    test.shuffle()
    display_tiles(test)
    print ("########################")
    
    testhand = tile_set(test.multidraw(13)) # because we shuffle before drawing, testhand should be random
    display_tiles(testhand)
    print ("########################")
    
    print(len(test.tile_list)) # we should have 148-13 = 135 tiles left in the test deck after drawing 1 testhand

