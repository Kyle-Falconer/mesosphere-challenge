#!/usr/local/bin/python
# -*- coding: latin-1 -*-
# Kyle Falconer
# Mesosphere Programming Challenge
# <2013-10-07 13:24 CDT>

import optparse, sys

class elevator:
    
    def __init__(self, id):
        """
        Instantiates a new elevator, with current floor = 1 and
        no goal floors.
        """
        self.id = id
        self.current_floor = 1
        self.goal_floors = list()
    
    def state(self):
        """
        Reports on the current state of this elevator.
        """
        return [self.id, self.current_floor, self.goal_floors]
        
    def get_next_floor(self):
        temp_floor = self.current_floor
    
    
        if len(self.goal_floors) > 0:
            if isinstance(self.goal_floors[0], tuple):
                direction = self.goal_floors[0][1]
                print("direction: "+str(direction))
                if direction < 0 :
                    # going down
                    temp_floor = temp_floor - 1
                else :
                    #going up
                    temp_floor = temp_floor + 1
            else:
                print("not a tuple!",self.goal_floors[0])
            
        return temp_floor
    
    def update(self, cur_floor, goal_floor):
        """
        Updates the current floor and removes from the goal floors
        any floor numbers which are equal to the current floor.
        This is analogous to having the riders of an elevator leave
        the elevator when it has reached their floor.
        """ 
        self.cur_floor = cur_floor
        
        for floor in self.goal_floors:
            if self.cur_floor == floor[0]:
                self.goal_floors.remove(floor)
        
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
    
    def step(self):
        for i in range(0, len(self.elevators)):
        
            if len(self.pickup_requests) > 0:
                pickup = self.pickup_requests.pop()
                print("sending pickup request "+str(pickup)+" to elevator "+str(i))
                self.update(i, self.elevators[i].get_next_floor(), pickup)
            elif len(self.elevators[i].goal_floors) == 0:
                print("no pickup request and no goal floors for elevator "+str(i))
                continue
            else:
                print("no pickup request; sending elevator "+str(i)+" to next goal floor")
                self.update(i, self.elevators[i].get_next_floor(), self.elevators[i].current_floor)

        
        
def main():
    args = sys.argv[1:]
    print('number of elevators: '+ args[0])
    ecs = elevatorControlSystem(int(args[0]))
    
    while True:
        line = ''
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
            print('')
        elif line.startswith('pickup'):
            ecs.pickup(int(line.split(' ')[1]), int(line.split(' ')[2]))
            print('')


if __name__ == '__main__':
    main()
