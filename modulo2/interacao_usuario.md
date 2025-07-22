# Interação com o usuário em Python

A função input() é usada para ler dados digitados pelo usuário no console.

````python
variavel = input("Mensagem para o usuário: ")
````

- A mensagem entre aspas é exibida na tela como um prompt.
- O valor digitado pelo usuário é sempre retornado como uma string (str).

## Exemplo:

````python
nome = input("Qual é o seu nome? ")
print("Olá,", nome)
````

## Conversão de Tipos

Se precisar de números (inteiros ou decimais), é necessário converter o valor:

````python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
````

>Obseração

Ele replica a string o mesmo número de vezes especificado pelo número.

Por exemplo:

"James" * 3 gera "JamesJamesJames"
3 * "an" gera "ananan"
5 * "2" (or "2" * 5) gera "22222" (não10!)


>Lembre-se

Um número menor ou igual a zero produz uma string vazia.

Este simples programa "desenha" um retângulo, fazendo uso de um antigo operador (+) em um novo papel:

````python
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
````