# Ctrl-Z FRC Team 4096 - Starter Swerve Code 2023

This codebase is for teams implementing swerve using python using 2023 libraries.

## Overview

The code is written in Python 3, using the [robotpy](http://robotpy.readthedocs.io/en/latest/) libraries. It uses a coroutine version of command-based.

## Layout

- `/robot/robot.py` - Boilerplate and subsystem initialization
- `/robot/oi.py` - Joystick button bindings
- `/robot/const.py` - Constants for swerve drive
- `/robot/subsystems` - Subsystems
- `/robot/swerve` - Python port of 364's Base Falcon Swerve
- `/robot/wpilibextra` - Extra functionality on top of wpilib. Includes coroutine commands implementation, decorator based xbox controller wrapper, PIDD2 controller (unused), Remote repl, and dynamic view only robot object creator (unused).
- `/robot/remote_shell_ds.py` - Client side of the remote repl tool. More info/usage at https://github.com/TheTripleV/robotpy-remoterepl


## Questions?

Feel free to email us:
contact@team4096.org

[Ctrl-Z website](http://team4096.org/)
