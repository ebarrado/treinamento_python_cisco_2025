## 📐 Cenário

> Dê uma olhada no código abaixo: ele lê um valor float, coloca-o em uma variável chamada `x` e imprime o valor de uma variável chamada `y`.
> Sua tarefa é completar o código para avaliar a seguinte expressão:

```
3x³ - 2x² + 3x - 1
```

> O resultado deve ser atribuído a `y`. Lembre-se de usar o operador `*` para multiplicação.
> O tipo de dado deve ser `float`, e o código precisa ser limpo e legível.

---

## 🧠 Sua tarefa:

Complete o código abaixo para que ele calcule corretamente a expressão polinomial e exiba o valor de `y`.

### Código:

```python
x = float(input("Digite o valor de x: "))
# escreva seu código aqui
###
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("y =", y)
```

---

## 📌 Dica:

* Lembre-se de que `x ** 2` representa x ao quadrado, e `x ** 3` representa x ao cubo.
* Use sempre o operador de multiplicação `*`, mesmo quando estiver multiplicando por variáveis.

---

## ✅ Exemplos de entrada e saída:

### Entrada:

```python
x = 0
```

### Saída:

```
y = -1.0
```

### Entrada:

```python
x = 1
```

### Saída:

```
y = 3.0
```

### Entrada:

```python
x = -1
```

### Saída:

```
y = -9.0
```

---

## 🧪 Experimente mais!

* Tente modificar a expressão para outro polinômio.
* Teste com números decimais como `x = 2.5` ou `x = -3.7`.
* Explore combinações de entrada e arredondamento com `round()` se desejar.

> 🎯 Lembre-se: aprender exige prática. Experimente, erre e tente de novo!
