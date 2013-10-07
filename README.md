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

Please provide a source tarball (or link to a GitHub repository) containing
code in the language of your choice, as well as a README discussing your
solution (and providing build instructions).


#### Assumptions
Each time step enables an elevator to reach its goal floor within that timeframe. That is, it takes an elevator 0 time to reach its destination.

### Usage and Examples

    > python elevators.py (number of elevators)

The program will then prompt, waiting for commands.

#### sample input

	2			// number of elevators
	status		// print out status
	pickup 3 -1	// pickup request from floor 3 to go down
	status		// print out status
	step		// time tick
	pickup 2 1	// pickup request from floor 3 to go down
	status		// print out status
	step		// time tick
	pickup 1 1	// pickup request from floor 1 to go up
	status		// print out status
	step		// time tick