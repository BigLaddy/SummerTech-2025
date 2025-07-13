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


def Attack(PLeft,PRight,ELeft,ERight):
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
        return[PLeft,PRight,ELeft,ERight]
    else:
        ERight += AttackValue
        if ERight > 4:
            ERight = 0
        return[PLeft,PRight,ELeft,ERight]
    

def Choice(P1L,P1R,P2L,P2R,Turn):
     if Turn == 1:
        Choice = input("Would you like to attack or combine?" )
        if Choice == "Attack":
            return Attack(P1L,P1R,P2L,P2R)
        if Choice == "Combine":
            List = Combine(P1L,P1R)
            List.append(P2L)
            List.append(P2R)
            return List
     if Turn == 2:
        Choice = input("Would you like to attack or combine?" )
        if Choice == "Attack":
            return Attack(P1L,P1R,P2L,P2R)
        if Choice == "Combine":
            List = Combine(P1L,P1R)
            List.append(P2L)
            List.append(P2R)
            return List
          


print(Choice(Player1Left,Player1Right,Player2Left,Player2Left))


        
        































































































































