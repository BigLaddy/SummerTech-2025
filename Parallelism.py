import multiprocessing
import time
def get(x):
    print("hello")
    time.sleep(1)
    print("I'm back")
    Pipe[0].send("Pipe")
    print(Pipe[0].recv())
def hey():
    for x in range(0,5):
        print("hey")
    print(Pipe[1].recv())
    Pipe[1].send("Sent")
Process = multiprocessing.Process(target = get,args = [])
Process2 = multiprocessing.Process(target = hey)
Pipe = multiprocessing.Pipe()

Process2.start()
Process.start()
