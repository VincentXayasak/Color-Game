#Vincent Xayasak Lab 5
from game import Game
import csv
import re

class CustomGame(Game):
    """
    Class that allows user to play game and add a customized name + time limit.
    """
    SAVEFILE = "save.csv"

    def __init__(self):
        self._highscoreList = []
        try:
            with open(CustomGame.SAVEFILE) as f:
                reader = csv.reader(f)
                for l in reader:
                    self._highscoreList.append(l[0])
        except IOError:
            with open(CustomGame.SAVEFILE, "a") as f:
                f.write("0") #In case user initializes object, but decides to close program right away.
                self._highscoreList.append(0)
        self._name = input("Enter Your Name: ").strip()
        if self._name in self._highscoreList:
            print("Welcome Back "+self._name)
        else:
            print("Welcome to the game, "+self._name)
        self._timeLimit = input("Enter Time Limit (20-60s), Or Press Enter For 20s: ")
        self._timeLimit = self.check(self._timeLimit)
        super().__init__(int(self._timeLimit))
    
    def play(self):
        """
        Plays the game and stores data if score is greater or equal to high score. 
        """
        self.mainloop()
        nScore = round(self._score / float(self._timeLimit), 5)
        print("Your Score:",nScore)
        if nScore > float(self._highscoreList[0]):
            with open(CustomGame.SAVEFILE, "w") as f:
                f.write(str(nScore)+"\n")
                f.write(self._name+"\n")
            print("Congratulations! Your Name Is The First In The List Of Top Players")
            print("Top Players: "+self._name)
        elif nScore == float(self._highscoreList[0]):
            with open(CustomGame.SAVEFILE, "w") as f:
                f.write(str(nScore)+"\n")
                if not self._name in self._highscoreList[1:]:
                    f.write(self._name+"\n")
                for name in self._highscoreList[1:]:
                    f.write(name+"\n")
            print("Congratulations! Your Name Is Entered In The List Of Top Players")
            if not self._name in self._highscoreList[1:]:
                self._highscoreList.append(self._name)
            print("Top Players: "+", ".join(self._highscoreList[1:]))
        else:
            print("Good Game. Try Again To Beat The Best Score")
    
    def check(self, str):
        """
        Uses regex to check if user's entered crazy time limit string is valid. 
        """
        correct = False
        m = re.findall(r"-*\d*\.*\d+\.*\d*", str)
        if len(m) == 1:
            if re.search(r"\.{2}", m[0]) and len(re.findall(r"\d+", m[0])) == 1: 
                if re.search(r"\.", m[0]).start() != (re.search(r"\d", m[0]).start() - 1): 
                    m[0] = re.search(r"-*\d+", m[0]).group()
            if re.search(r"-{2}\d+", m[0]) and len(re.findall(r"\d+", m[0])) == 1: 
                m[0] = re.search(r"\d+", m[0]).group()
            try:
                if 20 <= int(m[0]) <= 60:
                    m[0] = re.search(r"\d+", m[0]).group()
                    correct = True
            except ValueError:
                correct = False
        if correct:
            print(m[0]+"s Time Limit")
            return int(m[0])
        print("Time Limit Not Entered, Using 20s Time Limit")
        return 20

CustomGame().play()