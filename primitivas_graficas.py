import math

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def pontos2d():
    '''
        Desenha os pontos de um polígono com 7 vértices
    '''
    ang = 0

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)

    glBegin(GL_POINTS)

    while ang < 2*math.pi:
        glVertex2f(20*math.cos(ang), 20*math.sin(ang))
        ang += (math.pi/7.0)
    glEnd()


def lines2d():
    '''
        Desenha as linhas de um polígono com 7 vértices
    '''
    ang = 0

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)

    glBegin(GL_LINES)

    while ang < 2*math.pi:
        glVertex2f(20*math.cos(ang), 20*math.sin(ang))
        ang += (math.pi/7.0)
    glEnd()


def lineloop2d():
    '''
        Desenha um polígono com 7 vértices
    '''
    ang = 0

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)

    glBegin(GL_LINE_LOOP)

    while ang < 2*math.pi:
        glVertex2f(20*math.cos(ang), 20*math.sin(ang))
        ang += (math.pi/7.0)
    glEnd()


def triangles2d():
    '''
        Desenha dois triângulos.
    '''
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(-35.0, -14.0)
    glVertex2f(-21.0, 14.0)
    glVertex2f(-7.0, -14.0)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(7.0, 14.0)
    glVertex2f(21.0, -14.0)
    glVertex2f(35.0, 14.0)
    glEnd()


def main():
    pg.init()
    display = (1366, 768)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    # gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    gluOrtho2D(-100, 100, -100, 100)

    glTranslatef(0.0, 0.0, 0.0)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # glRotatef(1, 1, 1, 1)
        # glTranslatef(0.00, 0.0, 0.00)
        # glScalef(0.99, 0.99, 0.99)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # pontos2d()
        # lines2d()
        # lineloop2d()
        triangles2d()
        pg.display.flip()
        pg.time.wait(10)


if __name__ == "__main__":
    main()
