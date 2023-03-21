import tkinter as tk
import random 

class Game(tk.Tk) :
    """
    Class that creates game GUI.
    """
    
    colors = ['Black','Blue','Brown','Green','Orange','Pink','Purple','Red','Yellow']

    def __init__(self, timeLimit=20) :
        super().__init__()
        
        self._colors = Game.colors
        self._timer = timeLimit       
        self._score = 0               
        
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
        """
        Displays start and end screens.
        """
        self._msgLabel.config(text="Type in the COLOR of the word") 
        self._countdown()
        self._nextColor() 
        if self._timer == 0 :
            self._msgLabel.config(text="Game over! Please close window") 
            self._wordLabel.config(text="") 
            self._e.delete(0, tk.END)
        
    def _nextColor(self):
        """
        Moves onto next colors.
        """
        if self._timer > 0:
            self._e.focus_set()
            if self._e.get().lower() == self._colors[2].lower() :
                self._score += 1
            self._e.delete(0, tk.END)            
            random.shuffle(self._colors)
            self._wordLabel.config(fg = str(self._colors[2]), text = str(self._colors[0]))
            self._scoreLabel.config(text="Score: " + str(self._score)) 
            
    def _countdown(self):
        """
        Countdown for time limit.
        """
        if self._timer > 0:
            self._timer -= 1
            self._timeLabel.config(text = "Time left: "+ str(self._timer))
            self._timeLabel.after(1000, self._countdown)   

if __name__ == "__main__" :
    g = Game()           
    g.mainloop()         