import os
os.system("clear")

valor_a = int(input("Digite um valor: "))
operador = input("Digite um operador(+ - * /): ")
valor_b = int(input("Digite um valor: "))

match operador:

    case "+":
        resultado = valor_a + valor_b

    case "-":
        resultado = valor_a - valor_b

    case "*":
        resultado = valor_a * valor_b

    case "/":
        resultado = valor_a / valor_b


print(f"Resultado: {resultado} ")




