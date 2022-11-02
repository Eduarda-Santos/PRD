from threading import Thread
from queue import Queue
import time

class Produtor(Thread):

    def __init__(self, nomeArqEntrada, fila):
        Thread.__init__(self)
        self.nomeArqEntrada = nomeArqEntrada
        self.fila = fila
        
    def run(self):
        arq = open(self.nomeArqEntrada, "rt")

        for linha in arq:
            linha = linha[:-1]
            palavras = linha.slipt(" ")
            for palavra in palavras:
                self.fila.put(palavra)
                time.sleep(1)

class Consumidor(Thread):

    def __init__(nomeArqSaida, fila):
        Thread.__init__(self)
        self.nomeArqSala = nomeArqSaida
        self.fila = fila

    def run(self):

        flag = True

        ocorrencias={}

        while flag:
            palavra = self.fila.get()

            if palavra in ocorrencias.keys:
                ocorrencias[palavra] += 1
                flag = False
            else:
                ocorrencias[palavra] = 1

            self.fila.task done()



if __name__ == '__main__':
    fila = Queue(4)
    produtor = Produtor("teste.txt", fila)
    produtor.start()

    consumidor = Consumidor("saida.txt", fila)
    consumidor.start()

    produtor.join()
    consumidor.join()

