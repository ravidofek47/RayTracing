from vec3 import Vec3

class Ray:
    def __init__(self, A: Vec3, B: Vec3):
        self.origin = A
        self.direction = B
        # A
    def at(self, t):
        return self.origin + self.direction * t

    def direction(self):
        return self.direction

    def origin(self):
        return self.origin
