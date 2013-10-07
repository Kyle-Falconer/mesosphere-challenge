Mesosphere Challenge
====================

### Problem Specification

Design and implement an elevator control system. What data structures,
interfaces and algorithms will you need? Your elevator control system should
be able to handle a few elevators -- up to 16.

You can use the language of your choice to implement an elevator control
system. In the end, your control system should provide an interface for:

  * Querying the state of the elevators (what floor are they on and where they
    are going),

  * receiving an update about the status of an elevator,

  * receiving a pickup request,

  * time-stepping the simulation.

For example, we could imagine in Scala an interface like this:

	trait ElevatorControlSystem {
		def status(): Seq[(Int, Int, Int)]
		def update(Int, Int, Int)
		def pickup(Int, Int)
		def step()
	}

Here we have chosen to represent elevator state as 3 integers:

  Elevator ID, Floor Number, Goal Floor Number

An update alters these numbers for one elevator. A pickup request is two
integers:

  Pickup Floor, Direction (negative for down, positive for up)

This is not a particularly nice interface, and leaves some questions open. For
example, the elevator state only has one goal floor; but it is conceivable
that an elevator holds more than one person, and each person wants to go to a
different floor, so there could be a few goal floors queued up.

=========================================


#### Assumptions and Limitations
Each time step enables an elevator to reach one floor either above or below its current floor within that timeframe. That is, it takes an elevator one time tick to reach one floor.

The algorithm implemented is very naïve, using brute-force, first-in-first-out order for pickup requests and drop-offs. This could potentially make one of the elevators very busy while the others are waiting around.

#### Known issues:
Update and step commands are not fully implemented.

No load-balancing implemented. If `step` is called after a pickup request, then all pickup requests will be handled by the first elevator.

### Usage and Examples

    > python elevators.py (number of elevators)

The program will then prompt, waiting for commands.

#### Possible commands:

 * status - returns the status of all the elevators in the form of a list of triples. Each triple represents one elevator: (Elevator ID, Floor Number, Goal Floor Number).
 * step - allows one unit of time to pass, effectively telling the elevators to go to the next goal floor.
 * pickup floor_number direction - adds a pickup request to the pending requests queue. The arguments (floor_number, direction) are separated by spaces.
 * quit - exits the program.

#### sample input (using provided "elevator_test_1.txt")

	> python elevators.py 3 < elevator_test_1.txt
	
	status		// print out status
	pickup 3 -1	// pickup request from floor 3 to go down
	status		// print out status
	step		// time tick
	pickup 2 1	// pickup request from floor 3 to go up
	status		// print out status
	step		// time tick
	pickup 1 1	// pickup request from floor 1 to go up
	status		// print out status
	step		// time tick