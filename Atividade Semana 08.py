from concurrent.futures import process
from multiprocessing import Process, Queue
from operator import contains
import time
import random

class MineradorCarvao(Process):

    def __init__(self, num, balde):
        Process.__init__(self)
        self.num = num
        self.balde = balde

    def run(self):
        while True:
            while estoque <= 20:
                time.sleep(3)
                carvao = random.randint(1,3)
                self.balde.put(carvao)
                estoque = estoque + carvao
                trabalhador = random.randint(1,2)
                self.trabalhador = trabalhador

                if trabalhador == 2:
                    carvao = random.randint(1,3)
                    self.balde.put(carvao)
                    estoque = estoque + carvao

                print(f"Mineradores {self.num} produziu {carvao}")
                
                
class MineradorFerro(Process):

    def __init__(self, num, container):
        Process.__init__(self)
        self.num = num
        self.container = container

    def run(self):
        while True:
            while estoquemin <= 10:
                time.sleep(5)
                minerio = random.randint(0,2)
                self.container.put(minerio)
                estoquemin = estoquemin + minerio
                print(f"Trabalhador {self.num} produziu {minerio}")
                trabalhador = random.randint(1,2)
                self.trabalhador = trabalhador

                if trabalhador == 2:
                    minerio = random.randint(1,3)
                    self.container.put(minerio)
                    estoquemin = estoquemin + minerio

                print(f"Mineradores {self.num} produziu {minerio}")

class Benificiador(Process):

    def __init__(self, num):
        Process.__init__(self)
        self.num = num

    def run(self):
        while True:
            estoquemin = self.estoquemin.get()
            estoque = self.estoque.get()

            if estoque >= 10 and estoquemin >= 5:
                time.sleep(8)
                lingote = lingote + 1
                print(f"Mineradores {self.num} produziu {lingote}")
    
class Fereiro(Process):

    def __init__(self, num):
        Process.__init__(self)
        self.num = num

    def run(self):
        while True:
            lingote = self.lingote.get()
            estoque = self.estoque.get()

            if estoque >= 10 and lingote >= 3:
                time.sleep(10)
                espada = espada + 1
                print(f"Mineradores {self.num} produziu {espada}")


if __name__ == '__main__':

    N = 1
    processos = []
    fila = Queue(N)

    for i in range(N):
        processos.append(MineradorCarvao,fila)
        processos.append(MineradorFerro,fila)
        processos.append(Benificiador,fila)
        processos.append(Fereiro,fila)
    
    for p in processos:
        p.start()

    print('Terminou..')