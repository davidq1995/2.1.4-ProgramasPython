
# lista=[1,2,3]
# lista.append(9)
# lista.append(19)

# while True:
#     op=int{input()}
#     match op
#         case 1:
#             for g in lista:
#                 print(g)

# datos ="""ESTA WEA ME CARGA"""
# with open('archivo_david.txt', 'w') as archivo:
#     archivo.write(datos)


# import csv

# with open('archivo_david.csv', 'w', newline='') as archivo_csv:
#     escritor_csv = csv.writer(archivo_csv)

#     escritor_csv.writerow(['Nombre', 'Edad', 'Comuna'])

#     escritor_csv.writerows([
#     ['Esteban', 25, 'Santiago'],
#     ['David', 29, 'Santiago'],
#     ['Kendell', 35, 'Santiago'],
#     ['Vicente', 19, 'Santiago'],
#     ['Cristóbal', 0.5, 'Santiago'],
#     ['Anita', 25, 'Santiago'],
#     ])

    #ls

import csv

num=0
lista="Los datos a guardar son ", str(num)

with open('bingo_david.txt', 'w') as archivo:
    archivo.write(str(lista))

bingoql=[]
with open('bingo_david.csv', 'w', newline='') as archivo_csv:
    escritor_csv.writerow(['Nombre', 'Número', 'Cantidad de números comprados'])

    escritor_csv.writerows([
    ['Esteban', 12, '3 Números'],
    ['David', 23, '2 Números'],
    ['Kendell', 34, '10 Números'],
    ['Vicente', 45, '1 Número'],
    ['Cristóbal', 56, '1 Número'],
    ['Anita', 67, '1 Número'],
    ])


