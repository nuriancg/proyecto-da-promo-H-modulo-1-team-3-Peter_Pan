import random
import os
 

class Juegos:

  def __init__(self,nombre,equipo):
      
      self.nombre = nombre
      self.equipo = equipo
      pass

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
    print("                     ¡¡¡¡   E M P E Z E M O S  !!!\n\n\n")
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
          
          aux=0 
          for i in lista_palabra:      
            if i == letra:
                lista_guiones[aux]=letra

            aux += 1
            
        else:
            intentos-=1
            print(f'\n\nNo, la letra {letra.upper()} no está.\n\n{nombre} te quedan {intentos} intentos.')
    
      # LETRAS ACERTADAS en el espacio correspondiente en lugar de guiones  
        palabra_jugada = ''.join(lista_guiones)
    
      # Imprimir las letras usadas
        letra_usada.append(letra)
        letra_usada.sort()
        # print(f'\n\nLas letras usadas hasta ahora son: {letra_usada}\n\n')

        print('\n\n\n')
        input('Presiona "ENTER" para continuar')
        os.system("clear")

        if palabra_jugada == palabra_aleatoria:
            acierto = True

    
    if acierto == True:   
          print(f"\n  Felicidades {nombre} eres GANADOR@ de la partida  !!!!\n")
          print(f'\n       La palabra oculta era {palabra_aleatoria.upper()}\n')
          print('          :)  :)  :)  :)  :)  :)\n\n')
          
             
    else:
          self.figura_Ahoracado(intentos)
          print(f"\n        Lo sentimos {nombre} PERDISTE \n")
          print(f'\n       La palabra oculta era {palabra_aleatoria.upper()}.\n')
          print('          :(  :(  :(  :(  :(  :(\n\n')
      
  
  def preguntas_y_respuestas():
    
      intentos_juego = 3
      acertadas = 0

      listado_preguntas =  {"¿Cuál es el río más largo de la Península Ibérica? a) Tajo b) Guadiana c) Ebro   " : "a",
      "¿Cuál es el país más pequeño del mundo? a) Francia b) Portugal c) El Vaticano   " : "c", 
      "¿Cuántos océanos hay en la Tierra?  a) Cuatro b) Cinco c) Tres   " : "b",
      "¿Qué país tiene más habitantes? a) España b) Austria c) China  " : "c",
      "¿Qué país es el más grande del mundo? a) Rusia b) Hungría c) Italia.   " : "a",
      "¿Cuál es la montaña más alta del mundo? a) Everest b) Kilimanjaro c) Teide   " : "a",
      "¿Cuál es el río más largo del mundo? a) Nilo b) Amazonas c) Támesis   " : "a",
      "¿Cuál es la capital de Francia?  a) Roma b) París c) Londres   " : "b",
      "¿Dónde podemos ver las auroras boreales?  a) Finlandia b) Suiza c) Dinamarca   " : "a",
      "¿Cuál es la capital de España? a) Barcelona b) Sevilla c) Madrid   " : "c"}
      
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
      print("\n")
      print("\n")
      
      while intentos_juego > 0 and acertadas < 5:
    
        pregunta = random.choice(list(listado_preguntas.keys()))
        respuesta = input(pregunta)
    
       
        if respuesta == listado_preguntas.get(pregunta):
            acertadas +=1
            print("")
            print("")
            print(f"Has acertado la pregunta. Sigue jugando, ya tienes {acertadas} aciertos")
            print("=======================================")
            print("")
            print("")
            
            listado_preguntas.pop(pregunta)
            
            if acertadas ==5:
                print("\n")
                print("    ===   ===                      ")
                print("   |  _| |  _|                     ")
                print("   | | | | | |                     ")
                print("    ===   ===   OLEEEEEE!!!        ")
                print("        O                          ")
                print("     _     _                       ")
                print("      _____                        ")
                print("                                   ")
                print("Felicidades!!!, has ganado el juego")
                print("===================================")
    
        else:
            intentos_juego -= 1
            if intentos_juego !=0: 
                print("")
                print("")     
                print(f"Has fallado la pregunta, te quedan {intentos_juego} intentos")
                print("=============================================================")
                print("\n")
                print("")
            else:
                print("\n")
                print("    ===   ===          ")
                print("   |  _| |  _|         ")
                print("   | | | | | |         ")
                print("    ===   ===   OHHH!!!")
                print("        O              ")
                print("       ---             ")
                print("      |   |            ")
                print("       ---             ")
                print("Te has quedado sin intentos")
      
                
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
            
            self.figura_Piedra_Papel_o_Tijera()

            print("=" * 11)               
            print("  RONDA", rondas)
            print("=" * 11)
        
            respuesta_jugador1 = input(f" {nombre} elige una opcion entre Piedra, Papel o Tijera =>  ").upper()
            print("\n")
               
            if respuesta_jugador1 not in opciones:
                print("Esa opción no es válida\n")
                input('Presiona "ENTER" para continuar')
                print('')
                os.system("clear")
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
                      
            if jugador1_gana == 3:
                print(f"\nFelicidades {nombre} eres GANADOR@ de la partida  !!!!\n")
                print('              :)  :)  :)  :)  :)  :)\n\n')
                break
    
            if jugador2_gana == 3:
                print("\nEl ganador de la partida es el Ordenador\n")
                print('        :(  :(  :(  :(  :(  :(\n\n')
                break
            
            input('Presiona "ENTER" para continuar')
            print('')
            os.system("clear")

            rondas +=1
      
      
    
  def salir ():
      exit()

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