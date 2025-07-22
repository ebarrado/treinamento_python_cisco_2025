
lista = [1,23,4,5,6,7,8,9,10]
print(len(lista), " elementos") # Imprimindo o tamanho da lista

#método de acesso
lista.append(6) # inserir um valor na lista no final
print(lista) # Imprimindo a lista após a inserção

print(lista.pop()) # remove o último elemento da lista e o imprime
print(lista) # Imprimindo a lista após a remoção do último elemento

lista.insert(0, 44) # inserir um valor na lista na posição 0
print(lista) # Imprimindo a lista após a inserção na posição 0

print(lista.clear()) # limpa a lista
print(lista) # Imprimindo a lista após a limpeza