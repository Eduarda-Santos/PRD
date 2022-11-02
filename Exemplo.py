from multiprocessing import Process, Queue, current_process
import time 


class Produtor(Thread):

    def __init__(self,estoque):
        Thread.__init__(self)
        self.estoque=estoque 

    
    def produzir(self): 
        f = open('arquivo', 'r')
        palavras = []
        arquivo = palavras.split(" ")


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


    estoque = Queue(3)
    processos = []

    for i in range(3):
        processos.append(Consumidor(i,estoque))

    for i in range(2):
        processos.append(Produtor(i,estoque))

    for p in processos:
        p.start()

    for p in processos:
        p.join()
    

    print("program terminated")