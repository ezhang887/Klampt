from klampt import *
from klampt.math import *
import math
import sys
sys.path.append("Web/Server")
import kviz

#stub code
def lab1b(point,angle):
    pass


pos1 = (0,0)
pos2local = (0,0)
pos3local = (0,0)
angle = 0
auto = True

def boilerplate_start():
    global pos1,pos2local,pos3local,angle,auto
    pos1 = (0,0)
    pos2local = (3,0)
    pos3local = (1.6,1.4)
    angle = 0
    auto = True
    kviz._world.loadElement(__KLAMPT_DIR__+"data/terrains/plane.env")
    kviz.add_sphere("center",0,0,0.1,0.1)
    kviz.add_sphere("point1",0,0,0.1,0.05)
    kviz.add_sphere("point2",0,0,0.1,0.05)
    kviz.add_line("line1", 0,0,0.1, 0,0,0.1)
    kviz.add_line("line2", 0,0,0.1, 0,0,0.1)
    kviz.set_color("center",1,0,0)
    kviz.set_color("point1",1,1,0)
    kviz.set_color("point2",1,0.5,0)

def boilerplate_advance():
    global pos1,pos2local,pos3local,angle,auto
    pos2 = vectorops.add(pos1,stub.lab1b(pos2local,angle))
    pos3 = vectorops.add(pos1,stub.lab1b(pos3local,angle))
    kviz.update_sphere("point1",pos2[0],pos2[1],0.1)
    kviz.update_sphere("point2",pos3[0],pos3[1],0.1)
    kviz.update_line("line1", 0,0,0.1, pos2[0],pos2[1],0.1)
    kviz.update_line("line2", 0,0,0.1, pos3[0],pos3[1],0.1)
    
    if auto:
        angle += 2
        if angle >= 360:
            angle -= 360


def boilerplate_setitem(name,value):
    global auto,angle
    if name == "angle_manual":
        print "Setting angle manual control to",value
        auto = not value
    elif name == "angle":
        print "Setting angle to",value,"degrees"
        angle = float(value)
