
from Drone_Control import Drone_Control

class Lineal_Control(Drone_Control):

    def compute(self):
        print("Child class method")

def handler_Messages(self, channel, data):
        print "recieve message"
        msg = mavlink_msg_container_t.decode(data)
        msgId =  msg.msg.msgid & 0xff