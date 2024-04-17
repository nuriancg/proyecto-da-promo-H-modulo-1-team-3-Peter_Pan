#Creamos una presentación para que el usuario interaccione con la lista de juegos disponibles y se inscriba como jugador.
# Cargamos los siguientes módulos para poder usarlos en el código de los juegos:
import os                       #  os nos proporcionará funciones para interacturar con el archivo o el sistema operativo.
import random                   #  radom para generar funciones que impliquen elementos aleatorios.

# MEJORA AÑADIDA: Definimos una clase con métodos que permiten al usuario interactuar con la presentación y lista de juegos.

class Juegos:

  def __init__(self,nombre,equipo):
      
      self.nombre = nombre
      self.equipo = equipo
      pass


  def menu(self):

    # Definimos una presentación gráfica del juego mediante el método print()
    
    self.figura_menu_inicio()
    #Ofrecemos al usuario la lista de juegos disponibles:

    print("Listado de juegos")
    print("")
    print("  1. Preguntas y respuestas")
    print("  2. Ahorcado")
    print("  3. Piedra,papel o tijera")
    print('')
    print('  4. Reglas de los juegos')
    print("  5. Salir")
    print("")
    print("")

    print("================================================")

    #Le indicamos al jugador que seleccione un juego con la función input()
    #El jugador, debe indicar el dígito asociado a cada juego:1,2,3,4
    
    seleccion=input(f"{nombre} elige uno de los juegos (1,2,3 o 4 para salir):  ")

    #creamos una sentencia de control asociada a una funcion de cada juego:
    #cada condición llama a la función del juego seleccionado.
    if seleccion =="1":
        self.preguntas_y_respuestas(nombre)
   
    elif seleccion == "2":
        self.ahorcado(nombre)
            
    elif seleccion =="3":
        self.piedra_papel_tijera(nombre)

    elif seleccion =="4":
        self.reglas_juego()    

    #Le damos la opción al jugador de salir del juego.
    #Esta función nos saca de la consola.
    elif seleccion =="5":      
        self.salir()      
   
    else:
        print("No has elegido una opción valida")


  def ahorcado(self,nombre):
    intentos=10
    acierto=False
    palabra_aleatoria=""
    palabra_guiones=''
    lista_palabra=''
    lista_guiones=''
    palabra_jugada=''
    letra_usada=[]
    letra=''
    palabras_aleatorias = [
      "perro", "gato", "casa", "coche", "mesa", "silla", "libro", "computadora", "planta",
      "ciudad", "pared", "puerta", "ventana", "reloj", "manzana",
      "banana", "naranja", "fresa", "uva", "kiwi",  "piña", "papaya",
      "nube", "sol", "luna", "estrella", "mar", "océano", "lago", "montaña", "colina",
      "valle", "pradera", "desierto", "playa", "arena", "roca", "nieve", "hielo", "fuego", "viento"   
    ]
    
        
    os.system("clear")
    
    print("=================================================================================")
    print("=                      _   _   _   _   _   _   _   _                            =")
    print("=                     / \ / \ / \ / \ / \ / \ / \ / \                           =")
    print("=                    ( a | h | o | r | c | a | d | o )                          =")
    print("=                     \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                           =")
    print("=                                                                               =")
    print("=================================================================================")

    print(f"\n\n              ¡¡¡ {nombre} bienvenid@ al juego del Ahoracado !!!\n\n")    
    print ("          El juego consiste en adivinar la palabra oculta letra a letra.\n\n")
    print("                     ¡¡¡¡   E M P E C E M O S  !!!\n\n\n")
    input('Presiona "ENTER" para continuar')
    os.system("clear")


    palabra_aleatoria = random.choice(palabras_aleatorias).lower()  
    palabra_guiones = "_"*len(palabra_aleatoria)
    lista_palabra=list(palabra_aleatoria)
    lista_guiones=list(palabra_guiones)


    
    while 0 < intentos <= 10 and acierto==False:

      # Imprimir guiones sin letras

        self.figura_Ahoracado(intentos)
    
        print(f"\nEstas son las letras ocultas de la palabra:   {' '.join(lista_guiones)}")
        #letra_usada.append(letra)
        print(f'\n\nLas letras usadas hasta ahora son: {letra_usada}\n\n')

      # preguntar al usuario la ltera
        letra=input("Introduce una letra a ver si está en la palabra =>  ").lower()

        if letra in lista_palabra:
          print(f'\n\nGenial! la letra {letra.upper()} está en la palabra oculta.')
          print("-------------------------------")
          
          aux=0 
          for i in lista_palabra:      
            if i == letra:
                lista_guiones[aux]=letra

            aux += 1
            
        else:
            intentos-=1
            print(f'\n\nNo, la letra {letra.upper()} no está.\n\n{nombre} te quedan {intentos} intentos.')
            print("-------------------------------")
    
      # LETRAS ACERTADAS en el espacio correspondiente en lugar de guiones  
        palabra_jugada = ''.join(lista_guiones)
    
      # Imprimir las letras usadas
        if letra not in letra_usada:
          letra_usada.append(letra)
          letra_usada.sort()
        
        print('\n\n\n')
        input('Presiona "ENTER" para continuar')
        os.system("clear")

        if palabra_jugada == palabra_aleatoria:
            acierto = True

    
    if acierto == True:   
          print(f"\n  Felicidades {nombre} eres GANADOR@ de la partida  !!!!\n")
          print(f'\n       La palabra oculta era {palabra_aleatoria.upper()}\n')
          print('          :)  :)  :)  :)  :)  :)\n\n\n')
                    
             
    else:
          self.figura_Ahoracado(intentos)
          print(f"\n        Lo sentimos {nombre} PERDISTE \n")
          print(f'\n       La palabra oculta era {palabra_aleatoria.upper()}.\n')
          print('          :(  :(  :(  :(  :(  :(\n\n\n')
          
    print('')

    self.volver_a_jugar()
              
      
  
  def preguntas_y_respuestas(self, nombre):
    
      intentos_juego = 3
      acertadas = 0
      ronda = 0

      listado_preguntas =  {"¿Cuál es el río más largo de la Península Ibérica? \n\na) Tajo \nb) Guadiana \nc) Ebro \n\n=> " : "a",      "¿Cuál es el país más pequeño del mundo? \n\na) Francia \nb) Portugal \nc) El Vaticano \n\n=>" : "c", 
      "¿Cuántos océanos hay en la Tierra?  \n\na) Cuatro \nb) Cinco \nc) Tres  \n\n=> " : "b",
      "¿Qué país tiene más habitantes? \n\na) España \nb) Austria \nc) China  \n\n=> " : "c",
      "¿Qué país es el más grande del mundo? \n\na) Rusia \nb) Hungría \nc) Italia  \n\n=> " : "a",
      "¿Cuál es la montaña más alta del mundo? \n\na) Everest \nb) Kilimanjaro \nc) Teide  \n\n=> " : "a",
      "¿Cuál es el río más largo del mundo? \n\na) Nilo \nb) Amazonas \nc) Támesis  \n\n=> " : "a",
      "¿Cuál es la capital de Francia?  \n\na) Roma \nb) París \nc) Londres  \n\n=> " : "b",
      "¿Dónde podemos ver las auroras boreales?  \n\na) Finlandia \nb) Suiza \nc) Dinamarca \n\n=> " : "a",
      "¿Cuál es la capital de España? \n\na) Barcelona \nb) Sevilla \nc) Madrid  \n\n=> " : "c"}
      
      os.system("clear")
      
      print("===============================================================================")
      print("=                    _   _   _   _   _   _   _   _                            =")
      print("=                   / \ / \ / \ / \ / \ / \ / \ / \                           =")
      print("=                  ( p | r | e | g | u | t | a | s)                           =")
      print("=                   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                           =")
      print("=                                 _                                           =")
      print("=                                / \                                          =")
      print("=                               | y |                                         =")
      print("=                                \_/                                          =")      
      print("=                 _   _   _   _   _   _   _   _   _   _                       =")
      print("=                / \ / \ / \ / \ / \ / \ / \ / \ / \ / \                      =")
      print("=               ( r | e | s | p | u | e | s | t | a | s )                     =")
      print("=                \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                      =")
      print("=                                                                             =")
      print("===============================================================================")
      
      print(f"\n\n     ¡¡¡ {nombre} bienvenid@ al juego de Preguntas y respuestas !!!\n\n")    
      print("                    ¡¡¡¡   E M P E C E M O S  !!!\n\n\n")
      input('Presiona "ENTER" para continuar')
      os.system("clear")
      
      while intentos_juego > 0 and acertadas < 5:

        os.system("clear")
        ronda +=1

        print("")            
        print("  RONDA", ronda)
        print("*" * 11)
        print('\n')
    
        pregunta = random.choice(list(listado_preguntas.keys()))
        respuesta = input(pregunta).lower()

        while respuesta != 'a' and respuesta != 'b' and respuesta != 'c':
            print("")
            print("")     
            print(f"ERROR! {nombre}, la opción que has intorducido no existe.\n\nVuelve a intentaerlo. Introduce 'a', 'b' o 'c.")
            print("-------------------------------\n\n")
            respuesta = input('=> ')
            
        if respuesta == listado_preguntas.get(pregunta):
            acertadas +=1
            print("")
            print("")
            print(f"Muy bien {nombre}! Has acertado la pregunta. \n\nSigue jugando, ya tienes {acertadas} aciertos")
            print("-------------------------------")
            print("")
            print("")
            
            listado_preguntas.pop(pregunta)

            input('Presiona "ENTER" para continuar')
                  
            if acertadas ==5:
                os.system("clear")
                print("\n")
                print("              ===   ===                      ")
                print("             |  _| |  _|                     ")
                print("             | | | | | |                     ")
                print("              ===   ===   OLEEEEEE!!!        ")
                print("                  O                          ")
                print("               _     _                       ")
                print("                _____                        ")
                print("                                             ")
                print("\n\n")
                print(f"Felicidades {nombre}!!!, has ganado el juego!\n")
                print("=============================================")
        
        
        else:
            intentos_juego -= 1
            if intentos_juego !=0: 
                print("")
                print("")     
                print(f"Has fallado la pregunta {nombre}.\n\nTe quedan {intentos_juego} intentos")
                print("-------------------------------")
                print("")
                print("")
                input('Presiona "ENTER" para continuar')
                
            else:
                os.system("clear")
                print("\n")
                print("               ===   ===          ")
                print("              |  _| |  _|         ")
                print("              | | | | | |         ")
                print("               ===   ===   OHHH!!!")
                print("                   O              ")
                print("                  ---             ")
                print("                 |   |            ")
                print("                  ---             ")
                print("                                  ")
                print("\n\n")
                print(f"Lo sentimos {nombre}, te has quedado sin intentos")
                print("=============================================")
          

      self.volver_a_jugar()
                
  def piedra_papel_tijera(self,nombre):
        
        os.system("clear")
        
        opciones = ("PIEDRA", "PAPEL", "TIJERA")

        rondas = 1
        jugador1_gana = 0
        jugador2_gana = 0

        print(f"\n\n¡¡¡ {nombre} bienvenid@ al juego de Piedra, Papel o Tijera !!!\n\n")
        print(f'                       S U E R T E     \n\n\n')
        self.figura_Piedra_Papel_o_Tijera()
        print('')
        input('Presiona "ENTER" para continuar')
        os.system("clear")
        
        while True:
            os.system("clear")
            self.figura_Piedra_Papel_o_Tijera()

            print("=" * 11)               
            print("  RONDA", rondas)
            print("=" * 11)
            print('')
        
            respuesta_jugador1 = input(f" {nombre} elige una opcion entre Piedra, Papel o Tijera =>  ").upper()
            print("\n")
               
            if respuesta_jugador1 not in opciones:
                print("Esa opción no es válida\n")
                input('Presiona "ENTER" para continuar')
                print('')
                continue
        
            respuesta_jugador2 = random.choice(opciones)

            print(f'Respuesta {nombre}      vs      Respuesta Ordenador')
            print('      |                                |          ')
            print('     \|/                              \|/         ')
            print('      \'                                \'          ')
            print(f'    {respuesta_jugador1}                           {respuesta_jugador2}\n')
        
            if respuesta_jugador1 == respuesta_jugador2:
                print("\nEMPATE!\n")
        
            elif respuesta_jugador1 == "PIEDRA":
                if respuesta_jugador2 == "TIJERA":
                    print("\nPIEDRA gana a TIJERA\n")
                    print(f"{nombre} ganas !!!\n")
                    jugador1_gana +=1
        
                else:
                    print("\nPAPEL gana a PIEDRA\n")
                    print("El Ordenador gana!!!\n")
                    jugador2_gana +=1
        
            elif respuesta_jugador1 == "PAPEL":
                if respuesta_jugador2 == "PIEDRA":
                    print("\nPAPEL gana a PIEDRA\n")
                    print(f"{nombre} ganas !!!\n")
                    jugador1_gana +=1
            
                else:
                    print("\nTIJERA gana a PAPEL\n")
                    print("El Ordenador gana!!!\n")
                    jugador2_gana +=1
             
            elif respuesta_jugador1 == "TIJERA":
                if respuesta_jugador2 == "PAPEL":
                    print("\nTIJERA gana a PAPEL\n")
                    print(f"{nombre} ganas !!!\n")
                    jugador1_gana +=1

                else:
                    print("\nPIEDRA gana a TIJERA\n")
                    print("El Ordenador gana!!!\n")
                    jugador2_gana +=1    
            
            print(f"Marcador {nombre} : ", jugador1_gana)
            print("Marcador Ordenador :", jugador2_gana)
            print('')

            input('Presiona "ENTER" para continuar')
                      
            if jugador1_gana == 3:
                os.system('clear')
                print(f"\nFelicidades {nombre} eres GANADOR@ de la partida  !!!!\n")
                print('              :)  :)  :)  :)  :)  :)\n')
                break
    
            if jugador2_gana == 3:
                os.system('clear')
                print("\nEl ganador de la partida es el Ordenador\n")
                print('        :(  :(  :(  :(  :(  :(\n')
                break
            
            
            rondas +=1
      
        
        self.volver_a_jugar()



    
  def salir (self):
      exit()



  def volver_a_jugar(self):
      volver_a_jugar = 0
      while volver_a_jugar == 0:
        
        print('')
        volver_al_menu = input(f'{nombre}, quieres volver a jugar?\n\nS : sí\n\nN : no\n\n=>  ').upper()

        if volver_al_menu == 'S':
          self.menu()
          volver_a_jugar =1

        elif volver_al_menu == 'N':
            os.system("clear")
            print(f'\n\n   ¡¡¡  Muchas gracias {nombre}  !!! \n\n  Esperamos volver a verte pronto. \n\n       :)  :)  :)  :)  :) '  )
            print('\n\n')
            input('Presiona "ENTER" para continuar')
            os.system("clear")
            self.salir()
            volver_a_jugar=1

        else:
            print('\n\nERROR! La opción introducida no existe.')
            print('\n')    

  def reglas_juego(self):
      os.system("clear")
      self.figura_menu_inicio()
      print('')
      print('''1. PREGUNTAS Y RESPUESTAS:
            
   DESCRIPCIÓN:
    - El juego va a constar de 10 preguntas aleatorias sobre geografía.
    - Cada pregunta tendrá tres opciones de respuesta (a, b, c) y sólo una será correcta.
    - Se obtiene un punto por cada respuesta acertada.

   REGLAS DEL JUEGO:
    - El jugador tendrá dos intentos por cada pregunta.
    - El jugador empieza con 3 vidas y se le restará una cada vez que conteste incorrectamente una pregunta.
    - El juego termina si el jugador pierde todas sus vidas o si responde a 5 preguntas correctamente.
            

2. AHORCADO:
            
   DESCRIPCIÓN:
    - El jugador tiene que adivinar una palabra.
    - El jugador tiene que ir adivinando letras hasta completar la palabra.

   REGLAS DEL JUEGO:
    - El jugador tiene 10 vidas.
    - Por cada fallo se dibuja una parte del cuerpo en la horca y se pierde una vida.
    - El juego termina si el jugador adivina la palabra o si se dibuja el cuerpo entero en la horca y el jugador pierde todas sus vidas.
            
            
3. PIEDRA, PAPEL O TIJERA
            
   DESCRIPCIÓN:
    - Dos jugadores eligen una de las tres opciones: "Piedra", "Papel" o "Tijera"
    - Se obtiene un punto por cada ronda ganada.
    - Gana el jugador que consiga 3 puntos.

   REGLAS DEL JUEGO:
    - Piedra vence a Tijera.
    - Tijera vence a Papel.
    - Papel vence a piedra
            ''')
      print('')
      print("-------------------------------")
      input('Presiona "ENTER" para continuar')
      
      self.menu()
   
  def figura_menu_inicio (self):
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




  def figura_Piedra_Papel_o_Tijera (self):
        print("Piedra:                Papel:                   Tijera:           ")
        print("    _______             _______                  _______          ")
        print("---'   ____)       ---'    ____)____        ---'     ____)____    ")
        print("      (_____)                 ______)                   ______)   ")
        print("      (_____)                _______)              __________)    ")
        print("      (____)                 _______)             (____)          ")
        print("---.__(___)        ---.__________)          ---.__(___)           ")
        print("\n")

  def figura_Ahoracado(self, vidas):
        figura=[
         '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        /|\\
          |       / | \\
          |        / \\
          |       /   \\
         ==================''',
           '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        /|\\
          |       / | \\
          |        /
          |       /  
         ==================''',
                '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        /|\\
          |       / | \\
          |         |
          |          
         ==================''',
                '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        / \\
          |       /   \\ 
          |         
          |          
         ==================''',
                '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |        /   
          |       /   
          |        
          |        
         ==================''',
                  '''
          +---------+
          |        _|_
          |        |__|
          |         | 
          |          
          | 
          |         
          |        
         ==================''',
                  '''
          +---------+
          |        _|_
          |        |__|
          |        
          |          
          |         
          |   
          |     
         ==================''',
                    '''
          +---------+
          |         |
          |        
          |        
          |          
          |         
          |
          |
         ==================''',
                        '''
          +
          |         
          |         
          |        
          |        
          |                  
          |
          |
         ==================''',
                            '''
                   
              
              
                       
      
                            


         ==================''','''         
              
              
                       
      
                            


                  
         ------------------''']
        
        print(figura[vidas])
      
      
  
class Jugadores:
  
  def __init__(self):
    self.lista_jugadores = []
  
  def alta_jugador(self,nombre, equipo):
      if nombre not in self.lista_jugadores:
        jugador = Jugador(nombre, equipo)
        self.lista_jugadores.append(nombre)
      else:
        pass

class Jugador:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo

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
juego.menu()

#*MEJORA EN PROCESO: Registro de jugadores.
#Creamos un registro de jugadores para registrar las rachas ganadas y puntuaciones:

lista_jugadores=Jugadores()
lista_jugadores.alta_jugador(nombre,equipo)

