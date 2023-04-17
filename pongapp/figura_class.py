import pygame as pg
from .old_utils import * 


class Raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=120,color=BLANCO,vx=1,vy=1 ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy
        
        self.file_imagenes = {
            'drcha':['electric00_drcha.png','electric01_drcha.png','electric02_drcha.png'],
            'izqda': ['electric00_izqda.png','electric01_izqda.png','electric02_izqda.png'],
        }
        self.imagenes = self.cargar_imagenes()#llamo al metodo que devuelve la incializacion de imagenes
        self._direccion = ''#variable para asignar direccion
        self.imagen_activa = 0#variable para indicar repeticion

       

    def cargar_imagenes(self):
        imagenprueba={}
        for lado in self.file_imagenes:
            imagenprueba[lado]=[]
            for nombre_fichero in self.file_imagenes[lado]:
                imagen = pg.image.load(f"pongapp/images/raquetas/{nombre_fichero}")
                imagenprueba[lado].append(imagen)
        return imagenprueba        

    @property    
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self,valor):
        self._direccion=valor

    def dibujar(self,pantalla):
        #pantalla.blit(self.raqueta,( self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h ) )
        #pg.draw.rect(pantalla, self.color,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h) )
        pantalla.blit(self.imagenes[self.direccion][self.imagen_activa],(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h))
        self.imagen_activa +=1
        if self.imagen_activa >= len(self.imagenes[self.direccion]):
            self.imagen_activa = 0


    def mover(self,tecla_arriba,tecla_abajo,y_max=Y_MAX,y_min=Y_MIN):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[tecla_arriba] == True and self.pos_y > y_min+(self.h//2):
            self.pos_y -=1

        if estado_teclado[tecla_abajo] == True and self.pos_y < y_max-(self.h//2):
            self.pos_y +=1
    @property
    def derecha(self):
        return self.pos_x+(self.w//2)
    @property
    def izquierda(self):
        return self.pos_x-(self.w//2)
    @property
    def arriba(self):
        return self.pos_y -(self.h//2)
    @property
    def abajo(self):
        return self.pos_y +(self.h//2)

class Pelota:
    def __init__(self,pos_x,pos_y,color=BLANCO,radio=20,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.sonido = pg.mixer.Sound(SONIDO_PELOTA)
    
      

    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio )
      

    def mover(self,x_max=X_MAX,y_max=Y_MAX,x_min=X_MIN,y_min=Y_MIN):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if (self.pos_y >= y_max-self.radio) or (self.pos_y < y_min+self.radio):#rebote en eje y
            self.vy *= -1
        
        if self.pos_x >= x_max+self.radio*10:#limite derecho
            #self.contadorIzquierdo +=1

            self.pos_x=x_max//2
            self.pos_y=y_max//2

            self.vx *= -1
            self.vy *= -1
            
            return "left"
        
        if self.pos_x < x_min-self.radio*10:#limite izquierdo
            #self.contadorDerecho +=1
            
            self.pos_x=x_max//2
            self.pos_y=y_max//2

            self.vx *= -1
            self.vy *= -1

            return "right"

            

    

    @property
    def derecha(self):
        return self.pos_x + self.radio
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    @property
    def arriba(self):
        return self.pos_y -self.radio
    @property
    def abajo(self):
        return self.pos_y + self.radio

    def comprobar_choque(self,r1,r2):
        if self.derecha >= r2.izquierda and\
            self.izquierda <= r2.derecha and\
            self.abajo >= r2.arriba and\
            self.arriba <= r2.abajo:
                self.vx *= -1
                pg.mixer.Sound.play(self.sonido)

        if self.derecha >= r1.izquierda and\
            self.izquierda <= r1.derecha and\
            self.abajo >= r1.arriba and\
            self.arriba <= r1.abajo:
                self.vx *= -1
                pg.mixer.Sound.play(self.sonido)        

    def comprobar_choqueV2(self,*raquetas):
        for r in raquetas:
            if self.derecha >= r.izquierda and\
               self.izquierda <= r.derecha and\
               self.abajo >= r.arriba and\
               self.arriba <= r.abajo:
                    self.vx *= -1