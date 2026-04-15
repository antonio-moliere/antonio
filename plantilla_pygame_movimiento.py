# Plantilla básica para mover objetos con el teclado en Pygame
# Basada en la estructura de programarcadegames.com

import pygame

# --- Colores (R, G, B) ---
NEGRO   = (  0,   0,   0)
BLANCO  = (255, 255, 255)
ROJO    = (255,   0,   0)
VERDE   = (  0, 255,   0)
AZUL    = (  0,   0, 255)
AMARILLO= (255, 255,   0)
NARANJA = (255, 165,   0)

# --- Inicialización de Pygame ---
pygame.init()

# --- Tamaño de la ventana ---
ANCHO = 700
ALTO  = 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# --- Título de la ventana ---
pygame.display.set_caption("Movimiento con teclado")

# -------------------------------------------------------
# POSICIÓN Y VELOCIDAD del objeto
# -------------------------------------------------------
objeto_x = ANCHO // 2   # posición horizontal inicial (centro)
objeto_y = ALTO  // 2   # posición vertical inicial (centro)
velocidad = 4           # píxeles que se mueve por fotograma

# -------------------------------------------------------
# TAMAÑO del objeto (modifícalo a tu gusto)
# -------------------------------------------------------
RADIO = 25              # radio del círculo que usamos como objeto

# --- Bucle principal ---
hecho = False
reloj = pygame.time.Clock()

while not hecho:

    # 1) Gestión de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # -------------------------------------------------------
    # 2) LEER EL ESTADO DEL TECLADO y actualizar la posición
    # -------------------------------------------------------
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]  or teclas[pygame.K_a]:
        objeto_x -= velocidad
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        objeto_x += velocidad
    if teclas[pygame.K_UP]    or teclas[pygame.K_w]:
        objeto_y -= velocidad
    if teclas[pygame.K_DOWN]  or teclas[pygame.K_s]:
        objeto_y += velocidad

    # Opcional: evitar que el objeto salga de la pantalla
    objeto_x = max(RADIO, min(ANCHO - RADIO, objeto_x))
    objeto_y = max(RADIO, min(ALTO  - RADIO, objeto_y))

    # 3) Fondo de la pantalla (borra el fotograma anterior)
    pantalla.fill(BLANCO)

    # -------------------------------------------------------
    # 4) DIBUJA AQUÍ TU OBJETO
    # -------------------------------------------------------

    # Círculo como objeto móvil
    pygame.draw.circle(pantalla, AZUL, (objeto_x, objeto_y), RADIO)
    pygame.draw.circle(pantalla, NEGRO, (objeto_x, objeto_y), RADIO, 2)  # borde

    # Puedes sustituirlo por un rectángulo:
    # pygame.draw.rect(pantalla, ROJO, [objeto_x - 25, objeto_y - 25, 50, 50])

    # Mostrar la posición actual como texto (útil para depurar)
    fuente = pygame.font.SysFont("Arial", 18)
    info = fuente.render(f"x={objeto_x}  y={objeto_y}   (flechas o WASD para mover)", True, NEGRO)
    pantalla.blit(info, [10, 10])

    # -------------------------------------------------------
    # 5) Actualizar pantalla (no modificar)
    # -------------------------------------------------------
    pygame.display.flip()
    reloj.tick(60)

# --- Salir de Pygame ---
pygame.quit()
