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
        no = No(valor, prioridade)
        if self.is_full():
            raise Exception("Lista de prioridade atingiu seu limite!")

        elif self.is_empty():
            self.__inicio = no
        
        elif prioridade > self.__inicio.prioridade:
            no.prox = self.__inicio
            self.__inicio = no

        else:    
            pointer = self.__inicio
            while pointer.prox and prioridade <= pointer.prox.prioridade:
                pointer = pointer.prox

            no.prox = pointer.prox
            pointer.prox = no

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
       nova_lista = []
       if self.is_empty():
        print("A fila de prioridade,no momento,está vazia")
        return nova_lista
       itens = []
       no_atual = self.__inicio
       while no_atual is not None:
            itens.append((no_atual.dado, no_atual.prioridade))
            no_atual = no_atual.prox

       for item in itens:
            print(item)

       return itens

         

    

    # retorna a quantidade de elementos na fila de prioridade
    # se a fila de prioridade estiver vazia, retorna ZERO
    def size(self) -> int:
        return self.__qtdItens