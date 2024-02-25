# need to pip install customtkinter

# the game will be run from this script
# this script will call the required functionalities from other scripts
# we will probably have a GameHandler.py that runs the gameloop when the runGame button is pressed, somehow need to display what is happening ingame? idk
# cpu player difficulty can be configured in settings (not implemented)

import customtkinter
import sys
import GameHandler

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("3000x700")



frame = customtkinter.CTkFrame(master=root)
frame.pack(fill="both", expand=True)
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight = 1)


gamename = customtkinter.CTkLabel(master=frame, text="MAHJONG BOT", font=("Times New Roman", 48))
gamename.grid(column = 1, row = 1, ipady = 30, ipadx = 10)

frame.grid_columnconfigure(2, weight=1)


def runGame():
    print("test") # run the game here
    GameHandler.run() # the game loop has to run inside here
    # game handler should just tell this outside whileoop what happens every turn step
    pass
playbutton = customtkinter.CTkButton(master = frame, text = 'START GAME', command = runGame, font=("Times New Roman", 24))
playbutton.grid(column = 1, row = 2, ipady = 10)
    
frame.grid_rowconfigure(3, minsize = 10)

def settings():
    print("access settings") # configure game settings here
    pass
settingsbutton = customtkinter.CTkButton(master = frame, text = 'SETTINGS', command = settings, font=("Times New Roman", 24))
settingsbutton.grid(column = 1, row = 4, ipady = 10, ipadx = 20)
    
frame.grid_rowconfigure(5, minsize = 10)

def exitGame():
    print("Exiting game...")
    root.destroy()
    sys.exit()
    pass
exitbutton = customtkinter.CTkButton(master = frame, text = 'QUIT', command = exitGame, font=("Times New Roman", 24))
exitbutton.grid(column = 1, row = 6, ipady = 10, ipadx = 20)

frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(7, weight = 1)


root.mainloop()