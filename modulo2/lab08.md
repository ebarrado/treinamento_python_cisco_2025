## ➗ Cenário

> Sua tarefa é completar o código para avaliar os resultados de **quatro operações aritméticas básicas**:
> **adição (+), subtração (-), multiplicação (\*) e divisão (/)**.
> Os resultados devem ser **impressos no console**.

> Talvez você não consiga proteger o código de um usuário que deseja dividir por zero. Tudo bem, não se preocupe com isso por enquanto.

> Teste seu código – ele produz os resultados esperados?

> Não mostraremos dados de teste – isso seria muito simples. 😉

---

## 🧐 Sua tarefa:

1. Leia dois números fornecidos pelo usuário.
2. Realize as quatro operações: soma, subtração, multiplicação e divisão.
3. Imprima os resultados.

### Exemplo de código base:

```python
# entrada dos dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# operações aritméticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2  # cuidado com divisão por zero!

# impressão dos resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
```

---

## ✅ Sugestões:

* Tente usar `int()` ao invés de `float()` se quiser trabalhar apenas com números inteiros.
* Tente formatar a saída usando `round()` para arredondar os resultados da divisão.

---

> ✨ Dica extra: tente modificar o código para aceitar três ou mais números, ou aplicar outras opera
