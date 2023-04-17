import pygame as pg
from pongapp.figura_class import Pelota,Raqueta
from .utils import *


class Partida:
   
    def __init__(self,pantalla,tasa_refresco):
        self.pantalla_principal=pantalla
        self.tasa_refresco=tasa_refresco

        self.pelota = Pelota(ANCHO//2,ALTO//2)
        self.raqueta1 = Raqueta( 10,ALTO//2 )
        self.raqueta1.direccion='izqda'
        self.raqueta2 = Raqueta(ANCHO-20,ALTO//2)
        self.raqueta2.direccion='drcha'
        self.fuente1 = pg.font.Font(FUENTE1, 20)
        self.fuente2 = pg.font.Font(FUENTE2, 20)

        self.contadorDerecho=0
        self.contadorIzquierdo=0
        self.quienMarco=""
        self.temporizador=TIEMPO
        self.game_over = False
        self.contadorFotograma=0
        self.colorFondo=COLOR_CANCHA
        self.resultado_partida=""
        

    def bucle_pantalla(self):
        #para inicializar parametros del juego
        self.temporizador=TIEMPO
        self.tasa_refresco.tick()
        self.contadorDerecho=0
        self.contadorIzquierdo=0

        while not self.game_over and (self.contadorDerecho<10 or self.contadorIzquierdo<10) and self.temporizador > 0:

            salto_tiempo = self.tasa_refresco.tick(FTS)#1000/380 = cantidad de fotograma por segundo
            self.fin_de_partida()
            self.temporizador -= salto_tiempo
           
          
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #self.game_over = True
                    return True

            self.raqueta1.mover(pg.K_w,pg.K_s)#raqueta izquierda
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)#raqueta derecha
            self.quienMarco = self.pelota.mover()

            
            color = self.fijar_fondo()
            self.pantalla_principal.fill(color=color)

            self.mostrar_linea_central()
            
            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

           

            self.pelota.comprobar_choque(self.raqueta1,self.raqueta2)
            

            self.mostrar_marcador()
            self.mostrar_jugador()
            self.mostrar_temporizador()

            pg.display.flip()
            
        return self.resultado_partida    
        

    def mostrar_jugador(self):
        jugador1 = self.fuente2.render("Jugador 1",0,NARANJA)
        jugador2 = self.fuente2.render("Jugador 2",0,NARANJA)  
        self.pantalla_principal.blit(jugador1,(150,20))
        self.pantalla_principal.blit(jugador2,(550,20))

    def mostrar_linea_central(self):
        '''
        cont_linea=0
        while cont_linea <= 660:
        pg.draw.line(self.pantalla_principal,BLANCO,(ANCHO//2,cont_linea),(ANCHO//2,cont_linea+50),10 )
        cont_linea += 70
        '''
        for i in range(0,661,70):
            pg.draw.line(self.pantalla_principal,BLANCO,(ANCHO//2,i),(ANCHO//2,i+50),10 )

    def mostrar_marcador(self):
        if self.quienMarco =="right":
            self.contadorDerecho += 1
        elif self.quienMarco == "left":
            self.contadorIzquierdo +=1   
        jugador1 = self.fuente1.render(str(self.contadorIzquierdo),0,AMARILLO)
        jugador2 = self.fuente1.render(str(self.contadorDerecho),0,AMARILLO)     
        self.pantalla_principal.blit(jugador1,(200,50))
        self.pantalla_principal.blit(jugador2,(ALTO,50))

    def mostrar_temporizador(self):
        tiempo_juego= self.fuente1.render( str( int(self.temporizador/1000) ),0,GRANATE)
        self.pantalla_principal.blit(tiempo_juego,(ANCHO//2-10,30))

    def fin_de_partida(self):
        if self.contadorDerecho > self.contadorIzquierdo:
            self.resultado_partida= f"Gana el Jugador 2, resultado Jugador2:{self.contadorDerecho}, Jugador1:{self.contadorIzquierdo}"
        elif self.contadorIzquierdo > self.contadorDerecho:
            self.resultado_partida=f"Gana el Jugador 1, resultado Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"
        else:
            self.resultado_partida= f"Empate entre Jugador 1 y Jugador 2, resultado Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"     
        
        
        """
        if self.temporizador <= 0:
            self.game_over = True

            if self.contadorDerecho > self.contadorIzquierdo:
                self.resultado_partida= f"Gana el Jugador 2, resultado Jugador2:{self.contadorDerecho}, Jugador1:{self.contadorIzquierdo}"
            elif self.contadorDerecho < self.contadorIzquierdo:
                self.resultado_partida=f"Gana el Jugador 1, resultado Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"
            else:
                self.resultado_partida= f"Empate entre Jugador 1 y Jugador 2, resultado Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"

        if self.contadorDerecho == 10:
            self.game_over = True
            self.resultado_partida= "Gana el Jugador 2"
        if self.contadorIzquierdo == 10:    
            self.game_over = True
            self.resultado_partida= "Gana el Jugador 1"
        """          
    
    def fijar_fondo(self):
        self.colorFondo= COLOR_CANCHA
        self.contadorFotograma += 1
        #print("contador fotograma: ",self.contadorFotograma)

        if self.temporizador > TIEMPO_LIMIT_1:
            self.contadorFotograma=0
        elif self.temporizador > TIEMPO_LIMIT_2:
            if self.contadorFotograma ==10:
                if self.colorFondo ==COLOR_CANCHA:
                    self.colorFondo = NARANJA_OSCURO
                else:
                    self.colorFondo= COLOR_CANCHA
                self.contadorFotograma=0
        else:
              if self.contadorFotograma ==10:
                if self.colorFondo ==COLOR_CANCHA:
                    self.colorFondo = ROJO
                else:
                    self.colorFondo= COLOR_CANCHA
                self.contadorFotograma=0      

        return self.colorFondo                
        """
        if self.temporizador < 10000 and self.temporizador >=5000:
            self.pantalla_principal.fill(NARANJA_OSCURO)
            #cambiarian si es verde a naranja y viceversa
        elif self.temporizador <=5000:
            self.pantalla_principal.fill(ROJO)
            #cambiarian si es verde a rojo y viceversa
        else:
            self.pantalla_principal.fill(COLOR_CANCHA)
            self.contadorFotograma =0
        """    

class Menu:
    
    def __init__(self,pantalla,tasa_refresco):
        self.pantalla_principal= pantalla
        self.tasa_refresco= tasa_refresco

        self.imagenFondo = pg.image.load(IMG_FONDO)
        self.fuenteMenu = pg.font.Font(FUENTE1,20)
        self.sonido = pg.mixer.Sound(SONIDO_AMBIENTE)#definimos el sonido

    def bucle_pantalla(self):
        game_over=False
        self.tasa_refresco.tick(FTS)

        pg.mixer.Sound.play(self.sonido)#iniciamos el sonido

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True

            

            """
            boton = pg.key.get_pressed()
            if boton[pg.K_r] == True:
                game_over = True
                pg.mixer.Sound.stop(self.sonido)#paramos el sonido
                return "records"
            if boton[pg.K_RETURN] == True:
                game_over = True
                pg.mixer.Sound.stop(self.sonido)#paramos el sonido
                return "partida"  
            """    
            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            jugar = self.fuenteMenu.render("Pulsa ENTER para jugar",0,GRANATE)
            records = self.fuenteMenu.render("Pulsar R para ver Records",0,AMARILLO)
               
            self.pantalla_principal.blit(jugar,(155,ALTO//2))
            self.pantalla_principal.blit(records,(155,ALTO//2+40))

            pg.display.flip()             

        pg.mixer.Sound.stop(self.sonido)#paramos el sonido

class Resultado:

    def __init__(self,pantalla,tasa_refresco):
        self.pantalla_principal = pantalla
        self.tasa_refresco = tasa_refresco

        self.fuenteResultado = pg.font.Font(FUENTE1,10)
        self.resultado_final = ""
        
    def bucle_pantalla(self):
        game_over = False
        self.tasa_refresco.tick(FTS)

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True
            
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
            
            self.pantalla_principal.fill(BLANCO)
            resultado = self.fuenteResultado.render(self.resultado_final,0,GRANATE)

            self.pantalla_principal.blit(resultado,(120,ALTO//2))

            pg.display.flip()
       

    def cargarResultado(self,resultado):
        self.resultado_final = resultado                       

class Records:
    def __init__(self,pantalla,tasa_refresco):
        self.pantalla_principal= pantalla
        self.tasa_refresco= tasa_refresco
        
        self.fuenteRecords = pg.font.Font(FUENTE1,20)

    def bucle_pantalla(self):
        self.tasa_refresco.tick(FTS)
        game_over=False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True

            self.pantalla_principal.fill(BLANCO)
            texto = self.fuenteRecords.render("Mejores puntajes",0,GRANATE)
      
            self.pantalla_principal.blit(texto,(155,ALTO//2))

            pg.display.flip()             

        