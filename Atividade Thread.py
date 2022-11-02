from threading import Thread 
from queue import Queue 
import time


class Produtor(Thread):

    def __init__(self,estoque):
        Thread.__init__(self)
        self.estoque=estoque 

    
    def produzir(self): 
        print("Produzindo lendo...")
        f = open('arquivo', 'r')
        palavras = []
        arquivo = palavras.split(",")
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
        print("Escrevendo {} ...".format(self.i)) 
        time.sleep(5)
        palavras = []
        for j in range():
            if palavras[j] == (" "):
                f = open('ocorrencias', 'w')
                cont = cont + 1
                self.estoque.put(cont)

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