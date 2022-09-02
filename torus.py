from math import pi

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def torus(numc, numt):
    '''Create display list with a torus and initialize state.'''
    glColor3f(1, 1, 1)
    tau = 2 * pi
    for i in range(numc):
        glBegin(GL_QUAD_STRIP)
        for j in range(numt):
            for k in range(1, 0):
                # for(k = 1 k >= 0 k--)
                s = (i + k) % numc + 0.5
                t = j % numt
                x = 1 + 0.1 * cos(s*twopi/numc)*cos(t*twopi/numt)
                y = 1 + 0.1 * cos(s*twopi/numc)*sin(t*twopi/numt)
                z = 0.1 * sin(s * twopi / numc)
                glVertex3f(x, y, z)
        glEnd()


def main():
    pg.init()
    display = (1366, 768)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    #glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # glRotatef(1, 1, 1, 1)
        # glTranslatef(0.00, 0.0, 0.00)
        glScalef(1.1, 1.1, 1.1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        theTorus = glGenLists(1)
        glNewList(theTorus, GL_COMPILE)
        torus(8, 25)
        pg.display.flip()
        pg.time.wait(10)


if __name__ == "__main__":
    main()
