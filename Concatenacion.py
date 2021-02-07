nombre = input('nombre: ')
app = input('apellido1: ')
apm = input('apellido2: ')
if 'a' in app and 'e' in apm:
    curp = app[0:3]+apm[0:2]+nombre[-1]
    curp = curp.upper()
print('Tu curp es ', curp)
completo = nombre + ' ' + app + ' ' + apm
print(completo)
print('Tu fecha de nacimiento')
year = input('año: ')
mes = input('mes: ')
dia = input('dia: ')
pos = year.find('9')
print(pos)
# tambien lo hize como if year[2] == '9'
if year.startswith('199'):
    clave = year[2:]
    curp = curp + clave + mes + dia
print(curp)
appn = app.replace('a','x')
print(appn)


