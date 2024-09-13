"""Escreva um programa que calcule o aumento de salário
. Ele deve solicitar o valor do salário
 e a porcentagem de aumento do aumento.
Exiba o valor do aumento e do novo salário."""
# Entrada -> solicito o usuário que digite uma informação

salario = float(input("Digite o valor do Salário"))
print("O Salario informado foi de R$ ",salario)
aumento = float(input("Digite o percentual de aumento"))
print("O percentual informado foi de ",aumento)
# processamento
novosalario = salario +(salario * aumento)/100
#saída
print("O valor do aumento é R$", aumento)
print("O novo salário é : R$", novosalario)