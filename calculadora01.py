def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: ta dividindo por zero"

def calcuradora():
    print("Selecione a oporação")
    print("1. SOMA")
    print("2. SUBTRAÇÃO")
    print("3. MULTIPLICAÇÃO")
    print("4. DIVISÃO")

    escolha = input("Digite o numero da operação (1/2/3/4):")

    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))

    if escolha == "1":
        print(num1, "+", num2, "=", soma(num1, num2))

    elif escolha == "2":
        print(num1, "-", num2, "=", subtracao(num1, num2))

    elif escolha == "3":
        print(num1, "*", num2, "=", multiplicacao(num1, num2))

    elif escolha == "4":
        print(num1, "/", num2, "=", divisao(num1, num2))

    else:
        print("deu erro")

calcuradora()