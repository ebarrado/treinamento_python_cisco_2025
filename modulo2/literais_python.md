# Literais

Literais em Python são valores constantes que representam dados diretamente no código. Exemplos comuns incluem números (`10`, `3.14`), strings (`"texto"`), booleanos (`True`, `False`) e valores especiais como `None`. Eles são usados para inicializar variáveis ou passar valores diretamente para funções.

````python
print("2")
print(2)
````

* A primeira linha representa uma string entre aspas
* A segunda linha representa um número inteiro, não há a necessidade de utilizar aspas.

## Inteiros

Inteiros em Python são números sem parte decimal, positivos ou negativos, representados pelo tipo `int`. Eles podem ser usados em operações matemáticas, atribuídos a variáveis e manipulados facilmente. Exemplos de inteiros incluem `5`, `-12` e `1000`.

```python
saldo = 2000
deposito = 500

print("O saldo = R$", saldo)
print("O novo saldo é R$", saldo + deposito)

# saida
# O saldo = R$ 2000
# O novo saldo é R$ 2500
```

## Números Octais e Hexadecimais

Python permite representar números inteiros em bases diferentes usando prefixos específicos:

- **Octais**: Prefixados por `0o` ou `0O`, utilizam apenas dígitos de 0 a 7. Exemplo: `0o123` (equivale a 83 em decimal).
- **Hexadecimais**: Prefixados por `0x` ou `0X`, utilizam dígitos de 0 a 9 e letras de A a F. Exemplo: `0x123` (equivale a 291 em decimal).

```python
print(0o123)  # saída: 83
print(0x123)  # saída: 291
```

## Floats

Floats (ou números de ponto flutuante) em Python representam valores que possuem parte fracionária, ou seja, números com casas decimais. Exemplos incluem `2.5`, `-0.4`, `0.4` ou `.4`. É importante usar o ponto (`.`) como separador decimal, nunca a vírgula.

A diferença entre inteiros e floats é marcada pelo ponto decimal: `4` é inteiro, enquanto `4.0` é float. Além disso, floats podem ser representados em notação científica usando `e` ou `E`, como `3E8` (equivalente a 3 × 10⁸) ou `6.62607E-34` (constante de Planck).

Python pode exibir floats em notação científica automaticamente para valores muito grandes ou pequenos, por exemplo:

```python
print(0.0000000000000000000001)  # saída: 1e-22
```

A notação científica é útil para representar números com muitos zeros de forma mais compacta.

## Strings

Usados para processar texto (como nomes de todos os tipos, endereços)

Esta é uma string muito típica: `"Eu sou uma string."`
