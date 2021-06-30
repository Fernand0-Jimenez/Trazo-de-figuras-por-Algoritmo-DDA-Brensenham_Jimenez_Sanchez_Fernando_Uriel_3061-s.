import Operaciones
import matplotlib.pyplot as plt


def menu():
    print ("""

        1- Cuadrado
        2- rectangulo
        3- triangulo Equilatero
        4 - triangulo rectangulo
    """)
    figura = int(input("Figura: ")) 
    print ("""

        1- DDA
        2- Bresenham
    """)
    algoritmo = int(input("Algoritmo: ")) 
    
    if figura == 1 or figura == 3:
        ancho = int(input("Ingresa el tamaño de la figura"))
        alto = ancho
    else:
        ancho = int(input("Ingresa la base: "))
        alto = int(input("Ingresa la altura: "))
    return figura,algoritmo,ancho-1,alto-1

def puntos_figura(figura,alto,ancho):
    if figura == 1 or figura == 2:
        # cuadrilateros
        coordenadas = [
            [0,0],
            [0,alto],
            [ancho,alto],
            [ancho,0],
            [0,0]
            ]
    elif figura ==3:
        # equilatero
        # c-b=a
        punto_mas_alto = (alto**2)-(ancho/2)**2
        punto_mas_alto = int(punto_mas_alto**0.5)
        coordenadas = [
            [0,0],
            [ancho,0],
            [ancho//2,punto_mas_alto],
            [0,0]
            ]
    else:
        # triangulo rectangulo
        coordenadas = [
            [0,0],
            [ancho,0],
            [ancho,alto],
            [0,0]
        ]
    return coordenadas

def square(p,n,m):#recibe el plot, coordenada x y coordenada y
    # dibuja un cuadrado en un solo pixel de color verde
    p.plot([n+1,n+1,n,n,n+1],[m,m+1,m+1,m,m],color = "green")

if __name__ == '__main__':
    #obtenemos los datos necesarios para el programa
    figura,algoritmo,ancho,alto=menu()

    # establecemos los puntos para ingresar a los algoritmos de dda y bresenham
    puntos = puntos_figura(figura,alto,ancho)

    # listas para guardar los puntos a graficar y mostrar en consola
    coordenadas_completas_x= []
    coordenadas_completas_y= []

    # llenando con las lineas a partir de los puntos obtenidos
    for i in range(len(puntos)-1):
        if algoritmo ==1:
            x,y = Operaciones.dda(puntos[i][0],puntos[i][1],puntos[i+1][0],puntos[i+1][1])
        else:
            x,y=Operaciones.bresenham(puntos[i][0],puntos[i][1],puntos[i+1][0],puntos[i+1][1])
        coordenadas_completas_x.append(x)
        coordenadas_completas_y.append(y)
        #pinta un cuadro por cada coordenada obtenida de la linea actual de la figura
        for i in range(len(x)):
            square(plt,x[i],y[i])



    print(f"Puntos para trazos {puntos}")
    print(f"Puntos para lineas en x {coordenadas_completas_x}")
    print(f"Puntos para lineas en y {coordenadas_completas_y}")
    plt.show()