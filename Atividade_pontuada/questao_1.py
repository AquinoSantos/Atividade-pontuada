import os
os.system("clear")


valor_a = float(input("Digite o valor de A: "))
valor_b= float(input("Digite o valor de B: "))
valor_c= float(input("Digite o valor de C: "))


if valor_a + valor_b < valor_c:
    print("A soma de A + B é menor que C")
else:
    print("A soma de A + B é maior que C")
