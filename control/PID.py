
#------------------CONTROL PID--------------------
import math
import time

 #controller direction variables
 #DIRECT  = 0
 #REVERSE = 1

class PID(object):

    #def __init__(self, c_input, c_output, c_setpoint, kp, ki, kd, controller_direction):
    def __init__(self, c_setpoint, kp, ki, kd, controller_direction):       
        #build the object
        #self.control_input = c_input
        #self.control_output = c_output
        self.control_input = None
        self.control_output = None      
        self.control_setpoint = c_setpoint
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.control_dir = controller_direction

        self.ITerm = self.control_output

        self.LastError = None

        # Possible controller_direction values are: 1(DIRECT) | 0(REVERSE)
        self.LastInput = self.control_input

        # Object Outputs
        self.OutMin = None;
        self.OutMax = None;

        # Always in AUTO MODE, Never in MANUAL MODE
        # self.InAutoMode = false

        #Sample Time in Milliseconds, in this case 100 ms = 0.1 seconds
        self.SampleTime = 100

        # # ******* Set the Output Limits of the PID *******
        # # should be called before PIDCompute()
        # # Default Values are (0 - 255) (Min, Max)
        # # ---- To change  OutPutLimits range, call the method again with the new
        # # ---- ranges after creating pid_control object
        # #SetOutputLimits(0, 255)
        self.SetOutputLimits(0, 100)

        # # ******* Set the Gain Tunnings for PID *********
        # # should be called before PIDCompute()
        # #SetTunning(kp, ki, kd)
        self.SetTunning(kp, ki, kd)

        # # ******* Set Controller Direction *********
        # # should be called before PIDCompute()
        # # SetControllerDirection(self.control_dir)
        # #SetControllerDirection(controller_direction)
        self.SetControllerDirection(controller_direction)
        
        # Get current time in milliseconds
        millis = int(round(time.time() * 1000))
        
        # Get Last Time
        self.LastTime = millis - self.SampleTime


    def SetOutputLimits(self, Range_Min, Range_Max):

        self.OutMin = Range_Min
        self.OutMax = Range_Max

        
        if (self.control_output > self.OutMax):
            self.control_output = self.OutMax
            
        if (self.control_output < self.OutMin):
            self.control_output = self.OutMin

        if (self.ITerm > self.OutMax):
            ITerm = self.OutMax

        if (self.ITerm < self.OutMin):
            self.ITerm = self.OutMin


    def SetTunning(self, SetKp, SetKi, SetKd):
        # Time per samples = 0.1 [s] | 100 [ms]
        # Take a sample every 100 ms
        TimePerSample = (float(self.SampleTime) / float(1000)) 
        #TimePerSample = 100 
        self.kp = SetKd
        self.ki = SetKi * TimePerSample
        self.kd = SetKd / TimePerSample

        # if control direction is REVERSE(value = 1)
        if(self.control_dir == 1):
            self.kp = (0 - self.kp)
            self.ki = (0 - self.ki)
            self.kd = (0 - self.kd)

    # This method can be called at any moment in the execution time #
    def SetControllerDirection(self, UserControlDirection):
        if(UserControlDirection != self.control_dir):
            self.kp = (0 - self.kp)
            self.ki = (0 - self.ki)
            self.kd = (0 - self.kd)


    def GetInputPID(self, user_input):
        self.control_input = user_input


    def ComputePID(self):
        # Get current time in milliseconds
        now = int(round(time.time() * 1000))  
        TimeChange = now - self.LastTime

        if(TimeChange >= self.SampleTime):
            compute_input = self.control_input

            compute_error = (self.control_setpoint - compute_input)

            if(self.ITerm is None):
                self.ITerm = 0
                
            self.ITerm = self.ITerm + (self.ki * compute_error)

            if(self.ITerm > self.OutMax):
                self.ITerm = self.OutMax

            if(self.ITerm < self.OutMin):
                self.ITerm = self.OutMin

            #dInput =  (self.control_input - self.LastInput)
            if(self.LastError is None):
                self.LastError = compute_error

            # Compute de Differential Error 
            dError = (compute_error - self.LastError)

            # Compute PID
            # This method takes variations in the inputs ???
            # pid_output = (self.kp * compute_error) + self.ITerm - (self.kd * dInput) 

            # This method takes variations in the Error dE = Error - lastError
            pid_output = (self.kp * compute_error) + self.ITerm - (self.kd * dError)  

            if(pid_output > self.OutMax):
                pid_output = self.OutMax

            if(pid_output < self.OutMin):
                pid_output = self.OutMin

            #Compute PID OUTPUT             
            self.control_output = pid_output

            #self.LastInput = compute_input
            self.LastError = compute_error

            self.LastTime = now 


    # ****** Call After ComputePID() ******
    def GetOutputPID(self):
        return self.control_output

    # ****** Call at any Moment ********
    def GetSetPoint(self):
        return self.control_setpoint

    # ******* Call only after ComputePID() *****
    def GetCurrentError(self):
        return self.LastError


