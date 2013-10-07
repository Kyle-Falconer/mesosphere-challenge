#!/usr/local/bin/python
# -*- coding: latin-1 -*-
# Kyle Falconer
# Mesosphere Programming Challenge
# <2013-10-07 13:24 CDT>

import optparse, os, sys

class elevator:
	
	def __init__(self, id):
		"""
		Instantiates a new elevator, with current floor = 1 and
		no goal floors.
		"""
		self.id = id
		self.current_floor = 1
		self.goal_floors = []
	
	def state(self):
		"""
		Reports on the current state of this elevator.
		"""
		return [self.id, self.current_floor, self.goal_floors]
	
	def update(self, cur_floor, goal_floor):
		"""
		Updates the current floor and removes from the goal floors
		any floor numbers which are equal to the current floor.
		This is analogous to having the riders of an elevator leave
		the elevator when it has reached their floor.
		""" 
		self.cur_floor = cur_floor
		
		while cur_floor in self.goal_floors:
			self.goal_floors.remove(cur_floor)
		
		self.goal_floors.append(goal_floor)

	
	
		
class elevatorControlSystem:
	
	def __init__(self, num_elevators):
		self.elevators =  list()
		self.pickup_requests = list()
		for i in range(0, num_elevators):
			self.elevators.append(elevator(i))
		
	def status(self):
		"""
		Returns a list of triples, each triple containing the current 
		status of an elevator. The number of triples ("elevators") returned 
		is equal to the number of elevators in the elevator control system.
		[(Elevator ID, Floor Number, Goal Floor Number)]
		"""
		return [(e.id, e.current_floor, e.goal_floors) for e in self.elevators ]
		
	def update(self, id, cur_floor, goal_floor):
		self.elevators[id].update(cur_floor, goal_floor)
	
	def pickup(self, pickupFloor, direction):
		# pickupFloor: which floor the request comes from
		# direction: (negative for down, positive for up)
		self.pickup_requests.append((pickupFloor, direction))
		return None
	
	def step(self):
		for elevator in self.elevators:
			if len(elevator.goal_floors) == 0 : continue
			next_floor = elevator.goal_floors.pop(0)
			if len(self.pickup_requests) > 0:
				pickup = self.pickup_requests.pop()
				print("sending pickup request "+pickup+" to elevator "+e.id)
				elevator.update(next_floor, pickup)
			else:
				print("no pickup request; sending elevator "+e.id+" to next goal floor")
				elevator.update(next_floor, elevator.goal_floor.pop(0))
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
		
		if line == 'quit':
			break
		elif line == "status":
			print(ecs.status())
		elif line == "step":
			ecs.step()
		elif line.startswith('pickup'):
			ecs.pickup(line.split(' ')[1], line.split(' ')[2])


if __name__ == '__main__':
    main()
