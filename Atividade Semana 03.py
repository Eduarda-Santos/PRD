from ast import Num, arg
import threading
from threading import Thread


def par():

    num = 1

    for num in range(num, num+9, 1):
        if(num%2 == 0):
            print(f"Número par: {num}")
    
def impar():

    num = 1

    for num in range(num, num+9, 1):
        if(num%2 != 0):
            print(f"Número impar: {num}")
        
if __name__ == "__main__":

    threads = []

    N = 1

    for i in range(N):
        thread  = Thread(target=par)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    par()

    for i in range(N):
        thread  = Thread(target=impar)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    impar()