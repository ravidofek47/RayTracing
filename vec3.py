import math

import numpy as np


class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        # Store as a NumPy array
        self.e = np.array([x, y, z], dtype=float)

    def __copy__(self):
        return Vec3(x=self.x(), y=self.y(), z=self.z())

    # Alternate constructor from any array-like
    @classmethod
    def from_array(cls, arr):
        arr = np.asarray(arr, dtype=float)
        if arr.shape != (3,):
            raise ValueError("Vec3 requires an array of shape (3,)")
        return cls(arr[0], arr[1], arr[2])

    # Accessors (C++ style: v.x(), v.y(), v.z())
    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    # Or Pythonic properties (optional, but convenient)
    @property
    def X(self):
        return self.e[0]

    @property
    def Y(self):
        return self.e[1]

    @property
    def Z(self):
        return self.e[2]

    # Indexing
    def __getitem__(self, i):
        return self.e[i]

    def __setitem__(self, i, value):
        self.e[i] = value

    # Unary minus
    def __neg__(self):
        return Vec3.from_array(-self.e)

    # In-place operators
    def __iadd__(self, other):
        if isinstance(other, Vec3):
            self.e += other.e
        else:
            self.e += other  # assumes array-like or scalar
        return self

    def __imul__(self, t):
        self.e *= t
        return self

    def __itruediv__(self, t):
        self.e /= t
        return self

    # Binary operators
    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3.from_array(self.e + other.e)
        return Vec3.from_array(self.e + other)

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3.from_array(self.e - other.e)
        return Vec3.from_array(self.e - other)

    def __mul__(self, other):
        # Elementwise product if other is Vec3 (like C++ code),
        # scalar multiplication otherwise.
        if isinstance(other, Vec3):
            return Vec3.from_array(self.e * other.e)
        return Vec3.from_array(self.e * other)

    def __rmul__(self, other):
        # scalar * Vec3
        return Vec3.from_array(other * self.e)

    def __truediv__(self, t):
        return Vec3.from_array(self.e / t)

    # Lengths
    def length_squared(self) -> float:
        return float(np.dot(self.e, self.e))

    def length(self) -> float:
        return float(np.sqrt(self.length_squared()))

    # Pretty printing
    def __repr__(self):
        return f"Vec3({self.e[0]}, {self.e[1]}, {self.e[2]})"

    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def unit(self):
        l = self.length()
        if l == 0:
            return Vec3()
        else:
            return self / l

    def dot(self, other) -> float:
        if isinstance(other, Vec3):
            return self.e.dot(other.e)
