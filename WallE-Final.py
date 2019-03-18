from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np      #np = numpy, it has "arange" function in it
from math import *      #for circle, it has Pi, Sin, Cos, ..etc

def drawAxis():
    glLineWidth(1)
    glBegin(GL_LINES)  # AXIS X & Y
    glVertex(-1, 0)
    glVertex(1, 0)
    glVertex(0, -1)
    glVertex(0, 1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(1, 0, 0)
    glVertex(.25, .25)
    glVertex(-.25, .25)
    glVertex(-.25, -.25)
    glVertex(.25, -.25)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex(.5, .5)
    glVertex(-.5, .5)
    glVertex(-.5, -.5)
    glVertex(.5, -.5)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex(.75, .75)
    glVertex(-.75, .75)
    glVertex(-.75, -.75)
    glVertex(.75, -.75)
    glEnd()

    glPointSize(4)
    glColor3f(1, 0, 1)
    glBegin(GL_POINTS)
    for x in np.arange(-1, 1, .05):
        y = x
        glVertex(x + 0.1, y + 0.1)
    for x in np.arange(-1, 1, .05):
        y = -x
        glVertex(x + 0.1, y - 0.1)
    for x in np.arange(-1, 1, 0.05):
        glVertex(x, 0)
    for y in np.arange(-1, 1, 0.05):
        glVertex(0, y)
    glEnd()
    # ALL the above are to draw GUIDELINES, for symmetry's sake



def bodypolygons():
    glColor(.98,.6275,.1666)
    glBegin(GL_POLYGON)
    glVertex(.5,.15)
    glVertex(.5,.375)
    glVertex(.425, .422)
    glVertex(-.5,.425)
    glVertex(-.425, .422)
    glVertex(-.5, .375)
    glVertex(-.5,.15)
    glEnd()

    glColor(0.068, .046, .222)
    glBegin(GL_LINES)
    glVertex(.425,.141)
    glVertex(.425, .422)
    glVertex(-.425, .141)
    glVertex(-.425, .422)

    glVertex(-.28,.232)
    glVertex(-.28,.422)
    glVertex(.28, .232)
    glVertex(.28, .422)
    glEnd()

    glColor(1,.85,0)
    glBegin(GL_POLYGON)
    glVertex(-.425,-.425)
    glVertex(.425,-.425)
    glVertex(.425,.15)
    glVertex(-.425,.15)
    glEnd()
#The leaf
    glColor(.3923,.44,.3828)
    Sdraw_circle(.08,.15,.32,0,2)
    glColor(1,0,0)
    glColor(.2337,.85,.1105)
    Sdraw_circle(.025,.13,.34,0,2)
    Sdraw_circle(0.025,.13,.3,0,2)
    Sdraw_circle(0.025,.17,.34,0,2)
    Sdraw_circle(0.025,.17,.3,0,2)
    glColor(.9323,.98,.2646)
    Sdraw_circle(0.02, .15,.32,0,2)
    glColor(0.0805, .46, .0046)
    glBegin(GL_LINES)
    glVertex(.15,.28)
    glVertex(.15,.24)
    glEnd()


#Window polygon n lines
    glColor(.021,.6972,1)
    glBegin(GL_POLYGON)
    glVertex(-.25, .4)
    glVertex(-.25, .25)
    glVertex(-0.05, .25)
    glVertex(-0.05, .4)
    glEnd()
    glLineWidth(3)
    glColor(0.068, .046, .222)
    glBegin(GL_LINE_LOOP)
    glVertex(-.25, .4)
    glVertex(-.25, .25)
    glVertex(-0.05, .25)
    glVertex(-0.05, .4)
    glEnd()


def HandsPolygons():    #This fn has POLYGONS OF FULL TWO HANDS , ONLY
    #lefthandfirst
    glColor(.6883,.8622,.97)
    glBegin(GL_POLYGON)
    glVertex(-.60, .17)  # ^^^that curve, but upper one, LEFT
    glVertex(-.55, .232)

    glVertex(-.23, .232)  # \
    glVertex(-.17, .19)

    glVertex(-.17, .19)  # |
    glVertex(-.17, .112)

    glVertex(-.53, .112)  # rect _
    glVertex(-.53, .072)

    glVertex(-.53, .072)  # rect _
    glVertex(-.17, .072)

    glVertex(-.17, .072)  # |
    glVertex(-.17, -.01)

    glVertex(-.17, -.01)  # /
    glVertex(-.22, -.048)

    glVertex(-.22, -.048)
    glVertex(-.55, -.048)  # Body line |

    glVertex(-.55, -.048)  # Small curve on the extreme left, down the LEFT hand
    glVertex(-.60, .01)

    glEnd()

    # RECTANGLES IN HANDS
    glColor(.3381,.4318,.49)
    glBegin(GL_POLYGON)  # Rectangles INSIDE the left hand
    glVertex(-.6, .17)
    glVertex(-.53, .17)

    glVertex(-.53, .17)
    glVertex(-.53, .01)

    glVertex(-.53, .01)
    glVertex(-.6, .01)

    glVertex(-.6, .01)
    glVertex(-.6, .17)
    glEnd()

    glColor(0.068, .046, .222)
    glBegin(GL_LINES)  # Rectangles INSIDE the left hand, LINES
    glVertex(-.6, .17)
    glVertex(-.53, .17)

    glVertex(-.53, .17)
    glVertex(-.53, .01)

    glVertex(-.53, .01)
    glVertex(-.6, .01)

    glVertex(-.6, .01)
    glVertex(-.6, .17)
    glEnd()



    # Right Hand


    glColor(.6883,.8622,.97)
    glBegin(GL_POLYGON)
    glVertex(.60, .17)  # ^^^that curve, but upper one, LEFT
    glVertex(.55, .232)

    glVertex(.23, .232)  # \
    glVertex(.17, .19)

    glVertex(.17, .19)  # |
    glVertex(.17, .112)

    glVertex(.53, .112)  # rect _
    glVertex(.53, .072)

    glVertex(.53, .072)  # rect _
    glVertex(.17, .072)

    glVertex(.17, .072)  # |
    glVertex(.17, -.01)

    glVertex(.17, -.01)  # /
    glVertex(.22, -.048)

    glVertex(.22, -.048)
    glVertex(.55, -.048)  # Body line |

    glVertex(.55, -.048)  # Small curve on the extreme left, down the LEFT hand
    glVertex(.60, .01)

    glEnd()

    glColor(.3381,.4318,.49)
    glBegin(GL_POLYGON)  # Rectangles INSIDE the right hand
    glVertex(.6, .17)
    glVertex(.53, .17)

    glVertex(.53, .17)
    glVertex(.53, .01)

    glVertex(.53, .01)
    glVertex(.6, .01)

    glVertex(.6, .01)
    glVertex(.6, .17)
    glEnd()

    glColor(0.068, .046, .222)
    glBegin(GL_LINES)  # Rectangles INSIDE the right hand, LINES
    glVertex(.6, .17)
    glVertex(.53, .17)

    glVertex(.53, .17)
    glVertex(.53, .01)

    glVertex(.53, .01)
    glVertex(.6, .01)

    glVertex(.6, .01)
    glVertex(.6, .17)
    glEnd()


def HandsLines():       #Hands LINE LOOPS ONLY
    # lefthandfirst
    glColor(0.068, .046, .222)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    glVertex(-.60, .17)  # ^^^that curve, but upper one, LEFT
    glVertex(-.55, .232)

    glVertex(-.23, .232)  # \
    glVertex(-.17, .19)

    glVertex(-.17, .19)  # |
    glVertex(-.17, .112)

    glVertex(-.53, .112)  # rect _
    glVertex(-.53, .072)

    glVertex(-.53, .072)  # rect _
    glVertex(-.17, .072)

    glVertex(-.17, .072)  # |
    glVertex(-.17, -.01)

    glVertex(-.17, -.01)  # /
    glVertex(-.22, -.048)

    glVertex(-.22, -.048)
    glVertex(-.55, -.048)  # Body line |

    glVertex(-.55, -.048)  # Small curve on the extreme left, down the LEFT hand
    glVertex(-.60, .01)

    glEnd()

    glColor(0.068, .046, .222)
    glLineWidth(5)
    glBegin(GL_LINES)       # the 2 lines in the tip of the claw
    glVertex(-.3, .232)  # Parallel lines in the left claw
    glVertex(-.3, .112)

    glVertex(-.3, .072)
    glVertex(-.3, -.048)

    glVertex(-.25, .112)  # Small line | in the claw's tip
    glVertex(-.25, .072)
    glEnd()



    # Right Hand :

    glColor(0.068, .046, .222)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    glVertex(.60, .17)  # ^^^that curve, but upper one, LEFT
    glVertex(.55, .232)

    glVertex(.23, .232)  # \
    glVertex(.17, .19)

    glVertex(.17, .19)  # |
    glVertex(.17, .112)

    glVertex(.53, .112)  # rect _
    glVertex(.53, .072)

    glVertex(.53, .072)  # rect _
    glVertex(.17, .072)

    glVertex(.17, .072)  # |
    glVertex(.17, -.01)

    glVertex(.17, -.01)  # /
    glVertex(.22, -.048)

    glVertex(.22, -.048)
    glVertex(.55, -.048)  # Body line |

    glVertex(.55, -.048)  # Small curve on the extreme left, down the LEFT hand
    glVertex(.60, .01)

    glEnd()


    glColor(0.068, .046, .222)
    glLineWidth(5)
    glBegin(GL_LINES)  # the 2 lines in the tip of the claw
    glVertex(.3, .232)  # Parallel lines in the right claw
    glVertex(.3, .112)

    glVertex(.3, .072)
    glVertex(.3, -.048)

    glVertex(.25, .112)  # Small line | in the claw's tip
    glVertex(.25, .072)
    glEnd()

    glColor(0.068, .046, .222)
    glBegin(GL_LINES)
    glVertex(0.17, .150)
    glVertex(-0.17, .150)
    glEnd()



def bodynhands():
    glColor(0.068, .046, .222)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)  # Body
    glVertex(-.425, -.425)  # Starting from the LEFT LOWER POINT, then to RIGHT LOWER POINT,
    glVertex(.425, -.425)  # Then moving up the right hand, right upper body, left uppder body, left hand,etc
    ##
    glVertex(.425, -.425)
    glVertex(.425, -.048)

    glVertex(.425, -.048)  # Right hand starts here
    glVertex(.5, -.048)

    glVertex(.5, -.048)
    glVertex(.22, -.048)

    glVertex(.22, -.048)
    glVertex(.17, -.01)

    glVertex(.17, -.01)
    glVertex(.17, .072)

    glVertex(.17, .072)
    glVertex(.53, .072)

    glVertex(.53, .072)
    glVertex(.53, .112)

    glVertex(.53, .112)
    glVertex(.17, .112)

    glVertex(.17, .112)
    glVertex(.17, .190)

    glVertex(.17, .190)
    glVertex(.22, .232)

    glVertex(.22, .232)
    glVertex(.5, .232)

    glVertex(.5, .375)
    glVertex(.425, .422)

    glVertex(-.425, .422)
    glVertex(-.5,.375)
    #glVertex(.5, .425)  # Left Upper Side

    glVertex(-.5, .232)
    ##

    glVertex(-.425, -.048)  # Body line |
    glVertex(-.425, -.425)
    glEnd()



