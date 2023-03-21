# Lab 5 Superclass for a color identifcation game

# The user gets a GUI window for the color identificaton game
#  - the user presses the Enter key to start the game
#  - in the game: a word shows up with a certain color
#  -              the user types in the color of the word
#  - the user has 30s to type in as many correct colors as possible
#  - when the 30s time is up, the user gets a score of correct
#    color identifications


import tkinter as tk
import random 

class Game(tk.Tk) :
    ''' color identification game: type in as many correct colors as possible within a time'''
    
    colors = ['Black','Blue','Brown','Green','Orange','Pink','Purple','Red','Yellow']

    def __init__(self, timeLimit=30) :
        super().__init__()
        
        self._colors = Game.colors
        self._timer = timeLimit       # default time limit is 30s
        self._score = 0               # user score
        
        self.title("COLOR IDENTIFIER")
        self.geometry("300x275")      
        self._scoreLabel = tk.Label(self, text="   Press ENTER key to start", 
                                    font=('Arial', 14))  
        self._scoreLabel.grid(pady=10)
        self._timeLabel = tk.Label(self, text="Time left: "+str(self._timer)+"s", 
                                   font=('Arial', 14)) 				
        self._timeLabel.grid(pady=10) 
        self._msgLabel = tk.Label(self, text="", font=('Arial', 14))
        self._msgLabel.grid(pady=10)       
        self._wordLabel = tk.Label(self, font = ('Arial', 30)) 
        self._wordLabel.grid(pady=10) 
        self._e = tk.Entry(self) 
        self._e.grid(pady=20)
        self.bind('<Return>', self._startGame)    
        
    def _startGame(self, event):
        self._msgLabel.config(text="Type in the COLOR of the word") 
        self._countdown()
        self._nextColor() 
        if self._timer == 0 :
            self._msgLabel.config(text="Game over! Please close window") 
            self._wordLabel.config(text="") 
            self._e.delete(0, tk.END)
        
    def _nextColor(self):
        if self._timer > 0:
            self._e.focus_set()
            if self._e.get().lower() == self._colors[2].lower() :
                self._score += 1
            self._e.delete(0, tk.END)            
            random.shuffle(self._colors)
            self._wordLabel.config(fg = str(self._colors[2]), text = str(self._colors[0]))
            self._scoreLabel.config(text="Score: " + str(self._score)) 
            
    def _countdown(self):
        if self._timer > 0:
            self._timer -= 1
            self._timeLabel.config(text = "Time left: "+ str(self._timer))
            self._timeLabel.after(1000, self._countdown)   


# unit test to see how the game is played
if __name__ == "__main__" :
    g = Game()           # create Game object
    g.mainloop()         # run the game