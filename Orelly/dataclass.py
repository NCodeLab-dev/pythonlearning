from dataclasses import dataclass

@dataclass
class marks:
    physics: float
    math: float

marks_object = marks(90,92)

print("physics marks",marks_object.physics)
print("maths marks", marks_object.math)
