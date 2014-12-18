from droneapi.lib import VehicleMode
from pymavlink import mavutil

class Drone:
    #VALUE PWM FOR ROLL
    MIN_PWM_ROLL = 1169
    TRIM_PWM_ROLL = 1512
    MAX_PWM_ROLL = 1850

    #VALUE PWM FOR TRHOTTLE
    MIN_PWM_THROTLLE = 1167
    TRIM_PWM_THROTLLE = 1512
    MAX_PWM_THROTLLE = 1851
    
    
    def __init__(self, name, api):
        self.name = name
        self.api = api
        # get our vehicle - when running with mavproxy it only knows about one vehicle (for now)
        self.vehicle = self.api.get_vehicles()[0]
        
    def moveLineal(self, posX, posY):
        # if the value of PosX or PosY is 0 
        print "move lineal!"
        self.setPWMRoll(posX)
        self.setPWMThrottle(posY)

    def move(self, posX, posY):
        pass
        
    def setPWMRoll(self, pwm_x):
        if(pwm_x >= Drone.MIN_PWM_ROLL and  pwm_x <= Drone.MAX_PWM_ROLL):
            print "SetPWMROLL", pwm_x
            self.vehicle.channel_override = {"1" : pwm_x}
            self.vehicle.flush()

    def setPWMThrottle(self, pwm_y):
        if(pwm_y >= Drone.MIN_PWM_THROTLLE and  pwm_y <= Drone.MAX_PWM_THROTLLE):
            print "setPWMThrottle", pwm_y
            self.vehicle.channel_override = {"4" : pwm_y}
            self.vehicle.flush()

    def stopMoveX (self):
        print "Stop Move X"
        self.vehicle.channel_override = {"4" : Drone.TRIM_PWM_THROTLLE}
        self.vehicle.flush()

    def stopMoveY (self):
        print "Stop Move Y"
        self.vehicle.channel_override = {"1" : Drone.TRIM_PWM_ROLL}
        self.vehicle.flush()

    def giveManualControl(self):
        print "Give Manual Control"
        self.vehicle.channel_override = {"1" : 0}
        self.vehicle.channel_override = {"4" : 0}
        self.vehicle.flush()
