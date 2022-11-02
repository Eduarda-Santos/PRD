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
        self.nomeArqEntrada.put("!FIM!")
        arq.close()
        print('FIM')

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

            if (palavra == "!FIM!"):
                flag = False
            else:
                if palavra in ocorrencias:
                    ocorrencias[palavra] += 1
                else:
                    ocorrencias[palavra] = 1
                    self.fila.task done()

        file = open(self.fila, 'wt', , enconding='utf-8')

        file.write(str(ocorrencias))
        file.close()

if __name__ == '__main__':
    for i in range(10):
        duration = time.time()
    
        fila = Queue(4)
        produtor = Produtor("dicionario.txt", fila)
        produtor.start()

        consumidor = Consumidor("saida.txt", fila)
        consumidor.start()

        produtor.join()
        consumidor.join()

        duration = time.time() - duration
    
        with open('tempos.txt', 'a+', encoding='utf-8') as file:
        file.write(f'Tempo com (Thread): {duration}\n')
        if(i == 9):
            file.write(f'FIM\n')
        print('Finalizado!')

