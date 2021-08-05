from __future__ import division
import time
import rospy
from std_msgs.msg import String
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
# Equivalente a 0°
servo_min = 150  # Min pulse length out of 4096
# Equivalente a 180°
servo_max = 600  # Max pulse length out of 4096

# Frecuencia= 60hz, utilizada para servos.
pwm.set_pwm_freq(60)

# Definimos los canales
dedo_0=0  #Channel 0
dedo_1=1  #Channel 1
dedo_2=2  #Channel 2
dedo_3=3  #Channel 3
dedo_4=4  #Channel 4

while True:
    #Empieza el código MIDI

    #definir posición
    degree = raw_input("Insert position:") 

    #Conversión de grados, como la función map en Arduino
    width_pulse=int(int(degree)*(servo_max-servo_min)/180+servo_min)
    
    delay=1

    pwm.set_pwm(dedo0,0,width_pulse)
    time.sleep(delay)

    pwm.set_pwm(dedo1,0,width_pulse)
    time.sleep(delay)
    
    pwm.set_pwm(dedo2,0,width_pulse)
    time.sleep(delay)
    
    pwm.set_pwm(dedo3,0,width_pulse)
    time.sleep(delay)
    
    pwm.set_pwm(dedo4,0,width_pulse)
    time.sleep(delay)