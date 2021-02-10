#los diccionario van entre [], son mutables, su constructor es dict()
series = dict()
series['Revenge'] = 4
series['HTGATM'] = 6
series['Charmed'] = 8
series['Revenge'] = series['Revenge'] + 9
print(series['Revenge'])
print(series)
personas=dict()
nombres=['axel', 'alan', 'alex', 'alan', 'alan', 'alex', 'axel', 'axel', 'alex', 'fran', 'axel', 'alan']

for i in nombres:
    if not i in personas:
        personas[i]=1
        #print(personas)
    else:
        personas[i]=personas[i]+1
        #print(personas)
print(personas)

for x in nombres:
    personas[x]= personas.get(x, 0)
print(personas)
