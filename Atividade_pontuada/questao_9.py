import os
os.system("clear")


renda_mensal = float(input("Digite a sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor do empréstimo que deseja: "))
numero_prestacoes = int(input("Digite o número de prestações: "))


valor_emprestimo_maximo = 10 * renda_mensal


valor_prestacao_maximo = 0.3 * renda_mensal


valor_prestacao = valor_emprestimo / numero_prestacoes


if valor_emprestimo <= valor_emprestimo_maximo and valor_prestacao <= valor_prestacao_maximo:
    print("Empréstimo pode ser concedido.")


else:
    print("Empréstimo não pode ser concedido.")














































