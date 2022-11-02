import sys
from types import prepare_class
from produto import Produto, ProdutoRepository
import random

nome = ["arroz", "feijao"]

def adicionaProduto{cadastro:ProdutoRepository, nome: str, descricao: str, preco: float}:

    p = Produto(nome, descricao, preco)
    cadastro.add(p)

def removePessoa(cadastro:ProdutoRepository, nome:str) -> bool:
    
    return cadastro.remove(nome)

def mostraMenu():
    print("1 - Cadastrar")
    print("2 - Buscar")
    print("3 - Listar")
    print("4 - Sair")

def produtos():
    lista = []
    for nome in nomes:
        descricao = random.