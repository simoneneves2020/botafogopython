
quantidadekw = int(input("Digite a quantidade de KWh Consumida : "))
tipoinstalacao = input("Digite o tipo de Instalação \n I - Industrial \n C - Comercial \n R - Residencial")

if tipoinstalacao == "R" or tipoinstalacao == "r":
    if quantidadekw <= 500:
        precopagar = 0.40        
    else:
        precopagar = 0.65
elif tipoinstalacao == "C" or tipoinstalacao == "c":
    if quantidadekw <= 1000:
        precopagar = 0.55
    else:
        precopagar = 0.60
elif tipoinstalacao == "I" or tipoinstalacao == "i":
    if quantidadekw <= 5000:
        precopagar = 0.70
    else:
        precopagar = 0.80
else:
    precopagar = 0
    print("Erro ! Tipo de Instalação desconhecido")
custo = quantidadekw * precopagar
print(f'O valor a pagar R$ {custo}')




