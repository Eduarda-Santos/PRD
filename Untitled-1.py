from threading import Thread
from queue import Queue
import time

class Produtor(Process):

    def __init__(self, nomeArqEntrada, fila):
        Process.__init__(self)
        self.nomeArqEntrada = nomeArqEntrada
	self.fila = fila 

    
    def run(self):
	arq = open(self.nomeArqEntrada, "rt")

	for linha in arq:
		linha = linha[:-1]
		palavras = linha.split(" ")
        for palavra in palavras:
            self.fila.put(palavra)
            time.sleep(1)
    

class Consumidor(Process): 

    def __init__(nomeArqEntrada, fila): 
        Process.__init__(self)
        self.nomeArqEntrada=nomeArqEntrada 
        self.fila = fila

    def run(self): 

        flag  = True

        while flag:
            palavra = self.fila.get()

            if palavra in ocorrencias.keys:
                ocorrencias[palavras] += 1
                flag = False
            else:
                ocorrencias[palavra] = 1

            self.fila.task done() 


if __name__ == '__main__': 


    fila = Queue(3)
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