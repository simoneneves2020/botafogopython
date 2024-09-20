"""
Escreva um programa que leia dois números
 e que pergunte qual operação você deseja realizar.
Você deve poder calcular 
soma (+), subtração (-), multiplicação (*) e divisão (/). 
Exiba o resultado da operação solicitada
"""
# Entrada
num1 = int(input("Digite o primeiro número para cálculo. "))
num2 = int(input("Digite o segundo número. "))
operacacao = input("Deseja realizar soma (+), subtração (-), multiplicação (*) e divisão (/)")

#Processamento
if operacacao == "+":
    resultado = num1 + num2
elif operacacao == "-":
    resultado = num1 - num2
elif operacacao == "*":
    resultado = num1 * num2
elif operacacao == "/":
    resultado = num1 / num2
else:
    print("Operação Inválida")
    resultado = 0
print("Resultado : ", resultado)



#Saída