# Lê o número de blocos disponíveis
blocos = int(input("Digite o número de blocos: "))

altura = 0
camada = 1

# Enquanto houver blocos suficientes para a próxima camada
while blocos >= camada:
    blocos -= camada
    altura += 1
    camada += 1

print("A altura da pirâmide:", altura)
