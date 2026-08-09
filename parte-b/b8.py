lecturas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

promedios = []

for i in range(len(lecturas) - 2):
    promedio = (lecturas[i] + lecturas[i + 1] + lecturas[i + 2]) / 3
    promedios.append(promedio)

print("Lecturas:", lecturas)
print("Promedios:", promedios)