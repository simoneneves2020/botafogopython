# copiar lista
sudeste = ["rj","sp","mg","es"]
estados = sudeste
print(sudeste)
print(estados)

sudeste[0]= "rio de janeiro"
print(sudeste)
print(estados)

estados.remove("mg")
print(sudeste)
print(estados)

sul = ["rs","sc","pr"]
sul2 = sul.copy()

print("--------")
print(sul)
print(sul2)
print("--------")
sul.remove("rs")
print(sul)
print(sul2)
