puntajes = [120, 45, 300, 80, 210]

ordenada = sorted(puntajes, reverse=True)

print("Lista original:", puntajes)
print("Copia ordenada:", ordenada)

puntajes.sort(reverse=True)
print("Lista ordenada", puntajes)
