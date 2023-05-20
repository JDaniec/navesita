from tkinter import *
import random

# variables
BASE = 560
ALTURA = 320
TAM_MIN = 10
TAM_MAX = 40
VELOCIDAD = 5

# Función para mover la imagen hacia arriba
def mover_arriba(event=None):
    global imagen_canvas
    x, y = c.coords(imagen_canvas)  # Obtener solo las coordenadas x e y
    if y <= 0:
        c.move(imagen_canvas, 0, ALTURA)
    else:
        c.move(imagen_canvas, 0, -VELOCIDAD)

# Función para mover la imagen hacia abajo
def mover_abajo(event=None):
    global imagen_canvas
    x, y = c.coords(imagen_canvas)  # Obtener solo las coordenadas x e y
    if y >= ALTURA:
        c.move(imagen_canvas, 0, -ALTURA)
    else:
        c.move(imagen_canvas, 0, VELOCIDAD)

# Función para mover la imagen hacia la izquierda
def mover_izquierda(event=None):
    global imagen_canvas
    x, y = c.coords(imagen_canvas)  # Obtener solo las coordenadas x e y
    if x <= 0:
        c.move(imagen_canvas, BASE, 0)
    else:
        c.move(imagen_canvas, -VELOCIDAD, 0)

# Función para mover la imagen hacia la derecha
def mover_derecha(event=None):
    global imagen_canvas
    x, y = c.coords(imagen_canvas)  # Obtener solo las coordenadas x e y
    if x >= BASE:
        c.move(imagen_canvas, -BASE, 0)
    else:
        c.move(imagen_canvas, VELOCIDAD, 0)

# ventana principal de la app
ventana_principal = Tk()
ventana_principal.title("Canvas")
ventana_principal.geometry("600x510")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

frame1 = Frame(ventana_principal)
frame1.config(width=580, height=350, bg="Royalblue1")
frame1.place(x=10, y=10)

frame2 = Frame(ventana_principal)
frame2.config(width=580, height=130, bg="Royalblue1")
frame2.place(x=10, y=370)

c = Canvas(frame1, width=BASE, height=ALTURA)
c.place(x=7, y=10)
c.config(bg="black")

# lista para almacenar las coordenadas de los círculos generados
coordenadas_circulos = []
circulos = []

# graficacion
for i in range(30):
    x = random.randint(0, BASE - TAM_MAX)
    y = random.randint(0, ALTURA - TAM_MAX)
    tam = random.randint(TAM_MIN, TAM_MAX)
    color = "#"
    for i in range(6):
        color += random.choice("0123456789ABCDEF")

    # Verificar superposición con los círculos existentes
    superposicion = False
    for circulo in circulos:
        coords = c.coords(circulo)
        if (x + tam >= coords[0] and x <= coords[2] and
                y + tam >= coords[1] and y <= coords[3]):
            superposicion = True
            break

    # Crear el círculo solo si no hay superposición
    if not superposicion:
        circulo = c.create_oval(x, y, x + tam, y + tam, fill=color)
        circulos.append(circulo)
        coordenadas_circulos.append((x, y, tam))

imagen = PhotoImage(file="img/navea.png")

# Obtener las dimensiones de la imagen
ancho_imagen = imagen.width()
alto_imagen = imagen.height()

# Calcular las coordenadas para insertar la imagen en el canvas
x_imagen = (BASE - ancho_imagen) // 2
y_imagen = (ALTURA - alto_imagen) // 2

# Insertar la imagen en el canvas
imagen_canvas = c.create_image(x_imagen, y_imagen, anchor=NW, image=imagen)

# Botón "Subir"
bt_subir = Button(frame2, text="🢁", command=mover_arriba)
bt_subir.place(x=280, y=5, width=40, height=40)

# Botón desplazarse derecha
bt_derecha = Button(frame2, text="🢂", command=mover_derecha)
bt_derecha.place(x=320, y=45, width=40, height=40)

# Botón desplazarse izquierda
bt_izquierda = Button(frame2, text="🢀", command=mover_izquierda)
bt_izquierda.place(x=240, y=45, width=40, height=40)

# Botón bajar
bt_bajar = Button(frame2, text="🢃", command=mover_abajo)
bt_bajar.place(x=280, y=85, width=40, height=40)

# Enlazar eventos de teclado a las funciones de movimiento
ventana_principal.bind("<Up>", mover_arriba)
ventana_principal.bind("<Down>", mover_abajo)
ventana_principal.bind("<Left>", mover_izquierda)
ventana_principal.bind("<Right>", mover_derecha)

ventana_principal.mainloop()

























