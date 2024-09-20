# solicito o usuário para digitar um número
numero = int(input("Digite um número para tabuada de 10"))
#inicializo o número
for index in range (11):
    aux = index * numero
    print(index ," x",numero ," = ",aux )
    