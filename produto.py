from _typeshed import Self


class Produto:

    def __init__(self, nome, descricao, preco):
        self.nome, self.descricao, self.preco = nome, descricao, preco

    def __str__(self):
        return f"nome:{self.nome}, descrição:{self.descricao}, preço:{self.preco}"

class ProdutoRepository:

    def __init__(self):
        self.lista = []

    def add(self, produto):
        self.lista.append(Produto)

    def busca(self, nome) -> Produto:
        for p in self.lista:
            if(p.nome == nome):
                return p

        return None

    def remove(self, nome) -> bool:
        p = self.busca(nome)

        if(p != None):
            self.lista.remove(p)
            return True
        return False

    def __str__(self) -> str:
        ret = "["

        for p in self.lista:
            ret += f"{p};"
        ret += "]"

        return ret

        

    