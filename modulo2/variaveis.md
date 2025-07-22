# Variáveis em Python

## O que são variáveis?

Variáveis são espaços na memória que armazenam valores para serem usados durante a execução do programa. Em Python, não é necessário declarar o tipo da variável, pois o tipo é definido automaticamente pelo valor atribuído.

## Como criar variáveis

```python
nome = "Ana"
idade = 25
altura = 1.68
```

## Regras para nomes de variáveis

- Devem começar com uma letra ou _ (underscore)
- Não podem conter espaços ou caracteres especiais
- São sensíveis a maiúsculas e minúsculas (`idade` é diferente de `Idade`)

## Tipos comuns de variáveis

- `int`: números inteiros (`10`)
- `float`: números decimais (`3.14`)
- `str`: textos (`"Python"`)
- `bool`: valores lógicos (`True` ou `False`)

## Exemplo de uso

```python
mensagem = "Bem-vindo ao Python!"
print(mensagem)
```

## Exemplos de nomes de variáveis

| Nome de variável                | Correto? | Observação                                              |
|----------------------------------|----------|---------------------------------------------------------|
| MyVariable                      | Sim      | Convenção PascalCase, pouco usada em Python             |
| i                               | Sim      | Comum em loops, mas pouco descritivo                    |
| l                               | Sim      | Pode ser confundido com o número 1                      |
| t34                             | Sim      | Aceito, mas pouco descritivo                            |
| Exchange_Rate                   | Sim      | Convenção snake_case, recomendada em Python             |
| counter                         | Sim      | Descritivo                                              |
| days_to_christmas               | Sim      | Descritivo                                              |
| TheNameIsTooLongAndHardlyReadable | Sim    | Aceito, mas pouco prático                               |
| _                               | Sim      | Usado para valores descartados                          |
| Adiós_Señora                    | Sim      | Aceito, inclui caracteres especiais                     |
| sûr_la_mer                      | Sim      | Aceito, inclui caracteres especiais                     |
| Einbahnstraße                   | Sim      | Aceito, inclui caracteres especiais                     |
| переменная                      | Sim      | Aceito, inclui caracteres não latinos                   |
| 10t                             | Não      | Não começa com letra ou _                               |
| !important                      | Não      | Não começa com letra ou _                               |
| exchange rate                   | Não      | Contém espaço                                           |

> Python permite o uso de caracteres especiais e alfabetos não latinos em nomes de variáveis, mas recomenda-se nomes claros e descritivos.

> Observação  

- O PEP 8 - Guia de Estilo para Código Python recomenda a seguinte convenção de nomenclatura para variáveis e funções em Python:

    - os nomes de variáveis devem estar em letras minúsculas, com palavras separadas por sublinhados para melhorar a legibilidade (por exemplo, var, my_variable)
    - nomes de funções seguem a mesma convenção que nomes de variáveis (por exemplo, fun, my_function)
    - também é possível usar casos mistos (por exemplo, myVariable), mas apenas em contextos onde esse já é o estilo predominante, para manter a compatibilidade com a convenção adotada.


## Criar variável

Para criar uma variável basta usar o nome da variável desejada, depois o sinal de igual(=) e o valor que deseja colocar na variável.

````python
var = 1
print(var)
````

## Usar uma variável

Pode-se utilizar quantas declarações de variáveis forem necessárias para atingir seu objetivo.

````python
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
````

## Atribuir novo valor a uma variável já existente

Exemplo:

````python
var = 1
print(var)
var = var + 1
print(var)
````