def Wheels():
    # Starting from the bottom, WHEELS first
    glColor(0.068, .046, .20)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)  # Left Wheel
    glVertex(-.75, -.75)
    glVertex(-.5, -.75)
    glVertex(-.5, -.3)
    glVertex(-.75, -.3)
    glEnd()
    glColor3f(.2324,.2618,.28)
    glBegin(GL_POLYGON)  # Left Wheel
    glVertex(-.75, -.75)
    glVertex(-.5, -.75)
    glVertex(-.5, -.3)
    glVertex(-.75, -.3)
    glEnd()
    ##
    glColor(0.068, .046, .222)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)  # Left Wheel
    glVertex(.75, -.75)
    glVertex(.5, -.75)
    glVertex(.5, -.3)
    glVertex(.75, -.3)
    glEnd()
    glColor3f(.2324,.2618,.28)
    glBegin(GL_POLYGON)  # Right Wheel
    glVertex(.75, -.75)
    glVertex(.5, -.75)
    glVertex(.5, -.3)
    glVertex(.75, -.3)
    glEnd()

    ####################

    # POLYGONS between wheels n body
    glColor(.4899,.6256,.71)
    glBegin(GL_POLYGON)  # Left wheel
    glVertex(-.425, -.425)
    glVertex(-.425, -.35)
    glVertex(-.5, -.35)
    glVertex(-.5, -.435)
    glVertex(-.425, -.5)
    glVertex(-.425, -.55)
    glVertex(-.425, -.63)
    glVertex(-.38, -.63)
    glVertex(-.32, -.6)
    glVertex(-.32, -.5)
    glVertex(-.32, -.425)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(-.425, -.55)
    glVertex(-.425, -.6)
    glVertex(-.5, -.6)
    glVertex(-.5, -.55)
    glEnd()

    glColor(0.068, .046, .222)
    glBegin(GL_LINES)
    glVertex(-.32, -.5)
    glVertex(-.425, -.5)
    glEnd()
    ###
    # POLYGONS between wheels n body
    glColor(.4899,.6256,.71)
    glBegin(GL_POLYGON)  # Right wheel
    glVertex(.425, -.425)
    glVertex(.425, -.35)
    glVertex(.5, -.35)
    glVertex(.5, -.435)
    glVertex(.425, -.5)
    glVertex(.425, -.55)
    glVertex(.425, -.63)
    glVertex(.38, -.63)
    glVertex(.32, -.6)
    glVertex(.32, -.5)
    glVertex(.32, -.425)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(.425, -.55)
    glVertex(.425, -.6)
    glVertex(.5, -.6)
    glVertex(.5, -.55)
    glEnd()

    glColor(0.068, .046, .222)
    glBegin(GL_LINES)
    glVertex(-.32, -.5)
    glVertex(-.425, -.5)
    glEnd()

    ##

    # LINES between wheels n body
    glColor(0.068, .046, .222)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex(-.425, -.35)
    glVertex(-.5, -.35)
    glVertex(.425, -.35)
    glVertex(.5, -.35)

    glVertex(-.32, -.425)
    glVertex(-.32, -.5)
    glVertex(.32, -.425)
    glVertex(.32, -.5)

    glVertex(-.32, -.5)
    glVertex(-.32, -.6)
    glVertex(.32, -.5)
    glVertex(.32, -.6)

    glVertex(-.32, -.5)
    glVertex(-.425, -.5)
    glVertex(.32, -.5)
    glVertex(.425, -.5)

    glVertex(-.425, -.5)
    glVertex(-.5, -.435)
    glVertex(.425, -.5)
    glVertex(.5, -.435)

    glVertex(-.32, -.6)
    glVertex(-.38, -.63)
    glVertex(.32, -.6)
    glVertex(.38, -.63)

    glVertex(-.38, -.63)
    glVertex(-.425, -.63)
    glVertex(.38, -.63)
    glVertex(.425, -.63)

    glVertex(-.425, -.63)
    glVertex(-.425, -.5)
    glVertex(.425, -.63)
    glVertex(.425, -.5)

    glVertex(-.425, -.55)
    glVertex(-.5, -.55)
    glVertex(.425, -.55)
    glVertex(.5, -.55)

    glVertex(-.425, -.60)
    glVertex(-.5, -.60)
    glVertex(.425, -.6)
    glVertex(.5, -.6)

    glVertex(-.5,-.55)
    glVertex(-.5,-.6)
    glVertex(.5, -.55)
    glVertex(.5, -.6)

    glVertex(-.5, -.35)
    glVertex(-.5, -.435)
    glVertex(.5, -.35)
    glVertex(.5, -.435)

    glVertex(-.425, -.425)
    glVertex(-.425, -.35)
    glVertex(.425, -.425)
    glVertex(.425, -.35)

    glVertex(-.425, -.425)
    glVertex(-.32, -.425)
    glVertex(.425, -.425)
    glVertex(.32, -.425)

    glEnd()

    ###
    # INSIDE-Left-Wheel
    #glColor(0,1,0)
    glBegin(GL_POLYGON)
    glVertex(-.75, -.345)
    glVertex(-.75, -.3675)
    glVertex(-.5, -.3675)
    glVertex(-.5, -.345)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(-.75, -.4125)
    glVertex(-.75, -.435)
    glVertex(-.5, -.435)
    glVertex(-.5, -.4125)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(-.75, -.48)
    glVertex(-.75, -.5025)
    glVertex(-.5, -.50250)
    glVertex(-.5, -.48)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(-.75, -.5475)
    glVertex(-.75, -.57)
    glVertex(-.5, -.57)
    glVertex(-.5, -.5475)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(-.75, -.615)
    glVertex(-.75, -.6375)
    glVertex(-.5, -.6375)
    glVertex(-.5, -.615)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(-.75, -.6825)
    glVertex(-.75, -.705)
    glVertex(-.5, -.705)
    glVertex(-.5, -.6825)
    glEnd()

    ###
    # INSIDE-RIGHT-Wheel
    # glColor(0,1,0)
    glBegin(GL_POLYGON)
    glVertex(.75, -.345)
    glVertex(.75, -.3675)
    glVertex(.5, -.3675)
    glVertex(.5, -.345)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(.75, -.4125)
    glVertex(.75, -.435)
    glVertex(.5, -.435)
    glVertex(.5, -.4125)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(.75, -.48)
    glVertex(.75, -.5025)
    glVertex(.5, -.50250)
    glVertex(.5, -.48)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(.75, -.5475)
    glVertex(.75, -.57)
    glVertex(.5, -.57)
    glVertex(.5, -.5475)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(.75, -.615)
    glVertex(.75, -.6375)
    glVertex(.5, -.6375)
    glVertex(.5, -.615)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(.75, -.6825)
    glVertex(.75, -.705)
    glVertex(.5, -.705)
    glVertex(.5, -.6825)
    glEnd()

    glColor(0.068, .046, .222)
    glPointSize(3)
    Sdraw_circle(.01,-.365,-.59,0,2)
    Sdraw_circle(.01,.365,-.59,0,2)



