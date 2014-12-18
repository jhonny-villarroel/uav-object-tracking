
from droneapi.lib import VehicleMode
from pymavlink import mavutil
#import lcmhandler
import thread
import threading
import time
import sys
import os
import lcm

sys.path.append("/home/free/ardupilot/ArduCopter")
from mavconn import mavlink_message_t
from mavconn import mavlink_msg_container_t

class Lcmhandler (threading.Thread):
    def __init__(self, drone):
        threading.Thread.__init__(self)
        self.lc = lcm.LCM()
        self.drone = drone
        #self.subscription = self.lc.subscribe("MAVLINK", self.my_handler)
        self.startThread = False
    def isStarted (self):
        return self.startThread
    def run(self):
        print "Starting..Thread"
        self.startThread = True
        self.startHandler()
    def stop(self):
        self.startThread = False

    def lcm_suscribe(self, channel, method):
        self.subscription = self.lc.subscribe(channel, method)
    
    def my_handler(self, channel, data):
        
        msg = mavlink_msg_container_t.decode(data)
        msgId =  msg.msg.msgid & 0xff

        if msgId == 140: # vison tracking
           print "Mavlink package vision"
           print("   payload 0 x  = %s" % str(msg.msg.payload64[0]))
           print("   Payload 1 y  = %s" % str(msg.msg.payload64[1]))

           posX = msg.msg.payload64[0]
           posY = msg.msg.payload64[1]
           #self.drone.move(posX, posY)
           self.drone.moveLineal(posX, posY)
        elif msgId == 150: # object avoidance
            print "Mavlink package object avoidance"
            print("   payload 0 x  = %s" % str(msg.msg.payload64[0]))
            print("   Payload 1 y  = %s" % str(msg.msg.payload64[1]))

        else: 
            print "No mavlink package reconized"

    def startHandler(self):
        print "---Start--Listener--"
        
        try:
            while self.isStarted():
                self.lc.handle()
                print "Handler"
        except KeyboardInterrupt:
            pass
    def stopHandler(self):
        #print "---Stopping handler---"
        self.startThread = False