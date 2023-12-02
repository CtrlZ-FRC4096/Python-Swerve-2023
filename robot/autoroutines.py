# This is to help vscode
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from robot import Robot

from wpilibextra.coroutine.coroutine_command import commandify
from wpilib import Timer
import wpimath.geometry

def _wait(time):
	timer = Timer()
	timer.start()
	while not timer.hasElapsed(time):
		yield

def _stationary_spin(robot: "Robot", rotation: float, abs_tol: float = 2):
	first_time = True
	while not abs(robot.drivetrain.angle_pid.getPositionError()) < abs_tol or first_time:
		yield
		first_time = False
		robot.drivetrain.drive_with_pid(
			wpimath.geometry.Translation2d(0, 0),
			rotation
		)
@commandify
def spin(robot: "Robot"):
	yield from _stationary_spin(robot, 0)