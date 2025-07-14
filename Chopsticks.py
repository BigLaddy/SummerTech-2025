class Values:
    def __init__(self):
        self.pl=1
        self.pr=1
        self.el=0
        self.er=0
        self.swaps = 0
    def Swap(self):
        X = self.pl
        self.pl = self.el
        self.el = X
        Y = self.pr
        self.pr = self.er
        self.er = Y
        self.swaps+=1
    def Combine(self):
        Con = True
        Total = self.pl + self.pr
        while Con == True:
            Left = int(input("What value would you like to use for the left hand?"))
            if Left == self.pl or Total - Left == self.pl or Left > 4 or Total - Left >4:
                print("Thats not valid")
                continue
            if input("That means that your right hand would have " + str(Total - Left) + " is that ok?")== "Yes":
                self.pl = Left
                self.pr = Total - Left
                Con = False
    def Attack(self):
        if input("Which hand would you like to use?") == "Left":
            AV = self.pl
        else:
            AV = self.pr
        if input("Which hand would you like to target?")=="Left":
            self.el += AV
        else:
            self.er += AV
        if self.er > 4:
            self. er = 0
        if self.el > 4:
            self.el = 0
    def CheckWin(self):
        if self.el == 0 and self.er == 0:
            if self.swaps %2 == 1:
                print("Player 2 Wins")
                quit()
            else:
                print("Player 1 Wins")
                quit()
    def Choice(self):
        if input("Would you like to attack or combine?") == "Attack":
            self.Attack()
        else:
            self.Combine()
    def Display(self):
        if self.swaps %2 == 1:
            print("Player 1:",self.el,self.er, "Player 2:",self.pl,self.er)
        else:
            print("Player 1:",self.pl,self.pr, "Player 2:",self.el,self.er)
Game = Values()
while True:
    Game.Display()
    Game.Choice()
    Game.CheckWin()
    Game.Swap()