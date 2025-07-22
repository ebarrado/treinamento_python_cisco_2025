# Operadores em Python

Python oferece diversos operadores para realizar operações em variáveis e valores. Eles são classificados em:

- **Operadores aritméticos**: `+`, `-`, `*`, `/`, `//`, `%`, `**`  
    Usados para cálculos matemáticos.

- **Operadores de comparação**: `==`, `!=`, `>`, `<`, `>=`, `<=`  
    Comparam valores e retornam `True` ou `False`.

- **Operadores lógicos**: `and`, `or`, `not`  
    Combinam expressões booleanas.

- **Operadores de atribuição**: `=`, `+=`, `-=`, `*=`, `/=`, etc.  
    Atribuem valores às variáveis.

- **Operadores de identidade**: `is`, `is not`  
    Verificam se dois objetos ocupam a mesma posição na memória.

- **Operadores de associação**: `in`, `not in`  
    Testam se um valor está presente em uma sequência.

Esses operadores são fundamentais para controlar o fluxo e manipular dados em programas Python.

- Função print()
    ````python
    print(2+4)
    ````

    ### Operadores aritméticos

    - **Exponenciação (`**`)**: Eleva um número à potência de outro.  
        Exemplo: `2 ** 3` resulta em `8`.

    - **Multiplicação (`*`)**: Multiplica dois valores.  
        Exemplo: `2 * 3` resulta em `6`.

    - **Divisão (`/`)**: Divide um valor pelo outro, retornando um número decimal.  
        Exemplo: `7 / 2` resulta em `3.5`.

    - **Divisão inteira (`//`)**: Divide e retorna apenas a parte inteira do resultado.  
        Exemplo: `7 // 2` resulta em `3`.

    - **Arredondamento**: Pode ser feito com a função `round()`, que arredonda o valor para o inteiro mais próximo.  
        Exemplo: `round(3.6)` resulta em `4`.

    - **Módulo (`%`)**: Retorna o resto da divisão entre dois valores.  
        Exemplo: `7 % 2` resulta em `1`.

    - **Adição (`+`)**: Soma dois valores.  
        Exemplo: `2 + 3` resulta em `5`.


### Operadores e suas prioridades

Em Python, operadores possuem diferentes níveis de prioridade (ou precedência), determinando a ordem em que as operações são avaliadas em uma expressão. Operadores com maior prioridade são avaliados antes dos de menor prioridade.

Por exemplo, a multiplicação (`*`) e divisão (`/`) têm prioridade maior que a adição (`+`) e subtração (`-`). Parênteses `()` podem ser usados para alterar a ordem padrão de avaliação.

**Exemplo de precedência:**
```python
resultado = 2 + 3 * 4  # resultado é 14, pois 3*4 é avaliado primeiro
resultado = (2 + 3) * 4  # resultado é 20, pois 2+3 é avaliado primeiro
```

A ordem de prioridade dos principais operadores é:
1. Parênteses `()`
2. Exponenciação `**`
3. Multiplicação `*`, divisão `/`, divisão inteira `//`, módulo `%`
4. Adição `+`, subtração `-`
5. Operadores de comparação (`==`, `!=`, `>`, `<`, `>=`, `<=`)
6. Operadores lógicos (`not`, `and`, `or`)

Compreender a precedência dos operadores é essencial para evitar resultados inesperados em expressões complexas.

## Análise passo a passo de uma expressão

Vamos analisar passo a passo a expressão dentro do `print`:

```python
print( (5 * ((25 % 13) + 100) / (2 * 13)) // 2 )
```

**Passo a passo:**

1. `25 % 13`  
    O operador `%` retorna o resto da divisão.  
    25 dividido por 13 é 1, resto 12.  
    Resultado: `12`

2. `((25 % 13) + 100)`  
    12 + 100 = `112`

3. `5 * 112`  
    5 vezes 112 = `560`

4. `(2 * 13)`  
    2 vezes 13 = `26`

5. `560 / 26`  
    560 dividido por 26 = `21.53846153846154`

6. `21.53846153846154 // 2`  
    O operador `//` faz divisão inteira (descarta as casas decimais).  
    21.53846153846154 // 2 = `10.0` (o resultado anterior era float)

**Resultado final:**  
O valor impresso será `10.0`.

### Explicação rápida

- `%` pega o resto da divisão.
- `//` faz divisão inteira.
- A expressão é resolvida seguindo a ordem dos parênteses e operadores.

### Sugestão para facilitar a leitura

Você pode dividir em variáveis para entender melhor:

```python
resto = 25 % 13
soma = resto + 100
produto = 5 * soma
divisor = 2 * 13
divisao = produto / divisor
resultado = divisao // 2
print(resultado)  # 10.0
```
