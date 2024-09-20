#
#
#print("Esperamos 10 segundos")

"""
Faça um programa para escrever a contagem regressiva do
 lançamento de um foguete. O
programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.

"""
import time

for i in range(10,-1,-1):
    time.sleep(1)
    print(i)
print("Fogo!")