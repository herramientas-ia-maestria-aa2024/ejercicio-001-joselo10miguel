
with open(r'C:\Users\ordon\Documents\Maestria\Herramientas IA\practicas\ejercicio-001-joselo10miguel\informacion.txt', 'r') as archivo:

    lineas = archivo.readlines()

for i, linea in enumerate(lineas):
    if i == 0:  
        continue
    campos = linea.strip().split(';')
    
    print("Nombres:", campos[0])
    print("Apellidos:", campos[1].split(',')[0]) 
    print("Dirección:", campos[2])
    print("Correo:", campos[3])
    print()  
