import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
# from OpenGL.GLUT import *


def set_display():
    '''Prepara a Tela para receber a renderização'''

    glColor3f(0, 0, 1)
    glPointSize(10.0)
    glLineWidth(2.0)
    # gluOrtho2D(0, 500, 0, 500)


def simple_house():
    '''Desenha a casa.'''
    glClear(GL_COLOR_BUFFER_BIT)

    # Telhado
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(100.0, 200.0)
    glVertex2f(300.0, 200.0)
    glVertex2f(200.0, 300.0)
    glEnd()

    # Estrutura
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(100, 50)
    glVertex2f(100, 200)
    glVertex2f(300, 200)
    glVertex2f(300, 50)
    glEnd()

    # Porta
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(180.0, 50.0)
    glVertex2f(220.0, 50.0)
    glVertex2f(220.0, 150.0)
    glVertex2f(180.0, 150.0)
    glEnd()

    # Janela
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(240.0, 110.0)
    glVertex2f(280.0, 110.0)
    glVertex2f(280.0, 150.0)
    glVertex2f(240.0, 150.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(240, 130)
    glVertex2f(280, 130)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(260, 110)
    glVertex2f(260, 150)
    glEnd()


def main():
    '''Gerencia a janela, transformações e a renderização da casa'''
    # glutInit()
    # glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # glutInitWindowSize(1366, 768)
    # glutInitWindowPosition(100, 100)
    # glutCreateWindow("Hello World")

    # set_display()
    # glutDisplayFunc(simple_house)
    # glutMainLoop()
    pg.init()
    display = (500, 500)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    # gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    gluOrtho2D(0, 500, 0, 500)
    # glTranslatef(4, 4, 0.0)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        # set_display()
        simple_house()
        pg.display.flip()
        pg.time.wait(10)


if __name__ == '__main__':
    main()
