import os
os.system("clear")

nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo(M\F): ").upper()
estado_civil = input("Digite seu estado civil: ").upper()

if sexo == "F" and estado_civil == "CASADA":

    tempo = input("Informe o tempo de casada: ")

    print(f"Tempo de casada:  {tempo} anos " )


else:
    print("Informação invalida ")



print("Nome: ", nome)
print("Sexo: ", sexo)
print("Estado civil: ", estado_civil)









    

