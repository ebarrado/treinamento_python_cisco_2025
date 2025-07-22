# Operações com Listas
lista = [1,23,4,5,6,7,8,9,10]
print(lista[0]) # Acessando o primeiro elemento da lista
print(lista[1]) # Acessando o segundo elemento da lista 
print(lista[2]) # Acessando o terceiro elemento da lista
print(lista[3]) # Acessando o quarto elemento da lista

print(len(lista), " elementos") # Imprimindo o tamanho da lista
print(lista[0:3]) # Imprimindo os três primeiros elementos da lista

del lista[0] # Deletando o primeiro elemento da lista
print(lista) # Imprimindo a lista após a deleção do primeiro elemento

lista[3]=8 # Substituindo o quarto elemento da lista por 8
print(lista) # Imprimindo a lista após a substituição do quarto elemento
print(lista[0:3]) # Imprimindo novamente os três primeiros elementos da lista

print(lista[-1])

