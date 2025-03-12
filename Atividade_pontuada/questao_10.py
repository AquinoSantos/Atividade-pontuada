import os
os.system("clear ")



print("""
 Codigo  \tProduto \t\t Desconto
                  
    1  \t\t A-alcool \t\t 2 por cento até 25 L
    2   \t A-alcool \t\t 4 por cento acima de 25 L
    3  \t\t G-gasolina \t\t 3 por cento até 25 L
    4  \t\t G-gasolina \t\t 5 por cento até 25 L
    
""")

produto = input("Digite o codigo do combustivel que deseja: ")
quantidade = float(input("Digite a quantidade em litros: "))






if produto == "1" and produto <= 25:

        
        produto = "A-alcool"
        desconto = 0.02
        valor_unitario = 3.79

        total = quantidade * valor_unitario
        desconto = total * desconto
        total = total - desconto

        

elif produto == "2" and produto > 25:
        
    produto = "A-alcool"
    desconto = 0.04
    valor_unitario = 3.79

    total = quantidade * valor_unitario
    desconto = total * desconto
    total = total - desconto
        
        
elif produto == "3" and produto <= 25:
        
    produto = "G-gasolina"
    desconto = 0.03
    valor_unitario = 6.59

    total = quantidade * valor_unitario
    desconto = total * desconto
    total = total - desconto

       
elif produto == "4" and produto > 25:
        
    produto = "G-gasolina"
    desconto = 0.05
    valor_unitario = 6.59

    total = quantidade * valor_unitario
    desconto = total * desconto
    total = total - desconto


else:

    print("Código de produto inválido.")


        

print(f"Produto: {produto}")
print(f"Valor unitário: R$ {valor_unitario:.2f}")
print(f"Quantidade: {quantidade} L")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")

        


























