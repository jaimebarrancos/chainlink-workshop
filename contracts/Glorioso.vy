# @version ^0.3.6

championships: public(uint8)
points: public(uint256)
birth: uint256

@external
def __init__():
    self.championships = 37
    self.birth = 1904

@external
def win() -> uint8:
    self.championships += 1
    return self.championships

@external
def add_points(step: uint256):
    self.points += step

@view
@external
def get_birth() -> uint256:
    return self.birth