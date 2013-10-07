#!/usr/local/bin/python
# -*- coding: latin-1 -*-
# Kyle Falconer
# Mesosphere Programming Challenge
# <2013-10-07 13:24 CDT>

import optparse, os, sys

class elevator:
	
	def __init__(self, id):
		self.id = id
		self.current_floor = 1
		self.goal_floors = []
	
	def state(self):
		return [self.id, self.current_floor, self.goal_floors]
	
		
class elevatorControlSystem:
	
	def __init__(self, num_elevators):
		self.elevators =  list()
		for i in range(0, num_elevators):
			self.elevators.append(elevator(i))
		
	def status(self):
		# [Elevator ID, Floor Number, Goal Floor Number]
		return [(e.id, e.current_floor, e.goal_floors) for e in self.elevators ]
		
	def update(self):
		return [0,0,0]
	
	def pickup(self, pickupFloor, direction):
		# pickupFloor: which floor the request comes from
		# direction: (negative for down, positive for up)
		return None
	
	def step(self):
		return None
		
		
def main():
	args = sys.argv[1:]
	print('number of elevators: '+ args[0])
	ecs = elevatorControlSystem(int(args[0]))
	print(ecs.status())
	while True:
		try:
			line = input('ecs> ')
		except EOFError:
			break
		
		if line == '' or line.isspace(): break
		
		try:
			e = Parser(line).parse()
			
		except ParseError as err:
			logging.critical('parse error: '+str(err.message))

if __name__ == '__main__':
    main()
