from Juegos import Juegos
from Juegos import Jugadores
import os

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
nombre=input("Introduce tu nombre: ")
equipo=input("A que equipo perteneces: ")
lista_jugadores=Jugadores()
lista_jugadores.alta_jugador(nombre,equipo)

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

    
seleccion=input(f"{nombre} elige unos de los juegos (1,2,3 o 4 para salir):  ")

if seleccion =="1":
    Juegos.preguntas_y_respuestas()
   
elif seleccion == "2":
    Juegos.ahorcado()
            
elif seleccion =="3":
    Juegos.piedra_papel_tijera()

elif seleccion =="4":
    Juegos.salir()
   
else:
    print("No has elegido una opción valida")