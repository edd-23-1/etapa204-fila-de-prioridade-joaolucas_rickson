# -*- coding:UTF-8 -*-
from no import No

class FilaPrioridade:
    """
    Implementação de Fila de Prioridade com Capacidade
    A fila de prioridade a ser implementada deverá ser em ordem crescente
    Os itens com maior prioridade devem ocupar as primeiras posições
    Itens com prioridades iguais devem ser ordenados conforme ordem de inserção
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Fila de Prioridade com capacidade: {capacidade}")


    # Retorna True se a fila de prioridade está vazia, False caso contrário
    def is_empty(self) -> bool:
       if self.__qtdItens == 0:
           return True
       else:
        return False
    
    # retorna True se a fila de prioridade está cheia, False caso contrário
    def is_full(self) -> bool:
       if self.__qtdItens >= self.__capacidade:
           return True
       return False


    # Retorna uma referência para o primeiro item da fila de prioridade
    # Caso a lista esteja vazia, retorna None
    def first(self) -> No:
        if self.is_empty():
            return None
        else:
            return self.__inicio


    # insere um item na fila de prioridade e retorna True, se o item for inserido
    # se a fila de prioridade estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
    def add(self, valor, prioridade) -> bool:
       novo_no = No(valor,prioridade)
       if self.is_full():
            raise Exception("A capacidade fila de prioridade foi atingida.")
       if self.is_empty():
            self.__inicio = novo_no
            self.__qtdItens += 1
            return True

       no_anterior = None
       no_atual = self.__inicio
       while no_atual is not None and no_atual.prioridade <= prioridade:
            no_anterior = no_atual
            no_atual = no_atual.prox

       if no_anterior is None:
            novo_no.prox = self.__inicio
            self.__inicio = novo_no
       else:
            novo_no.prox = no_atual
            no_anterior.prox = novo_no

       self.__qtdItens += 1
       return True
    
    # remove o primeiro item da fila de prioridade, caso não esteja vazia, e retorna o Nó
    # se a fila de prioridade estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove(self) -> No:
        if self.is_empty():
            raise Exception("A fila de prioridade está vazia.")
        primeiro_no = self.__inicio
        self.__inicio = primeiro_no.prox
        primeiro_no.prox = None
        self.__qtdItens -= 1
        return primeiro_no


    # retorna uma lista de tuplas com os itens (valor e prioridade) da fila de prioridade 
    # imprime os itens da fila de prioridade do primeiro para o último
    # caso a fila de prioridade esteja vazia, imprime uma mensagem informando
    # que a fila de prioridade está vazia e retorna uma lista vazia
    def display(self) -> list[tuple()]:
       pass
    

    # retorna a quantidade de elementos na fila de prioridade
    # se a fila de prioridade estiver vazia, retorna ZERO
    def size(self) -> int:
        return self.__qtdItens