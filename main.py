import turtle as t
import time
import random 
class SnakeGame():
    def __init__(self, width=600, height=600, color="black"):
     """Inicializamos los componentes del juego"""
     #inicializamos la pantalla
     self.screen = t.Screen()
     self.screen.title("Snake Game")
     self.screen.bgcolor(color)
     self.screen.setup(width=width, height=height)
     self.screen.tracer(0)
     self._ancho = width
     self._alto = height


     #inicializa la serpiente
     self.snake = t.Turtle()
     self.snake.speed(0)
     self.snake.shape("square")
     self.snake.color("red")
     self.snake.penup()
     self.snake.goto(0,0)
     
    #inicializar el texto que se muestra en pantalla
     self.txt = t.Turtle()
     self.txt.speed(0)
     self.txt.hideturtle()
     self.txt.shape("square")
     self.txt.color("white")
     self.txt.penup()
     self.txt.goto(0,(height / 2) - 40)

    #inicializamos la comida
     self.comida = t.Turtle()
     self.comida.speed(0)
     self.comida.color("#03bb85")
     self.comida.shape("circle")
     self.comida.penup()
     self.comida.goto(0, 200)


    #Atributos de la clase
     self._direccion = None
     self._delay = 0.1
     self._score = 0
     self._puntos = 0
     self.snake_cuerpo = []
    #Asociacion de los movimientos de las teclas
     self.screen.listen()
     self.screen.onkeypress(self.arriba, "w")
     self.screen.onkeypress(self.abajo, "s")
     self.screen.onkeypress(self.izquierda, "a")
     self.screen.onkeypress(self.derecha, "d")
    #sacamos el texto por pantalla
     self._print_score()
    

    
    def arriba(self):
       """Este metodo define el movimiento haci arriba de la serpiente"""
       if self._direccion != "abajo":
          self._direccion = "arriba"
    def abajo(self):
       """Este metodo define el movimiento de la serpiente hacia abajo"""
       if self._direccion != "arriba":
          self._direccion = "abajo"

    def izquierda(self):
       """Este metodo define el movimiento haci la derecha de la serpiente"""
       if self._direccion != "derecha":
          self._direccion = "izquierda"
    def derecha(self):
       """Este metodo define el movimiento de la serpiente hacia abajo"""
       if self._direccion != "izquierda":
          self._direccion = "derecha"
    
    def movimiento(self):
       #obtener las cordenadas de la cabeza de la serpiente
       hx, hy = self.snake.xcor(), self.snake.ycor()

       #mover el cuerpo de la serpiente
       for i in range(len(self.snake_cuerpo)-1,0,-1):
         x = self.snake_cuerpo[i-1].xcor()
         y = self.snake_cuerpo[i-1].ycor()
         self.snake_cuerpo[i].goto(x,y)

       #mover el segmento mas cercano a la cabeza
       if len(self.snake_cuerpo) > 0:
          self.snake_cuerpo[0].goto(hx,hy)

       if self._direccion == "arriba":
          self.snake.sety(hy + 20)
       elif self._direccion == "abajo":
          self.snake.sety(hy -20)
       elif self._direccion == "izquierda":
          self.snake.setx(hx - 20)
       elif self._direccion == "derecha":
          self.snake.setx(hx + 20)

    def colision(self):
       bxcor = (self._ancho // 2) - 10
       bycor = (self._alto // 2) - 10
       if self.snake.xcor() > bxcor or self.snake.xcor() < -bxcor or self.snake.ycor() > bycor or self.snake.ycor() < -bycor:
         self._reset()

    def colision_cuerpo(self):
      #colision con el cuerpo
      for x in self.snake_cuerpo:
         if x.distance(self.snake) < 20:
            self._reset()

    def colision_comida(self):
       if self.snake.distance(self.comida) < 20:
          bxcor = (self._ancho // 2) - 10
          bycor = (self._alto // 2) - 10
          x = random.randint(-bxcor, bxcor)
          y = random.randint(-bycor, bycor)
          self.comida.goto(x,y)
          #incrementar el cuerpo de la serpiente
          self.incrementar_cuerpo()
          #reducir el delay cada vez que come
          self._delay -= 0.001
          #aumentar los puntos
          self._puntos += 10
          self._print_score()

    def _reset(self):
      time.sleep(1)
      self.snake.goto(00,00)
      self._direccion = None
      self.txt.clear()
      #reiniciar la serpiente
      for s in self.snake_cuerpo:
         s.ht() #Ocultar el segmento
      #limpiar la lista de segmentos
      self.snake_cuerpo.clear()
      #reiniciar el delay
      self._delay = 0.1
      #reiniciar los puntos
      if self._puntos > self._score:
         self._score = self._puntos
      self._puntos = 0
      #mostramos la puntuacion
      self._print_score()

     
    def incrementar_cuerpo(self):
       segmento = t.Turtle()
       segmento.speed(0)
       segmento.shape("square")
       segmento.color("green")
       segmento.penup()
       self.snake_cuerpo.append(segmento)

       

         
    def dibujar_borde(self):
     borde = t.Turtle()
     borde.hideturtle()
     borde.color("white")  # Color del borde
     borde.penup()
     borde.goto(-self._ancho/2, self._alto/2)
     borde.pendown()
     borde.pensize(3)  # Grosor del borde

     for _ in range(4):
        if _ % 2 == 0:
            borde.forward(self._ancho)
        else:
            borde.forward(self._alto)
        borde.right(90)
          
          
    def _print_score(self):
       self.txt.clear()
       self.txt.write(f"Puntos: {self._puntos} Record: {self._score}", align="center", font=("Courier", 24, "normal"))

       
    def jugar(self):
       try:
         self.dibujar_borde()
         while True:
            self.screen.update()
            self.colision()
            self.colision_comida()
            self.colision_cuerpo()
            time.sleep(self._delay)
            self.movimiento()
       except t.Terminator:
        self.screen.mainloop()
        print("Juego terminado")
          
    
juego = SnakeGame()
juego.jugar()



