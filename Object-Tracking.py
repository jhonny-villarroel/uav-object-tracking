from droneapi.lib import VehicleMode
from pymavlink import mavutil
#import lcmhandler
import thread
import threading
import time
import sys
import os
import lcm


#-----------------------MAIN------------------------
def mavrx_debug_handler(message):
    """A demo of receiving raw mavlink messages"""
    print "Received", message


# First get an instance of the API endpoint
api = local_connect()
drone= api.get_vehicles()[0]
print "THe Mode is---->%s" % drone.mode 

akila = Drone("Akila", api)
lcm = Lcmhandler(akila)
#print dir (drone.mode)

#print "Compare--->" str(drone.mode is "VehicleMode:LOITER"
#try:
 #   thread.start_new_thread(mavrx_debug_handler, ("Thread-1", 2,)) 
#except:
 #   print "Error: unable to start thread"
isLoider=(str(drone.mode) == 'VehicleMode:LOITER')



print "status-->",(isLoider and (not lcm.isStarted()))
while True:
    
    time.sleep(2)
    
    isLoider=(str(drone.mode) == 'VehicleMode:LOITER')
    
    if isLoider:
        print "Starting LCM"
        lcm.start()

        while isLoider:
            time.sleep(1)
            if not (str(drone.mode) == 'VehicleMode:LOITER'):
                lcm.stopHandler()
                lcm.stop()
                lcm = Lcmhandler(akila)
                break
    else:
        print "waiting mode LOITER"
