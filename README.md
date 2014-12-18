uav-object-tracking
===================

This repository contain diferents projects:

- Lineal-Control
- Vision-Object-Tracking
- Follow-me


Prerequisites
=============
In the Odroid:
- Mavproxy installed, if no please see: [http://tridge.github.io/MAVProxy/](http://tridge.github.io/MAVProxy/)
- Dron Api installed, if not please see: http://dev.ardupilot.com/wiki/droneapi-tutorial/
- Mavconn installed, if not please see: https://pixhawk.ethz.ch/software/mavconn/start

How to run Lineal-Control
=========================

- ssh in the odroid: 

``ssh odroid@xx.xx.xx.xx`` 
clone repository
- clone repository:
``git clone https://github.com/jhonny-villarroel/uav-object-tracking.git``

- Start MavProxy :
``sudo mavproxy.py --master=/dev/ttyUSB0 --baudrate=57600``

- Load module Drone Api:
``module load droneapi.module.api``

- Start main python program:
``api start Object-Tracking.py``

How to run Vision-Object-Trackin
================================

How to run Follow-me
====================


