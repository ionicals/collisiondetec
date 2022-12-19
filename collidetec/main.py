import math

class CollisionSimulator:
  def __init__(self, mass1, velocity1, mass2, velocity2):
    self.mass1 = mass1
    self.velocity1 = velocity1
    self.mass2 = mass2
    self.velocity2 = velocity2
  
  def simulate(self):
    # Calculate the new velocities of the objects after the collision
    new_velocity1 = (self.mass1 - self.mass2) / (self.mass1 + self.mass2) * self.velocity1 + (2 * self.mass2) / (self.mass1 + self.mass2) * self.velocity2
    new_velocity2 = (2 * self.mass1) / (self.mass1 + self.mass2) * self.velocity1 + (self.mass2 - self.mass1) / (self.mass1 + self.mass2) * self.velocity2
    
    # Update the velocities of the objects
    self.velocity1 = new_velocity1
    self.velocity2 = new_velocity2

# Create a CollisionSimulator with two objects of mass 1 and initial velocities of 5 and -5
simulator = CollisionSimulator(1, 5, 1, -5)

# Simulate the collision
simulator.simulate()

# Print the new velocities of the objects
print(simulator.velocity1)
print(simulator.velocity2)