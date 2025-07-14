class Values:
    def __init__(self,P1L,P1R,P2L,P2R):
        self.P1L = P1L
        self.P1R = P1R
        self.P2L = P2L
        self.P2R = P2R
    def Combine(self,Turn):
        if Turn == 1:
            Total = self.P1L + self.P1R
            x = self.P1L
            Left = Total
            Right = 0
        elif Turn == 2:
            Total = self.P2L + self.P1R
            x = self.P2L
            Left = Total
            Right = 0
            if Total >4:
                Left = Total-(Total-4)
                Right = Right + Total-4
                print(Left,Right)
        for Amount in range(0,Total):
            if Left == x or Right == x:
                 Left-=1
                 Right+=1
            print(Left,Right)
            Answer=input("Would you like this combination?")
            if Answer == "Yes":
                if Turn == 1:
                    self.P1L = Left
                    self.P1R = Right
                    print(self.P1L,self.P1R,"These are the new values")
                if Turn == 2:
                    self.P2L = Left
                    self.P2R = Right
                    print(self.P2L,self.P2R,"These are the new values")
            else:
                Left-=1
                Right+=1
                


Values(1,1,1,1)
Player1Left=1
Player2Left=1
Player1Right=1
Player2Right=1

def Combine(x,y):
    Total = x + y
    Left = Total
    Right = 0
    if Total >4:
            Left = Total-(Total-4)
            Right = Right + Total-4
            print(Left,Right)
    for Amount in range(0,Total):
            if Left == x and Right == y:
                 Left-=1
                 Right+=1
            print(Left,Right)
            Answer=input("Would you like this combination?")
            if Answer == "Yes":
                ReturnableList=[Left,Right]
                return ReturnableList
            else:
                Left-=1
                Right+=1
                if Right > 4:
                    print("There is no longer a valid choice")
                    return [x,y]
    Combine(x,y)

def Attack(PLeft,PRight,ELeft,ERight,Turn):
    if Turn == 2:
        x=ELeft
        ELeft = PLeft
        PLeft=x 
        y=ERight
        ERight = PRight
        PRight=y 
    UsedHand=input("Would you like to use your left or right hand?")
    if UsedHand == "Left":
        AttackValue = PLeft
    else:
         AttackValue = PRight
    Target = input("Would you like to attack their left or right hand?")
    if Target =="Left":
        ELeft += AttackValue
        if ELeft > 4:
            ELeft = 0
        if Turn == 2:
            return [ELeft,ERight,PLeft,PRight]
        return[PLeft,PRight,ELeft,ERight]
    else:
        ERight += AttackValue
        if ERight > 4:
            ERight = 0
        if Turn == 2:
            return [ELeft,ERight,PLeft,PRight]
        return[PLeft,PRight,ELeft,ERight]
    
def Choice(P1L,P1R,P2L,P2R,Turn):
     if Turn == 1:
        Choice = input("Would you like to attack or combine?" )
        if Choice == "Attack":
            return Attack(P1L,P1R,P2L,P2R,1)
        if Choice == "Combine":
            List = Combine(P1L,P1R)
            List.append(P2L)
            List.append(P2R)
            return List
     if Turn == 2:
        Choice = input("Would you like to attack or combine?" )
        if Choice == "Attack":
            return Attack(P1L,P1R,P2L,P2R,2)
        if Choice == "Combine":
            List = Combine(P2L,P2R)
            List.insert(0,P1L)
            List.insert(1,P1R)
            return List
        
def CheckWin(P1L,P1R,P2L,P2R):
    if P1L == 0 and P1R == 0:
        return "P2Win"
    elif P2L == 0 and P2R == 0:
        return "P1Win"
    else:
        return "NoWin"

PlayerValues = (Choice(Player1Left,Player1Right,Player2Left,Player2Right,1))
print(PlayerValues)
while CheckWin(PlayerValues[0],PlayerValues[1],PlayerValues[2],PlayerValues[3]) == "NoWin":
    PlayerValues = (Choice(PlayerValues[0],PlayerValues[1],PlayerValues[2],PlayerValues[3],2))
    print(PlayerValues)
    if CheckWin(PlayerValues[0],PlayerValues[1],PlayerValues[2],PlayerValues[3]) !="NoWin":
        print(CheckWin(PlayerValues[0],PlayerValues[1],PlayerValues[2],PlayerValues[3]))
        continue
    PlayerValues = (Choice(PlayerValues[0],PlayerValues[1],PlayerValues[2],PlayerValues[3],1))
    print(PlayerValues)
    if CheckWin(PlayerValues[0],PlayerValues[1],PlayerValues[2],PlayerValues[3]) !="NoWin":
        print(CheckWin(PlayerValues[0],PlayerValues[1],PlayerValues[2],PlayerValues[3]))
        continue