def Neck():
    glColor(1,.85,0)
    glBegin(GL_POLYGON) #Big neck polygon
    glVertex(.1,.425)
    glVertex(.1,.6)
    glVertex(-.1,.6)
    glVertex(-.1,.425)
    glEnd()

    glBegin(GL_POLYGON) #Medium neck
    glVertex(.07,.6)
    glVertex(.07,.7)
    glVertex(-.07,.7)
    glVertex(-.07, .6)
    glEnd()

    glColor(0.068, .046, .222)
    glLineWidth(3)
    glBegin(GL_LINES)   #Big neck INSIDE 2 lines
    glVertex(.1,.46875)
    glVertex(-.1, .46875)
    glVertex(.1, .55625)
    glVertex(-.1, .55625)

    glVertex(.07,.6)        #Medium neck outer lines
    glVertex(.07, .7)
    glVertex(.07,.7)
    glVertex(-.07,.7)
    glVertex(-.07,.7)
    glVertex(-.07,.6)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINE_LOOP)   #Big neck outer lines
    glVertex(.1,.425)
    glVertex(.1,.6)
    glVertex(-.1,.6)
    glVertex(-.1,.425)
    glEnd()

    glLineWidth(5)
    glColor(0,0,0)
    glBegin(GL_LINES)
    glVertex(.07, .7)
    glVertex(.15, .8)
    glVertex(.15, .8)
    glVertex(-.15, .8)
    glVertex(.07, .88)
    glVertex(-.07, .88)
    glVertex(-.15, .8)
    glVertex(-.07, .7)
    glEnd()

    glColor(.98,.6275,.1666)
    glBegin(GL_POLYGON)
    glVertex(.07, .7)
    glVertex(.15, .8)
    glVertex(.07, .88)
    glVertex(-.07, .88)
    glVertex(-.15, .8)
    glVertex(-.07, .7)
    glEnd()

