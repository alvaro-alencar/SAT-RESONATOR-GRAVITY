# node.py

from z3 import Bool

class DecisionNode:
    def __init__(self, id, state=False, mass=0.0):
        self.id = id
        self.state = state
        self.mass = mass
        self.z3_var = Bool(f"node_{self.id}")

    def __repr__(self):
        return f"Node(id={self.id}, state={self.state}, mass={self.mass})"