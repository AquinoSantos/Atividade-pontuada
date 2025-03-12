import os
os.system("clear ")


preco = input("Digite a cor de CD que deseja e saiba o preço: ").upper()

match preco:

    case "VERDE":
        preco = 10.00

    case "AZUL":
        preco = 20.00
    
    case "AMARELO":
        preco = 30.00
    
    case "VERMELHO":
        preco = 40.00


print(f"O preço do CD é R$ {preco:.2f}")

