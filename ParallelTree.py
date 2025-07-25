import multiprocessing
def do ():
    print("I did")
def spawn(amount):
    if amount >= 2:
        if amount%2 ==1:
            x = (amount-1)/2
            Process = multiprocessing.Process(target = spawn,args = [x])
            Process2 = multiprocessing.Process(target = spawn,args = [x+1])
        else:
            
            Process = multiprocessing.Process(target = spawn,args = [amount/2])
            Process2 = multiprocessing.Process(target = spawn,args = [amount/2])
        Process.start()
        Process2.start()
    else:
        do()

Process = multiprocessing.Process(target = spawn,args = [7])
Process.start()