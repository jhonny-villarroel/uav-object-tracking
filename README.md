uav-object-tracking
===================

This repository contain diferents projects:

- Lineal-Control
- Vision-Object-Tracking
- Follow-me

Prerequisites
=============
- Mavproxy installed, if no please see: [http://tridge.github.io/MAVProxy/](http://tridge.github.io/MAVProxy/)
- Dron Api installed, if not please see: http://dev.ardupilot.com/wiki/droneapi-tutorial/
- Mavconn installed, if not please see: https://pixhawk.ethz.ch/software/mavconn/start

How to run Lineal-Control
=========================
Start MavProxy :
``sudo mavproxy.py --master=/dev/ttyUSB0 --baudrate=57600``
Load module Drone Api:
``module load droneapi.module.api``
Start main python program:
``api start small_demo.py``

How to run Vision-Object-Trackin
================================

How to run Follow-me
====================


