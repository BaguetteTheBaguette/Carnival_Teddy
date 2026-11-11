#import gpiozero
#from gpiozero import AngularServo
#from time import sleep # imports servo time system
#from gpiozero import Button 

#https://gpiozero.readthedocs.io/en/stable/
#https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo

pin_servo_left_arm = #integer
pin_servo_right_arm = #integer
max_cheer_height = 90 # how high arms should rotate for the peak of the cheer
min_cheer_height = 0 # how low arms should start and rotate for the peak of the cheer
left_arm = AngularServo(pin_servo_left_arm, min_angle=-90, max_angle=90) # may need to find min and max values seperatly for each servo 
num_cheers = 3 

def cheer():
    print("cheer") # this will later be motion control for servos right now it just checks files are talking to each other
    
    for i = range(1,num_cheers):
        left_arm.angle = min_cheer_height
        left_arm.angle = max_cheer_height
    left_arm.angle = min_cheer_height