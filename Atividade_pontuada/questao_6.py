import os
os.system("clear")


nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))

media = (nota_um + nota_dois) / 2

if media >= 6:
    print("Parabens, aprovado!")

elif media == 4:
    print("Recuperação! ")

elif media < 4:
    print("Reprovado! ")

else:

    print("Valor incorreto!")