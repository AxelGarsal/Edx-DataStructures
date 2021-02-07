#Capitulo de Strings
#la funcion input regresa strings
# la posicion inicial siempre es 0
fruta = input("dame una fruta: ")
letra  = fruta[2]
print(letra)
x = 4
w = fruta[x - 1]
print(w)
print('la longitud de esta fruta es de: ',len(fruta))
# la posicion del string si se puede operar como int

# imprimir la letra con su posicion con un while
palabra = input("dame una palabra: ")
i = 0
while i < len(palabra):
    letra = palabra[i]
    print(i, letra)
    i = i + 1

# imprimir la letra con su posicion con un for
pais = input("Dame el nombre de un país: ")
i = 0
for i in range(len(pais)):
    letter = pais[i]
    print(i, letter)
#cuenta la cantidad de letras en especifico que hay en una palabra
nombre = input('dame tu nombre: ')
i = 0 # contador de posicion
for x in nombre: # x contador de la letra 'a'
    if x == 'a':
        i = i + 1
print('La cantidad de letras a que tiene tu nombre es de: ', i)
#imprimir una parte de un string
print(nombre[0:4])
print(pais[5:])
print(fruta[:])
