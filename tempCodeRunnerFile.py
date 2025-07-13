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