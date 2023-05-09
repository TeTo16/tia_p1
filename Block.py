from dataclasses import dataclass
@dataclass
class Block:
    id: int
    weight: float

    def __eq__(self, other):
        if self.id == other.id:
            return True
        return False

b1 = Block(1, 10.0)
b2 = Block(2, 5.0)
b3 = Block(3, 2.5)
b4 = Block(4, 1.0)
b5 = Block(5, 0.5)

blocks = [b1, b2, b3, b4, b5]