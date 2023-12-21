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

   def move_front_right(self, x, y, z):
       # Calculate inverse kinematics for a single leg
       hipHeight = z - tibiaLength
       legLength = sqrt(x * x + y * y)

       coxaAngle = atan2(y, x) * 180.0 / pi

       D = (legLength * legLength - coxaLength * coxaLength - hipHeight * hipHeight - femurLength * femurLength - tibiaLength * tibiaLength) / (2.0 * coxaLength * sqrt(femurLength * femurLength + tibiaLength * tibiaLength))
       femurTibiaAngle = acos(D) * 180.0 / pi

       femurAngle = acos((hipHeight - femurLength * cos(femurTibiaAngle * pi / 180.0)) / legLength) * 180.0 / pi

       tibiaAngle = 180.0 - femurTibiaAngle

       servo4.move(coxaAngle)
       servo5.move(femurAngle)
       servo6.move(tibiaAngle)

   def move_middle_left(self, x, y, z):
       # Calculate inverse kinematics for a single leg
       hipHeight = z - tibiaLength
       legLength = sqrt(x * x + y * y)

       coxaAngle = atan2(y, x) * 180.0 / pi

       D = (legLength * legLength - coxaLength * coxaLength - hipHeight * hipHeight - femurLength * femurLength - tibiaLength * tibiaLength) / (2.0 * coxaLength * sqrt(femurLength * femurLength + tibiaLength * tibiaLength))
       femurTibiaAngle = acos(D) * 180.0 / pi

       femurAngle = acos((hipHeight - femurLength * cos(femurTibiaAngle * pi / 180.0)) / legLength) * 180.0 / pi

       tibiaAngle = 180.0 - femurTibiaAngle

       servo7.move(coxaAngle)
       servo8.move(femurAngle)
       servo9.move(tibiaAngle)

   def move_middle_right(self, x, y, z):
       # Calculate inverse kinematics for a single leg
       hipHeight = z - tibiaLength
       legLength = sqrt(x * x + y * y)

       coxaAngle = atan2(y, x) * 180.0 / pi

       D = (legLength * legLength - coxaLength * coxaLength - hipHeight * hipHeight - femurLength * femurLength - tibiaLength * tibiaLength) / (2.0 * coxaLength * sqrt(femurLength * femurLength + tibiaLength * tibiaLength))
       femurTibiaAngle = acos(D) * 180.0 / pi

       femurAngle = acos((hipHeight - femurLength * cos(femurTibiaAngle * pi / 180.0)) / legLength) * 180.0 / pi

       tibiaAngle = 180.0 - femurTibiaAngle

       servo10.move(coxaAngle)
       servo11.move(femurAngle)
       servo12.move(tibiaAngle)

   def move_back_left(self, x, y, z):
       # Calculate inverse kinematics for a single leg
       hipHeight = z - tibiaLength
       legLength = sqrt(x * x + y * y)

       coxaAngle = atan2(y, x) * 180.0 / pi

       D = (legLength * legLength - coxaLength * coxaLength - hipHeight * hipHeight - femurLength * femurLength - tibiaLength * tibiaLength) / (2.0 * coxaLength * sqrt(femurLength * femurLength + tibiaLength * tibiaLength))
       femurTibiaAngle = acos(D) * 180.0 / pi

       femurAngle = acos((hipHeight - femurLength * cos(femurTibiaAngle * pi / 180.0)) / legLength) * 180.0 / pi

       tibiaAngle = 180.0 - femurTibiaAngle

       servo13.move(coxaAngle)
       servo14.move(femurAngle)
       servo15.move(tibiaAngle)

   def move_back_right(self, x, y, z):
       # Calculate inverse kinematics for a single leg
       hipHeight = z - tibiaLength
       legLength = sqrt(x * x + y * y)

       coxaAngle = atan2(y, x) * 180.0 / pi

       D = (legLength * legLength - coxaLength * coxaLength - hipHeight * hipHeight - femurLength * femurLength - tibiaLength * tibiaLength) / (2.0 * coxaLength * sqrt(femurLength * femurLength + tibiaLength * tibiaLength))
       femurTibiaAngle = acos(D) * 180.0 / pi

       femurAngle = acos((hipHeight - femurLength * cos(femurTibiaAngle * pi / 180.0)) / legLength) * 180.0 / pi

       tibiaAngle = 180.0 - femurTibiaAngle

       servo16.move(coxaAngle)
       servo17.move(femurAngle)
       servo18.move(tibiaAngle)
    
   def moveAllLegsToPosition(self,x, y, z):
        # Calculate leg positions for lateral (x and y) and vertical (z) movements
        # You can adjust these calculations based on your hexapod's geometry

        # Calculate the desired position of the front left leg
        frontLeftX = x - 30.0; 
        frontLeftY = y + 30.0; 

        # Calculate the desired position of the front right leg
        frontRightX = x + 30.0; 
        frontRightY = y + 30.0; 

        # Calculate the desired position of the middle left leg
        middleLeftX = x - 60.0; 

        # Calculate the desired position of the middle right leg
        middleRightX = x + 60.0; 

        # Calculate the desired position of the rear left leg
        rearLeftX = x - 30.0; 
        rearLeftY = y - 30.0; 

        # Calculate the desired position of the rear right leg
        rearRightX = x + 30.0; 
        rearRightY = y - 30.0; 

        # Move individual legs to their respective positions
        self.move_front_left(frontLeftX, frontLeftY, z)
        self.move_front_right(frontRightX, frontRightY, z)
        self.move_middle_left(middleLeftX, y, z)
        self.move_middle_right(middleRightX, y, z)
        self.move_back_left(rearLeftX, rearLeftY, z)
        self.move_back_right(rearRightX, rearRightY, z)

   def moveForward(self, distance):
       # Move the hexapod forward by a specified distance (positive value)
       self.moveAllLegsToPosition(0, distance, 0)

   def moveBackward(self, distance):
       # Move the hexapod backward by a specified distance (negative value)
       self.moveAllLegsToPosition(0, -distance, 0)

   def moveRight(self, distance):
       # Move the hexapod to the right by a specified distance (positive value)
       self.moveAllLegsToPosition(distance, 0, 0)

   def moveLeft(self, distance):
       # Move the hexapod to the left by a specified distance (negative value)
       self.moveAllLegsToPosition(-distance, 0, 0)

   def moveUp(self, distance):
       # Move the hexapod upward by a specified distance (positive value)
       self.moveAllLegsToPosition(0, 0, distance)

   def moveDown(self, distance):
       # Move the hexapod downward by a specified distance (negative value)
       self.moveAllLegsToPosition(0, 0, -distance)

   def Loop(self):
       self.moveForward(100)

# Create a Hexapod object
hexapod = Hexapod()

# Move the front left leg of the hexapod
hexapod.move_front_left(10, 10, 10)

# Wait for the servos to finish moving
time.sleep(1)
