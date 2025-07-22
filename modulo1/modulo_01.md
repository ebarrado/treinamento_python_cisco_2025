# Certificação exame PCEP-30-0X - PCEP™ – Programador Python Certificado para Iniciantes

Preparação para o exame de certificação PCEP - Certified Entry - Level Python Programmer

## O que faz uma linguagem?

* um Alfabeto
    - conjunto de símbolos usado para criar palavras de um determinado idioma
    - Exemplo: na linguagem Python, o alfabeto inclui letras (A-Z, a-z), dígitos (0-9), símbolos como +, -, *, /, =, _, e caracteres especiais como aspas (" '), parênteses (), colchetes [], entre outros.

* uma Lexis
    - representa o conjunto de palavras reconhecidas pela linguagem, como palavras-chave, identificadores, operadores e literais.

    * Exemplo: Em Python, palavras como `if`, `else`, `for`, `print`, `True`, `False`, operadores como `+`, `-`, `*`, `/`, e identificadores definidos pelo usuário fazem parte da lexis.

* uma Sintaxe
    - define como as palavras e símbolos devem ser organizados para formar comandos compreensíveis pela linguagem.
    - Exemplo: Em Python, a instrução `print("Olá, mundo!")` segue a sintaxe correta, enquanto `print "Olá, mundo!"` não é válido.

* uma Semântica
    - conjunto de regras que determina se uma frase ou comando faz sentido dentro da linguagem, ou seja, se a instrução pode ser executada corretamente.

        * Exemplo: Em Python, `10 / 2` tem semântica válida, pois realiza uma divisão entre dois números. Já `10 / "texto"` não faz sentido semanticamente, pois não é possível dividir um número por uma string.


## Linguagem da máquina x linguagem de alto nível

**Linguagem de máquina** é o conjunto de instruções diretamente compreendidas pelo processador do computador. Essas instruções são compostas por códigos binários (0s e 1s) que representam operações básicas, como somar, mover dados ou comparar valores. Cada tipo de processador possui seu próprio conjunto de instruções de máquina, chamado de *arquitetura*. 

**Linguagem de alto nível** é um tipo de linguagem de programação projetada para ser mais próxima da linguagem humana, facilitando o entendimento e a escrita do código. Ela abstrai detalhes complexos do funcionamento do computador, permitindo que o programador foque na lógica do problema, sem se preocupar com instruções específicas do hardware. Exemplos incluem Python, Java e C#.

## Compilação x Interpretação

**Código compilado** é transformado por um compilador em código de máquina antes de ser executado. O programa gerado pode ser executado diretamente pelo computador. Exemplos: C, C++ e Go.

**Código interpretado** é executado linha por linha por um interpretador, sem gerar um arquivo de código de máquina independente. Exemplos: Python, JavaScript e Ruby.

## Exemplos de código

### Exemplo de código compilado (C)

```c
#include <stdio.h>

int main() {
    printf("Olá, mundo!\n");
    return 0;
}
```
*Este código precisa ser compilado antes de ser executado.*

---

### Exemplo de código interpretado (Python)

```python
print("Olá, mundo!")
```
*Este código pode ser executado diretamente pelo interpretador Python.*

## Exemplos de questões certificação PCEP-30-0X

### 1. Qual das opções abaixo representa uma palavra-chave da linguagem Python?
a) print  
b) main  
c) if  
d) echo  

**Resposta correta:** c) if

---

### 2. O que é necessário para que um código em C seja executado?
a) Interpretador  
b) Compilador  
c) Navegador web  
d) Editor de texto  

**Resposta correta:** b) Compilador

---

### 3. Qual das alternativas abaixo descreve corretamente a diferença entre linguagem de máquina e linguagem de alto nível?
a) Linguagem de máquina é mais fácil de entender para humanos  
b) Linguagem de alto nível é composta apenas por números binários  
c) Linguagem de máquina é diretamente compreendida pelo processador  
d) Linguagem de alto nível não pode ser usada para programar computadores  

**Resposta correta:** c) Linguagem de máquina é diretamente compreendida pelo processador

---

### 4. Qual dos exemplos abaixo possui sintaxe válida em Python?
a) print "Olá, mundo!"  
b) print("Olá, mundo!")  
c) echo("Olá, mundo!")  
d) printf("Olá, mundo!")  

**Resposta correta:** b) print("Olá, mundo!")

---

### 5. O que acontece se você tentar executar `10 / "texto"` em Python?
a) O resultado será 10  
b) O resultado será "texto"  
c) O Python exibirá um erro  
d) O resultado será 0  

**Resposta correta:** c) O Python exibirá um erro

## Python 2 x Python 3

**Python 2** foi lançado em 2000 e tornou-se amplamente utilizado por muitos anos. No entanto, possui limitações e diferenças de sintaxe em relação ao Python 3, como o comando `print` sem parênteses (`print "texto"`), tratamento de strings e divisão de inteiros.

**Python 3** foi lançado em 2008 para corrigir inconsistências e melhorar a linguagem. Traz mudanças importantes, como o uso obrigatório de parênteses no `print` (`print("texto")`), melhor suporte a Unicode, e divisão de inteiros que retorna float por padrão. O Python 2 chegou ao fim do suporte oficial em 2020, tornando o Python 3 o padrão para novos projetos.

## Padrão de distribuição cPython

**cPython** é a implementação oficial e mais utilizada da linguagem Python. Ela é escrita em C e serve como referência para outras implementações. O cPython inclui o interpretador, o compilador, o gerenciador de memória e a biblioteca padrão, sendo distribuído gratuitamente para diversos sistemas operacionais (Windows, macOS, Linux).

Ao baixar Python do site oficial ([python.org](https://www.python.org/)), você está obtendo o cPython. Ele garante compatibilidade total com os recursos da linguagem e é recomendado para a maioria dos projetos.

Outras implementações de Python incluem Jython (para Java), IronPython (para .NET) e PyPy (com foco em desempenho), mas cPython é o padrão adotado na certificação PCEP.

## Outras distribuições de Python

Além do cPython, existem outras distribuições que oferecem recursos adicionais ou são otimizadas para casos de uso específicos:

- **Anaconda**: Voltada para ciência de dados e aprendizado de máquina, inclui diversas bibliotecas populares (NumPy, pandas, matplotlib) e um gerenciador de ambientes chamado Conda.
- **Miniconda**: Uma versão mais enxuta do Anaconda, permitindo instalar apenas os pacotes necessários.
- **PyPy**: Focada em desempenho, utiliza um compilador JIT (Just-In-Time) para acelerar a execução de programas Python.
- **Jython**: Implementação de Python para a plataforma Java, permitindo integração direta com bibliotecas Java.
- **IronPython**: Voltada para o ecossistema .NET, possibilita integração com aplicações e bibliotecas desse ambiente.

Essas distribuições podem ser úteis conforme o tipo de projeto ou ambiente em que você está trabalhando.

