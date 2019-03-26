from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawAxis():
    glLoadIdentity()
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex(0,0,0)
    glVertex(10,0,0)

    glColor(0,1,0)
    glVertex(0,0,0)
    glVertex(0,10,0)

    glColor(0,0,1)
    glVertex(0,0,0)
    glVertex(0,0,10)
    glEnd()


def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1, .1, 30)
    gluLookAt(8,9,10,   #because we're looking at 3D Objects
              0,0,0,
              0,1,0)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

angle = 0
x = 0
forward = True
z = 1

def Car():
    global angle
    global x
    global forward

    # The 2 cubes of the car chassis
    glLoadIdentity()  # Bigger one
    glColor3f(0.88, .088, .088)  # glColor3f(.172,0.2238,0.67)    Blue deg.
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)
    glColor3f(0, 0, 0)
    glutWireCube(5.005)
    # drawAxis()

    glLoadIdentity()  # 3shan el scale تراكمي.. lazm a3ml LoadeIdentity tani 3shan t refresh yo3tbr
    glColor3f(0, 0, 0)  # glColor3f(0.88,.088,.088)
    glTranslate(0, 1.2, 0)  # Smallone
    glTranslate(x, 0, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)
    # glutWireCube(5.005)

    glLoadIdentity()
    glColor(1, 1, 1)
    glTranslate(1.3, 1.1, 0)
    glTranslate(x,0,0)
    glBegin(GL_POLYGON)  # Front windshield
    glVertex(0, -.2, -.7)
    glVertex(0, .7, -.7)
    glVertex(0, .7, 1)
    glVertex(0, -.2, 1)
    glEnd()

    # Tires
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(2.5, -2.5 * .25, 2.5 * .5)
    glTranslate(x, 0, 0)
    glRotate(angle, 0, 0, -1)
    glutWireTorus(0.22, .5, 12, 8)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(2.5, -2.5 * .25, -2.5 * .5)
    glTranslate(x, 0, 0)
    glRotate(angle, 0, 0, -1)
    glutWireTorus(0.22, .5, 12, 8)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-2.5, -2.5 * .25, 2.5 * .5)
    glTranslate(x, 0, 0)
    glRotate(angle, 0, 0, -1)
    glutWireTorus(0.22, .5, 12, 8)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-2.5, -2.5 * .25, -2.5 * .5)
    glTranslate(x, 0, 0)
    glRotate(angle, 0, 0, -1)
    glutWireTorus(0.22, .5, 12, 8)

    # Headlights
    glLoadIdentity()
    glColor(1, .9167, 0)
    # glScale(.5,.5 ,.5 )
    glTranslate(2.5, -.05, .6)  # glTranslate(5, -0.5, .75) this goes with scale^
    glTranslate(x, 0, 0)  # For movement
    glutWireSphere(.25, 10, 10)

    glLoadIdentity()
    glColor(1, .9167, 0)
    # glScale(.5,.5,.5)
    glTranslate(2.5, -0.05, -.8)
    glTranslate(x, 0, 0)  # For movement
    glutWireSphere(.25, 10, 10)

    if forward:
        angle += .15
        x += .003
        if x > 5:
            forward = False

    else:
        x -= .003
        angle -= .15
        if x < -10:
            forward = True


def Tarmac():
    glLoadIdentity()        #Tarmac
    glColor(0.29, 0.2755, 0.2755)
    glBegin(GL_POLYGON)
    glVertex(10,0,-10)
    glVertex(10,0,5)
    glVertex(-30,0,5)
    glVertex(-30,4,0)
    glEnd()
                            #Lanes
    glLoadIdentity()
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(0,0,-.7)
    glVertex(0,0,0)
    glVertex(-6,0,0)
    glVertex(-6,0,-.7)
    glEnd()

    glTranslate(7.7,0,0)
    glBegin(GL_POLYGON)
    glVertex(0, 0, -1.5)
    glVertex(0, 0, -.8)
    glVertex(-5, 0, -.8)
    glVertex(-5, 0, -1.5)
    glEnd()

    glTranslate(-18,0,0)
    glBegin(GL_POLYGON)
    glVertex(0, 0, -1.5)
    glVertex(0, 0, -.8)
    glVertex(-8, 0, -.8)
    glVertex(-8, 0, -1.5)
    glEnd()


    #sidewalk
    for x in range (-30, 10, 2):
        for z in -7, 6:
            if(x%4==0):
                glLoadIdentity()
                glColor3f(0, 0, 0)
                glTranslate(x, 1, z)
                glScale(2, 0.5, 1)
                glutSolidCube(1)

            else:
                glLoadIdentity()
                glColor3f(1, 1, 1)
                glTranslate(x, 1, z)
                glScale(2, 0.5, 1)
                glutSolidCube(1)

                #Sidewalks
        #glVertex(10, 0, -7)
        #glVertex(10, 0, 3)
        #glVertex(-20, 0, 6)
        #glVertex(-30, 6, -4)



def Background():
    glLoadIdentity()
    glColor(.1483, .83, .01)
    glBegin(GL_POLYGON)
    glVertex(-20, 10, 0)
    glVertex(-20, -10, -20)
    glVertex(20, -10, 20)
    glVertex(20, 10, 0)

    glEnd()

def display():
    global angle
    global x
    global forward
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    Background()

    Tarmac()

    Car()

    #glLoadIdentity()    #Sky, vertices aren't right yet
    #glColor(0.1, .7691, .83)
    #glBegin(GL_POLYGON)
    #glVertex(5, 0,-18)
    #glVertex(-30, 10, -18)
    #glVertex(-30, 0, -18)
    #glVertex(5, 30, -18)

    #glEnd()


    #drawAxis()

    glutSwapBuffers()       #instead of glFlush()



glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)  # Set the window's Initial width & height
glutCreateWindow(b"Moving car")
glutDisplayFunc(display)
glutIdleFunc(display)
myinit()
glutMainLoop()