def NeckMiss():
    glColor(0, .2042, .49)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex(.15,.8)
    glVertex(-.15,.8)
    glVertex(.07,.7)
    glVertex(-.07,.7)
    glEnd()


def Sdraw_circle(r=0.5, xc=0, yc=0, l=0, h=2):
    glBegin(GL_POLYGON)
    for theta in np.arange(l*3.14, h*3.14, 0.001):
        x = xc + r*cos(theta)
        y = yc + r*sin(theta)
        glVertex(x,y)
    glEnd()

def Pdraw_circle(r=0.5, xc=0, yc=0, l=0, h=2):
    glPointSize(2.5)
    glBegin(GL_POINTS)
    for theta in np.arange(l*3.14, h*3.14, 0.001):
        x = xc + r*cos(theta)
        y = yc + r*sin(theta)
        glVertex(x,y)
    glEnd()


def Eyes():
    glColor(.6883,.8622,.97)    #Biggest circles of the eye
    Sdraw_circle(.1,-.22,.81,0,2)
    Sdraw_circle(.1,.22,.81,0,2)
    Sdraw_circle(.055,-.12,.9,0,2)        #Smallest
    Sdraw_circle(.055,.12,.9,0,2)


    glColor(0,.2042,.49)
    Pdraw_circle(.055,-.12,.9,0,2)        #Left eye
    Sdraw_circle(0.09,-.18,.85,0,2)
    Pdraw_circle(.1,-.22,.81,0,2)

    Pdraw_circle(.055,.12,.9,0,2)         #Right eye
    Sdraw_circle(0.09,.18,.85,0,2)

    Pdraw_circle(.1,.22,.81,0,2)
