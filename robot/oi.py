"""
Ctrl-Z FRC Team 4096
FIRST Robotics Competition 2023
Code for robot ""
contact@team4096.org

Some code adapted from:pip install numpy
https://github.com/SwerveDriveSpecialties
"""

# This is to help vscode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from robot import Robot  # type: ignore

from wpilibextra.customcontroller.custom_button import CustomButton as Button
from wpimath.geometry import Translation2d

# Controls
from wpilibextra.customcontroller import XboxCommandController

###  IMPORTS ###


class OI:
	"""
	Operator Input - This class ties together controls and commands.
	"""

	def __init__(self, robot: "Robot"):
		self.robot = robot

		# Controllers
		self.driver1 = XboxCommandController(0)

		# self.driver1.LEFT_JOY_Y.setInverted(True)

		self.driver1.LEFT_JOY_X.setDeadzone(0.02)
		self.driver1.LEFT_JOY_Y.setDeadzone(0.02)
		self.driver1.RIGHT_JOY_X.setDeadzone(0.05)
		self.driver1.RIGHT_JOY_Y.setDeadzone(0.05)

		### Driving ###
		self.cardinal = 0
		self.cardinal_directing = False

		@self.robot.drivetrain.setDefaultCommand
		def _():
			target_angle = robot.drivetrain.get_yaw().degrees()

			while True:
				yield
				def square(x):
					return abs(x) * x
				forward_back = -square(self.driver1.LEFT_JOY_Y())
				left_right = -square(self.driver1.LEFT_JOY_X())
				if self.driver1.RIGHT_BUMPER():
					forward_back *= 0.5
					left_right *= 0.5
				rotate = -self.driver1.RIGHT_JOY_X()
				if self.cardinal_directing and rotate == 0:
					self.robot.drivetrain.drive_with_pid(
						Translation2d(forward_back, left_right) * 6,
						self.cardinal
					)
				else:
					self.cardinal_directing = False
					self.robot.drivetrain.drive(
						Translation2d(forward_back, left_right) * 6,
						rotate * 6,
						field_relative=True,
						is_open_loop=True,
					)
		
		@self.driver1.LEFT_BUMPER.whenPressed #Reset Gyro
		def _():
			robot.drivetrain.set_yaw(0)

		@self.driver1.LEFT_TRIGGER_AS_BUTTON.whenPressed
		def _():
			self.cardinal_directing = True
			self.cardinal = 180

		@self.driver1.RIGHT_TRIGGER_AS_BUTTON.whenPressed
		def _():
			self.cardinal_directing = True
			self.cardinal = 0


	def log(self):
		pass
