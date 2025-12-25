import math
class Interval:
    def __init__(self, min_val=-math.inf, max_val=math.inf):
        # Default interval is empty: (min = +inf, max = -inf)
        self.min = min_val
        self.max = max_val

    def size(self) -> float:
        return self.max - self.min

    def contains(self, x: float) -> bool:
        return self.min < x < self.max

    def surrounds(self, x: float) -> bool:
        return self.min < x < self.max
    def clamp(self, x: float):
        if x < self.min:
            return self.min
        if x > self.max:
            return self.max
        return x

    def __repr__(self):
        return f"Interval({self.min}, {self.max})"