#The 3 dots in the corners

    Sdraw_circle(.01,.105,.92,0,2)
    Sdraw_circle(.01,-.105,.92,0,2)

    Sdraw_circle(.01, -.285, .82, 0, 2)
    Sdraw_circle(.01, -.21, .74, 0, 2)

    Sdraw_circle(.01, .285, .82, 0, 2)
    Sdraw_circle(.01, .21, .74, 0, 2)
#Inner eyes
    glColor(0,.4469,.820)
    Sdraw_circle(.045,-.18,.85,0,2)
    Sdraw_circle(.045,.18,.85,0,2)
    glColor(0,.2042,.49)
    Pdraw_circle(0.02,-.18,.85,0,2)
    Pdraw_circle(0.02,.18,.85,0,2)
    glColor(.8342,.9066,.97)
    Sdraw_circle(0.033,-0.15,.87,0,2)
    Sdraw_circle(0.033,0.15,.87,0,2)
    glColor(.8342, .9066, .97)
    Sdraw_circle(.023,-.24,.78,0,2)
    Sdraw_circle(.023,.24,.78,0,2)

def Typing():
    glColor(0, .2042, .49)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex(-.25,-.24)
    glVertex(-.25,-.35)
    glVertex(-.25,-.35)
    glVertex(-.1,-.35)
    glVertex(-.1,-.35)
    glVertex(-.1,-.24)
    glVertex(-.175,-.24)
    glVertex(-.175,-.35)    #End of "W"

    glVertex(-.05,-.36)
    glVertex(-.05,-.25)
    glVertex(-.05,-.25)
    glVertex(.05,-.25)
    glVertex(.05,-.25)
    glVertex(.05,-.36)
    glVertex(-.05,-.3)
    glVertex(.05,-.3)   #End of "A"

    glVertex(.1,-.24)   #L
    glVertex(.1,-.35)
    glVertex(.1,-.35)
    glVertex(.175,-.35)


    glVertex(.21,-.24)  #L
    glVertex(.21,-.35)
    glVertex(.21,-.35)
    glVertex(.28,-.35)

    glVertex(.33, -.35)
    glVertex(.33, -.25)
    glVertex(.33,-.25)
    glVertex(.42, -.25)
    glVertex(.33,-.35)
    glVertex(.42,-.35)
    glVertex(.33, -.3)
    glVertex(.42, -.3)

    glEnd()
    glColor(.9,.2,.2)
    Sdraw_circle(.02,.29,-.3,0,2)

    glColor(0.068, .046, .222)
    glBegin(GL_LINES)
    glVertex(-.95,-.75)
    glVertex(.95,-.75)
    glEnd()
    Sdraw_circle(.02,.98,-.75)
    Sdraw_circle(.02, -.98, -.75)


def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0) #RGB

    #drawAxis()

    bodynhands()

    bodypolygons()

    HandsPolygons()
    HandsLines()

    Wheels()

    Neck()
    NeckMiss()

    Eyes()

    Typing()


    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)  #Set the window's Initial width & height
glutCreateWindow(b"Wall-E")
#glEnable(GL_DEPTH_TEST)
#glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glutDisplayFunc(draw)



glutMainLoop()