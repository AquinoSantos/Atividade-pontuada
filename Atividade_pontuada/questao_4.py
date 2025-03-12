import os
os.system("clear")


print("""
 Codigo  \t\t Fruta \t\t\t valor(Kg)
                  
    1   \t\t Maça \t\t\t R$ 1,80 até 5 Kg
    2   \t\t Maça \t\t\t R$ 1,50 acima de 5 Kg
    3   \t\t Morango \t\t R$ 2,50 até 5 Kg
    4   \t\t Morango \t\t R$ 2,20 acima de 5 Kg
    """)

morango = float(input("Digite a quantidade de morangos (em Kg) que deseja: "))
maca= float(input("Digite a quantidade de maçãs (em Kg) que deseja: "))

if morango <= 5:
            
            preco = 2.50

elif morango > 5:
            
            preco = 2.20

elif maca <= 5:
            
            preco = 1.80

elif maca > 5:
            
            preco = 1.50


total_kg = morango + maca
total_preco = morango + maca


if total_kg > 10 or total_preco > 15.00:
        total_preco = total_preco * 0.90




print(f"\nValor a ser pago: R$ {total_preco:.2f}")
print("Obrigado e volte sempre!")
        
































        