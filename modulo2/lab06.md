## 📏 Cenário

> Milhas e quilômetros são unidades de comprimento ou distância.
> Lembrando que 1 milha é igual a aproximadamente 1.61 quilômetros.
> **Vamos converter entre essas unidades!**

---

## 🧠 Sua tarefa:

Complete o programa para:

* Converter **milhas em quilômetros**;
* Converter **quilômetros em milhas**.

Não altere o código inicial. Escreva nos locais indicados por `###`.

### Código:

```python
# conversão de milhas para quilômetros
miles = 7.38
# escreva seu código aqui
###
kilometers = miles * 1.61
print(miles, "milhas é", round(kilometers, 2), "quilômetros")

# conversão de quilômetros para milhas
kilometers = 12.25
# escreva seu código aqui
###
miles = kilometers / 1.61
print(kilometers, "quilômetros é", round(miles, 2), "milhas")
```

---

## 📌 Dica:

Veja o uso da função `round()` dentro da função `print()`. Ela serve para **arredondar os resultados**, e recebe dois argumentos:

* o valor a ser arredondado;
* o número de casas decimais desejado.

Exemplo:

```python
round(3.14159, 2)  # retorna 3.14
```

---

## 🧪 Experimente mais!

Depois de concluir, abra um editor Python e tente:

* Criar um **conversor de moedas** (USD para EUR, BRL, etc.);
* Criar um **conversor de temperatura** (Celsius para Fahrenheit);
* Combinar strings com variáveis em `print()`;
* Usar `round()` com 1, 2, 3 ou sem número de casas decimais.

---

## ✅ Saída esperada:

```
7.38 milhas é 11.88 quilômetros
12.25 quilômetros é 7.61 milhas
```

