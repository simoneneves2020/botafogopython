"""
Escreva um programa que pergunte a distância que um passageiro 
deseja percorrer em km.Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,45 para viagens mais longas.
"""

km = float(input("Digite a distância percorrida"))

if km <= 200:
    passagem =  0.5 * km
   
else:
    passagem =  0.45 * km
print(f'O valor a pagar por percorrer a distância de {km} é  R${passagem}')    