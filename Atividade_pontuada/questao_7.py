import os
os.system("clear")


print("""
 Codigo  \t\t Nome \t\t preço
                  
    1   \t\t PERFUME \t R$ 250,00
    2   \t\t CAMISA \t R$ 80,00
    3   \t\t CALÇA\t\t R$ 89,90
    4   \t\t BERMUDA \t R$ 60,00

Digite o codigo do produto que deseja: """)


descricao = input().upper()
quantidade = int(input("Digite a quantidade que deseja: "))
preco_unitario = 0 


match descricao:

    case "1":

        preco_unitario = 250.00
        descricao = "PERFUME"

    case "2":

        preco_unitario = 80.00
        descricao = "CAMISA"

    case "3":

        preco_unitario = 89.90
        descricao = "CALÇA"

    case "4":

        preco_unitario = 60.00
        descricao = "BERMUDA"

    case _:

        print("Código de produto inválido.")
        

total = quantidade * preco_unitario

if quantidade <= 5:

    desconto = total * 0.02

elif quantidade > 5 and quantidade <= 10:

    desconto = total * 0.03

else:
    desconto = total * 0.05

total_a_pagar = total - desconto

print(f"Descrição do produto: {descricao}")
print(f"Quantidade adquirida: {quantidade}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Total: R${total:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${total_a_pagar:.2f}")


