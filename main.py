from math import sin, cos, atan2, acos, sqrt
from lx16a import *
import time

# Initialize the LX16A controller and create LX16A objects for each servo
LX16A.initialize("/dev/ttyUSB0", 0.1)

servo1 = LX16A(1)
servo2 = LX16A(2)
servo3 = LX16A(3)
servo4 = LX16A(4)
servo5 = LX16A(5)
servo6 = LX16A(6)
servo7 = LX16A(7)
servo8 = LX16A(8)
servo9 = LX16A(9)
servo10 = LX16A(10)
servo11 = LX16A(11)
servo12 = LX16A(12)
servo13 = LX16A(13)
servo14 = LX16A(14)
servo15 = LX16A(15)
servo16 = LX16A(16)
servo17 = LX16A(17)
servo18 = LX16A(18)

# Define the lengths of the legs
tibiaLength = 50
coxaLength = 50
femurLength = 50

class Hexapod:
   def __init__(self):
       pass

   def move_front_left(self, x, y, z):
       # Calculate inverse kinematics for a single leg
       hipHeight = z - tibiaLength
       legLength = sqrt(x * x + y * y)

       coxaAngle = atan2(y, x) * 180.0 / pi

       D = (legLength * legLength - coxaLength * coxaLength - hipHeight * hipHeight - femurLength * femurLength - tibiaLength * tibiaLength) / (2.0 * coxaLength * sqrt(femurLength * femurLength + tibiaLength * tibiaLength))
       femurTibiaAngle = acos(D) * 180.0 / pi

       femurAngle = acos((hipHeight - femurLength * cos(femurTibiaAngle * pi / 180.0)) / legLength) * 180.0 / pi

       tibiaAngle = 180.0 - femurTibiaAngle

       servo1.move(coxaAngle)
       servo2.move(femurAngle)
       servo3.move(tibiaAngle)

   # Similar methods for move_front_right, move_middle_left, etc.

# Create a Hexapod object
hexapod = Hexapod()

# Move the front left leg of the hexapod
hexapod.move_front_left(10, 10, 10)

# Wait for the servos to finish moving
time.sleep(1)
