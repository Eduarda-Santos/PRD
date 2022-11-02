from threading import Thread 
from queue import Queue 
import time 
import random 


class Produtor(Thread):

    def __init__(self,estoque):
        Thread.__init__(self)
        self.estoque=estoque 

    
    def produzir(self): 
        print("Produzindo adquirindo...")
        item=random.randint(1,1000)
        self.estoque.put(item)
        time.sleep(1)

    def run(self): 
        while True:
            self.produzir() 

class Consumidor(Thread): 

    def __init__(self,i,estoque): 
        Thread.__init__(self) 
        self.estoque=estoque 
        self.i=i 

    def consumir(self): 
        print("Consumir {} aguardando...".format(self.i)) 
        item=self.estoque.get() 
        self.estoque.task_done() 
        print("Consumidor {} consumindo...".format(self.i))
        time.sleep(5) 
        print("Consumindo {} item {}".format(self.i,item)) 

    def run(self): 
        while True: 
            self.consumir() 


if __name__ == '__main__': 


    estoque = Queue(5)


    p = Produtor(estoque) 
    c1 = Consumidor(1,estoque) 
    c2 = Consumidor(2,estoque) 
    c3 = Consumidor(3,estoque) 

    

    c1.start() 
    c2.start() 
    c3.start()

    p.start() 


    c1.join() 
    c2.join() 
    c3.join()

    p.join()

    

    print("program terminated") 

    