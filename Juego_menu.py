
#para poder acceder a las funciones que corresponde a los juegos, utilizamos la función from/import.
#Importamos la clase desde los archivos donde hemos guardado el código de cada juego.

from Juegos import Juegos
from Juegos import Jugadores
import os

# Definimos una presentación gráfica del juego mediante el método print()
os.system("clear")
print("================================================================================")
print("=        xxxxxxx      xxxxxxx                                                  =")
print("=          xxxxx      xxxxx     xxxxx  xxxxx  xxx  xxx  xxxxxx  xxxxxx         =")
print("=             xxx    xxx        x      x   x  x  xx  x  x       x              =")
print("=               xxx xxx         x  xx  xxxxx  x   x  x  xxxxxx  xxxxxx         =")
print("=             xxx    xxx        x   x  x   x  x      x  x            x         =")
print("=          xxxxx      xxxxx     xxxxx  x   x  x      x  xxxxxx  xxxxxx         =")
print("=        xxxxxxx      xxxxxxx                                                  =")
print("================================================================================")
print("")
print(" Bienvenido a los juegos interactivos de X Games ")
print("================================================")
print("")  

#Introducimos los datos del usuario para identificar al jugador y a la consola.
#Utilizamos la función input() para preguntar al usuario:

nombre=input("Introduce tu nombre: ").capitalize()             
equipo=input("A que equipo perteneces: ").capitalize()

# Creamos la instancia de la classe Juegos
juego = Juegos(nombre,equipo)

#*MEJORA EN PROCESO: Registro de jugadores.
#Creamos un registro de jugadores para registrar las rachas ganadas y puntuaciones:

lista_jugadores=Jugadores()
lista_jugadores.alta_jugador(nombre,equipo)

#Ofrecemos al usuario la lista de juegos disponibles:

print("")
print("")  
print("Listado de juegos")
print("")
print("  1. Preguntas y respuestas")
print("  2. Ahorcado")
print("  3. Piedra,papel o tijera")
print("  4. Salir")
print("")
print("")

print("================================================")

#Le indicamos al jugador que seleccione un juego con la función input()
#El jugador, debe indicar el dígito asociado a cada juego:1,2,3,4
    
seleccion=input(f"{nombre} elige uno de los juegos (1,2,3 o 4 para salir):  ")

#creamos una sentencia de control asociada a una funcion de cada juego:
#cada condición llama a la función del juego seleccionado.
if seleccion =="1":
    juego.preguntas_y_respuestas()
   
elif seleccion == "2":
    juego.ahorcado()
            
elif seleccion =="3":
    juego.piedra_papel_tijera(nombre)

#Le damos la opción al jugador de salir del juego.
#Esta función nos saca de la consola.
elif seleccion =="4":      
    juego.salir()      
   
else:
    print("No has elegido una opción valida")
    


