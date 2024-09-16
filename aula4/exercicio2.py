"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do 
aumento. Para salários superiores a R$ 1.250,00, 
calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""
salario = float(input("Digite o valor do salário do funcionário"))
if salario <= 1250 :
    #salario = salario + (salario * 15)/100
    salario = salario * 1.15
    print(f'O valor do novo salário é R$ {salario}')
else:
    salario = salario * 1.1
    print(f'O valor do novo salário é R$ {salario}')