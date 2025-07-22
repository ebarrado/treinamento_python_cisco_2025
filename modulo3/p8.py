numero = -999_999_999_999
maior = numero
while numero != -1:
    numero = int(input("Digite um número (0 para sair): "))
    if numero > maior:
       maior = numero
print("Maior número até agora:", maior)
# código tem uma falha proposital se digitado -1 no primeiro valor

print("Fim do programa.")