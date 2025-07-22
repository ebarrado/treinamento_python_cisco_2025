# Primeiro Programa

Crie um novo aquivo de origem Python, preencha com ````print("Olá Mundo")````, nome o arquivo e salve-o.

Partes importantes:
* a palavra print;
* um parênteses de abertura;
* aspas (")
uma linha de texto: Olá, Mundo!;
* outra aspa;
* outro parênteses.

## Função print()

A função `print()` em Python é usada para exibir informações na tela. Ela recebe um ou mais argumentos e mostra o resultado no console. Por exemplo, `print("Olá Mundo")` imprime o texto entre aspas. É uma das funções mais utilizadas para depuração e interação com o usuário.

## Argumentos de função

Os argumentos de uma função são os valores que você fornece entre os parênteses ao chamá-la. No exemplo `print("Olá Mundo!")`, o texto `"Olá Mundo!"` é o argumento passado para a função `print()`. Os argumentos permitem que as funções realizem tarefas diferentes dependendo dos valores recebidos. Algumas funções podem receber vários argumentos, enquanto outras não precisam de nenhum. Em Python, mesmo funções sem argumentos exigem o uso dos parênteses.

No caso da função `print()`, o argumento é o texto que será exibido na tela.


## Chamada de função

Em Python, uma chamada de função ocorre quando você escreve o nome da função seguido de parênteses, podendo incluir argumentos dentro deles. Por exemplo:

```python
print("Olá Mundo")
```

Neste exemplo, `print` é o nome da função e `"Olá Mundo"` é o argumento passado. Os parênteses indicam que a função está sendo chamada e executada.

## Sintaxe geral de chamada de função

A sintaxe para chamar qualquer função em Python segue o padrão:

```python
nome_da_função(argumento)
```

Por exemplo, se você tiver uma função chamada `saudar`, pode chamá-la assim:

```python
saudar("Olá")
```

Aqui, `saudar` é o nome da função e `"Olá"` é o argumento passado. O formato sempre será `function_name(argument)`, onde você substitui pelo nome da função e os valores desejados.

## Instruções

Uma linha pode estar vazia, mas não deve conter duas, três ou mais instruções.

````python
print("Aprendendo Python")
print("Criando mais de uma linha")
````

* O programa chama a função print() duas vezes, e você pode ver linhas separadas no console
* Cada invocação print() contém uma string diferente, como argumento

Criando arquivo com print() vazio

````python
print ("Aprendendo Python")
print()
print("Criando 3 linhas com 1 print vazio")
````
## Print com mais de um parâmetros

````python
print("como", "vai", "você?")
````
## Parâmetros nomeados do print no Python

````python
print ("Ola", "tudo", "bem", sep="---")
````
* usar o parâmetro nomeado após os posicionados

## Parâmetro end (finalizado do print)

````python
print("Olá", "tudo bem", end="! ")
print()
````
- Saída: `Olá tudo bem!` - tira a quebra de linha

## Usando Escape no Python

Para quebra de linha podemos utilizar o escape `\n`

Obs. Podemos utilizar aspas duplas ou simples no print()

````python
print("Amor é fogo que arde sem se ver,\nÉ ferida que dói e não se sente.")
print()
print("É um contentamento descontente,\nÉ dor que desatina sem doer.")
````
* A barra invertida `\`significa caractere de escape