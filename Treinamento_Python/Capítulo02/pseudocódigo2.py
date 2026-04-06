#Exiba "Bem-vindo à Calculadora"
#Peça para o usuário inserir o primeiro número
#Armazene o primeiro número em uma variável
#Peça para o usuário inserir o segundo número
#Armazene o segundo número em uma variável
#Peça para o usuário selecionar uma operação (+, -, *, /)
#Armazene a operação em uma variável
#Utilize a operação selecionada e os números armazenados para realizar o cálculo
#Exiba o resultado

print("Bem-vindo à Calculadora")

num01 = float(input("Insira o primeiro número: "))
num02 = float(input("Insira o segundo número: "))

operacao = input("Selecione a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num01 + num02
elif operacao == "-":
    resultado = num01 - num02
elif operacao == "*":
    resultado = num01 * num02
elif operacao == "/":
    if num02 != 0:
        resultado = num01 / num02
    else:
        resultado = "Erro: Divisão por zero"

print(f"O resultado da operação é: {resultado}")