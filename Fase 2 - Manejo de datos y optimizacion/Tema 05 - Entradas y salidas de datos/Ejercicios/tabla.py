#Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
# El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
# En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
# El script contendrá un bucle for que itere el número de veces del primer argumento.
# Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
# Dentro del segundo for, añade un print que escriba un *.
# Al final de cada iteración del segundo for, añade un print que escriba un salto de línea.

import sys

if len(sys.argv) == 3:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        if int(sys.argv[1]) in range(1,10) and int(sys.argv[2]) in range(1,10):
            for i in range(int(sys.argv[1])):
                for j in range(int(sys.argv[2])):
                    print("*", end="")
                print()
        else:
            print("Error: Los argumentos deben ser números enteros positivos del 1 al 9.")
    else:
        print("Error: Los argumentos deben ser números enteros positivos del 1 al 9.")
else:
    print("Error: Debe introducir 2 argumentos.")
    print("Uso: python tabla.py <número de filas> <número de columnas>")


