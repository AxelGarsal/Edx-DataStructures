# LISTAS
# lAS listas son mutables e igual empiezan en 0
ciudadanos = ['piccolo', 'goku', 'gohan', 'N.18', 'vegeta']
#print(ciudadanos[1])
#print(range(len(ciudadanos)))
i = 0
j = 0
for i in ciudadanos:
    if i == 'goku':
        print('Gracias por salvarnos', i.upper())
    elif i == 'gohan':
        print(i.upper(),'le gano a Cell')
    else:
        print('Insectos no pudieron', i)
ciudadanos.append('trunks')
ciudadanos.insert(2, 'cell')
print(ciudadanos)

nivel = [536, 975, 992, 1000, 789, 957, 801]

for index, valor in enumerate(ciudadanos):
    print('Guerrero:', valor.upper(), 'Nivel de pelea: ', nivel[index])
#quiero hacer que solo imprima al guerrero mas fuerte
for i, v in enumerate(ciudadanos):
    for j, k in enumerate(nivel):
        if nivel[j] == max(nivel):
            i = j
            print(k,ciudadanos[i])


'''print(ciudadanos)
print(ciudadanos[:-1])
ciudadanos.pop(2)
print(ciudadanos)
ciudadanos.sort()
print(ciudadanos)'''

print('El guerrero más fuerte tiene un nivel de pelea de: ', max(nivel))
#encuentra el valor mas grande de la lista y lo regresa junto con su posicion
for j, k in enumerate(nivel):
    if nivel[j] == max(nivel):
        print(j,k)
