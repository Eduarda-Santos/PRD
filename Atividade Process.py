from multiprocessing import Process, Queue, current_process
import time 


class Produtor(Process):

    def __init__(self,estoque):
        Process.__init__(self)
        self.estoque=estoque 

    
    def produzir(self):
        print("Lendo {self.i} arquivo...")
        f = open('arquivo', 'r')
        print("Lendo {self.i} arquivo... {item}")
        palavras = []
        arquivo = palavras.split(",")


    def run(self): 
        while True:
            self.produzir() 

class Consumidor(Process): 

    def __init__(self,i,estoque): 
        Process.__init__(self) 
        self.estoque=estoque 
        self.i=i 

    def consumir(self): 
        print("Escrevendo {}...".format(self.i))
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