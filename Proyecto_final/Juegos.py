import random
import os
 

class Juegos:

  def ahorcado():
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
    ==================''',
              '''
      +---------+
      |        _|_
      |        |__|
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
    ==================''',
                    '''
      +
      |         
      |         
      |        
      |        
      |                  
      |
    ==================''',
                        '''
               
              
              
                       
      
    ==================''','']
  
  
    def __init__():
      pass
  
    os.system("clear")
    
    print("=================================================================================")
    print("=                      _   _   _   _   _   _   _   _                            =")
    print("=                     / \ / \ / \ / \ / \ / \ / \ / \                           =")
    print("=                    ( a | h | o | r | c | a | d | o )                          =")
    print("=                     \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                           =")
    print("=                                                                               =")
    print("=================================================================================")

        
    print ("Bienvenido al juego del ahorcado.\nEl juego consiste en adivinar la palabra oculta letra a letra.\n\n          ¡¡¡¡ EMPEZEMOS!!!")


    palabra_aleatoria = random.choice(palabras_aleatorias).lower()  
    palabra_guiones = "_"*len(palabra_aleatoria)
    lista_palabra=list(palabra_aleatoria)
    lista_guiones=list(palabra_guiones)


    
    while 0 < intentos <= 10 and acierto==False:

      # Imprimir guiones sin letras
    
        print(f"\nEstas son las letras ocultas de la palabra:   {' '.join(lista_guiones)}")
        print('-------------------------------------------------------')

      # preguntar al usuario la ltera
        letra=input("Introduce una letra a ver si está en la palabra.").lower()

        if letra in lista_palabra:

          print(f'Genial! la letra {letra.upper()} está en la palabra oculta.')
          
          aux=0 
          for i in lista_palabra:      
            if i == letra:
                lista_guiones[aux]=letra

            aux += 1
            
        else:
            intentos-=1
            print(f'No, la letra {letra.upper()} no está. Te quedan {intentos} intentos.')
    
      # LETRAS ACERTADAS en el espacio correspondiente en lugar de guiones  
        palabra_jugada = ''.join(lista_guiones)
    
      # Imprimir las letras usadas
        letra_usada.append(letra)
        print(f'Las letras usadas hasta ahora son: {letra_usada}')

        print (figura[intentos])

        if palabra_jugada == palabra_aleatoria:
            acierto = True

    
    if acierto == True:   
          print("\n")  
          print('    ¡¡¡¡¡ GANASTE !!!!!')
          print(f'\nLa palabra oculta era {palabra_aleatoria.upper()}.')
          print("\n") 
          print("\n")
          
             
    else:
          print("\n")
          print('      :(  PERDISTE    :( ')
          print(f'\nLa palabra oculta era {palabra_aleatoria.upper()}.')
          print("\n")
      
  
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
      
                
  def piedra_papel_tijera():
        
        os.system("clear")
        
        print("\n")
        print("\n")
        print("Piedra:                Papel:                   Tijera:           ")
        print("    _______             _______                  _______          ")
        print("---'   ____)       ---'    ____)____        ---'     ____)____    ")
        print("      (_____)                 ______)                   ______)   ")
        print("      (_____)                _______)              __________)    ")
        print("      (____)                 _______)             (____)          ")
        print("---.__(___)        ---.__________)          ---.__(___)           ")
        print("\n")
      
        opciones = ("piedra", "papel", "tijera")

        jugador1 = "usuario"
        jugador2 = "ordenador"
        rondas = 1
        jugador1_gana = 0
        jugador2_gana = 0

        print("Bienvenido al juego de Piedra, Papel o Tijera")

        while True:
    
            print("=" * 20 + "\n")
            
            print("RONDA", rondas)
            print("=" * 20 + "\n")
    
            print("Marcador Jugador : ", jugador1_gana)
            print("Marcador Ordenador :", jugador2_gana)
    
            respuesta_jugador1 = input("Elige una opcion entre piedra, papel o tijera =>  ")
            print("\n")
            respuesta_jugador1 = respuesta_jugador1.lower()
   
            if respuesta_jugador1 not in opciones:
                print("Esa opción no es válida")
                continue
        
            respuesta_jugador2 = random.choice(opciones)
    
            print("Respuesta jugador =>", respuesta_jugador1)
            print("\n")
            print("Respuesta Ordenador =>", respuesta_jugador2)
    
            if respuesta_jugador1 == respuesta_jugador2:
                print("\n")
                print("Empate!")
        
            elif respuesta_jugador1 == "piedra":
                if respuesta_jugador2 == "tijera":
                    print("\n")
                    print("Piedra gana a tijera")
                    print("\n")
                    print("El jugador gana!!!")
                    jugador1_gana +=1
        
                else:
                    print("\n")
                    print("Papel gana a piedra")
                    print("\n")
                    print("El Ordenador gana!!!")
                    jugador2_gana +=1
        
            elif respuesta_jugador1 == "papel":
                if respuesta_jugador2 == "piedra":
                    print("\n")
                    print("Papel gana a piedra")
                    print("\n")
                    print("El Jugador gana!!!")
                    print("\n")
                    jugador1_gana +=1
            
                else:
                    print("\n")
                    print("Tijera gana a papel")
                    print("\n")
                    print("El Ordenador gana!!!")
                    print("\n")
                    jugador2_gana +=1
             
            elif respuesta_jugador1 == "tijera":
                if respuesta_jugador2 == "papel":
                    print("\n")
                    print("Tijera gana papel")
                    print("\n")
                    print("El Jugador gana!!!")
                    print("\n")
                    jugador1_gana +=1
            
            else:
                print("\n")
                print("Piedra gana a tijera")
                print("\n")
                print("El Ordenador gana!!!")
                print("\n")
                jugador2_gana +=1
            
            if jugador1_gana == 3:
                print("\n")
                print("El ganador de la partida es el Jugador")
                print("\n")
                break
    
            if jugador2_gana == 3:
                print("\n")
                print("El ganador de la partida es el Ordenador")
                print("\n")
                break

            rondas +=1
      
      
    
  def salir ():
      exit()
  
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