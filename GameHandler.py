from PlayerHandler import player
import TileHandler
import random

def next_winds(player_list):
    for player in player_list:
        player.wind = (player.wind+1)%4

# # choose initial dealer
# def choose_dealer():
#     return random.randint(0,3)

# return an integer of who won (-1 if nobody won)
def check_victory():
    return -1

def run():
    # do set up 
    
    # generate players
    turnorder = [0,1,2,3]
    random.shuffle(turnorder)
    human = player(turnorder[0], points=0, CPU=False)
    CPU1 = player(turnorder[1], points=0, CPU=True)
    CPU2 = player(turnorder[2], points=0, CPU=True)
    CPU3 = player(turnorder[3], points=0, CPU=True)

    player_list = [human, CPU1, CPU2, CPU3]
    end = False
    
    # each iteration of this loop is one round
    counter = 0
    while not end:
        global_wind = counter//4
        # generate tiles and shuffle
        all_tiles = TileHandler.generate_tiles()
        all_tiles.shuffle()
        player_list = sorted(player_list, key=lambda player: player.wind)
        for gamer in player_list:
            match gamer.wind:
                case 0:
                    gamer.hand = TileHandler.tile_set(all_tiles.multidraw(14))
                case _:
                    gamer.hand = TileHandler.tile_set(all_tiles.multidraw(13))
 
        victory = -1 # has someone won this round?
        # turn = 0 # who's turn now
        numturn = 0
        while victory < 0:
            # run each round
            # each iteration is one turn
            turn = numturn%4 # who's turn now
            match turn:
                case human.wind:
                    # do human turn
                    # draw, check_victory, throw if no win
                    pass
                case CPU1.wind:
                    # do cpu turn
                    pass
                case CPU2.wind:
                    # do cpu turn
                    pass
                case CPU3.wind:
                    # do cpu turn
                    pass
                case _:
                    print('DEVAX')
            # pong/chi
            victory = check_victory()
            numturn += 1
            
        # add points to victorious player only, based on their hand
        match victory:
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
        if victory > 0:
            counter += 1
            player_list = next_winds(player_list)
        print(counter, global_wind)
        if counter == 16:
            end = True
        
        
        
    
if __name__ == "__main__":
    run()